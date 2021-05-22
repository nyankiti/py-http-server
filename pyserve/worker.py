import logging
import queue
import threading
from typing import Type

logger = logging.getLogger(__name__)

DUMMY_RESPONSE = '''HTTP/1.1 200 OK
Date: Mon, 27 Jul 2009 12:28:53 GMT
Server: Apache/2.2.14 (Win32)
Last-Modified: Stu, 22 May 2009 19:15:56 GMT
Content-Type: text/html
Connection: Closed
<html>
<body>
<h1>Hello, World!</h1>
</body>
</html>'''


class Worker:

    is_stopped = False

    def setup(self, config):
        self.config = config
        # What should be the size of this queue
        self.queue = queue.Queue(maxsize=config.get('concurrency', 10))
        self.kill_pill = threading.Event()
        threads = [RequestProcessorThread(name=f'RequestProcessor {i}', queue=self.queue, kill_pill=self.kill_pill) for i in range(config.get('concurrency', 10))]
        for t in threads:
            t.start()

    def run(self, listener):
        logger.info("Accepting connections now")
        while not self.is_stopped:
            sock, _ = listener.accept()
            self.submit(sock)

    def submit(self, sock):
        try:
            self.queue.put(sock, timeout=self.config.get('timeout', 5))
        except queue.Full:
            # Send 503 Service Unavailable
            pass

    def shutdown(self):
        self.is_stopped = True
        self.kill_pill.set()


class RequestProcessorThread(threading.Thread):

    def __init__(self, group=None, target=None, name=None, queue:queue.Queue=None, kill_pill=None, args=(), kwargs=None):
        super().__init__(group=group, target=target, name=name, args=args, kwargs=kwargs)
        self.queue: Type[queue.Queue] = queue
        self.kill_pill = kill_pill

    def run(self) -> None:
        logger.info(f"Running thread {self.name}")
        while not self.kill_pill.is_set():
            try:
                socket = self.queue.get(block=True, timeout=1)
                self.process(socket)
            except queue.Empty:
                continue

    def process(self, sock):
        p = HttpParser()
        body = []
        while True:
          # Warning: Calling recv without timeout
          # recv() はソケット上のデータを受信し、バッファーに保管する。
            data = sock.recv(1024)
            if not data:
                # The client closed the connection. Nothing to do anymore
                return

            p.execute(data, len(data))

            if p.is_partial_body():
                body.append(p.recv_body())

            if p.is_message_complete():
                break

        body = "".join(body)
        headers = p.get_headers()
        path = p.get_path()
        query = p.get_query_string()
        method = p.get_method()
        
        # Warning: Sending hard-coded response
        sock.send(str.encode(DUMMY_RESPONSE))
        sock.close()