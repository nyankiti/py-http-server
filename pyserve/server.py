import socket


class Server:

    # http://man7.org/linux/man-pages/man2/socket.2.html

    def setup(self, config):
        self.config = config
        self.socket = None

    def run(self):
        listen_port = self.config['port']
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('0.0.0.0', listen_port))
        # What is backlog
        self.socket.listen(self.config.get('backlog', 100))
        return self.socket

    def shutdown(self):
        if self.socket:
            self.socket.close()

'''
AF_INET : アドレスファミリを示す定数。sys/socket.h に定義されている
この値を指定すると「IPv4という種類の通信をするために必要なお約束事たちを使ってやり取りしてくれたまえ」な指示になります。
あえて回りくどい書き方をしましたが、要するに「IPv4で通信しろ！」な指定です。


Backlogは、サーバーが他の接続の受け入れに忙しくしている間に、オペレーティングシステムがキューに保持する接続要求の数を指定します。サーバーに大きな負荷がかかっている場合、すべての着信接続をすぐに受け入れることができないことがあります。保留中の接続数がバックログを超えると、新しい接続要求は直ちに失敗します。この数字は設定要素として提供されているので、サーバのユーザはキューの大きさを決めることができます。
キューを大きくすればするほど、それらの接続を保持するためにOSが使用するリソースが多くなります。バックログについての詳しい説明はStackOverflowのこちらの回答をご覧ください。

'''