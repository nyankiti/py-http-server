# py-http-server
自作http-server
参考記事: https://betterprogramming.pub/writing-your-own-http-server-introduction-b2f94581268b


# Signalについて
Signal とはプロセスとプロセスの間で通信を行う際に使用される信号のこと。<br>
Signal を受け取ったプロセスなんらかの動作を行う<br>

SIGINT : キーボードからの割り込みシグナル(insert)<br>
SIGTERM : 終了シグナル killコマンドのデフォルトシグナル(terminate)<br>
SIGHUP : 制御端末の切断、仮想端末の終了(hung up)<br>

# Socketについて
SocketにはClientとListenerがある。ブラウザはClient, ServerはClient,Listenrの両方を持つ<br>
ListenerSocketはIPとポートにバインドして、Clientが接続するのを待つ。<br>
Webサイトのアドレスをブラウザに入力したとき、ブラウザは自分の側でクライアントソケットを作成し、ウェブサイトのドメインのDNS解決によって得られたIPアドレスを使ってウェブサーバに接続しようとします。（デフォルトでは、ポート番号80が使用される）<br>
このポートはSocketListenerがバインドされているポートならどの番号でもよい。<br>

接続要求が到着すると、ListenerSocketはServer上に新しいClientSocketを作成し、接続要求元ののClientSocketをこの新しいClientSocketに接続します。これで、両方のClientSocketが自由に通信できるようになります。<br>
つまり、実際に通信を行うのはClientSocket同士であり、ListenerSocketはServer側に新しいClientSocketを作成し、つなぐ役割を担う。<br>
このようにListenerSocketがたくさんのClientSocketを作成していくことで、Serverは複数の要求に対応できる<br>

# WSGI(Web Server Gateway Interface)について
アプリケーションが好きなサーバーにデプロイできるように、アプリケーションとサーバーの間を取り持ち、全てのサーバーと同じ方法でアプリケーションを通信し、デプロイを可能にする<br>
WSGIが定義する内容
・任意のWebサーバがどのようにアプリケーションを呼び出すか<br>
・どのようなパラメータを送信するか<br>
・どのような結果を期待するか<br>


