# 参考記事

- [Write Your Own HTTP Server](https://betterprogramming.pub/writing-your-own-http-server-introduction-b2f94581268b)
- [伸び悩んでいる 3 年目 Web エンジニアのための、Python Web アプリケーション自作入門](https://zenn.dev/bigen1925/books/introduction-to-web-application-with-python)

# Signal について

Signal とはプロセスとプロセスの間で通信を行う際に使用される信号のこと。<br>
Signal を受け取ったプロセスなんらかの動作を行う<br>

SIGINT : キーボードからの割り込みシグナル(insert)<br>
SIGTERM : 終了シグナル kill コマンドのデフォルトシグナル(terminate)<br>
SIGHUP : 制御端末の切断、仮想端末の終了(hung up)<br>

# Socket について

Socket には Client と Listener がある。ブラウザは Client, Server は Client,Listenr の両方を持つ<br>
ListenerSocket は IP とポートにバインドして、Client が接続するのを待つ。<br>
Web サイトのアドレスをブラウザに入力したとき、ブラウザは自分の側でクライアントソケットを作成し、ウェブサイトのドメインの DNS 解決によって得られた IP アドレスを使ってウェブサーバに接続しようとします。（デフォルトでは、ポート番号 80 が使用される）<br>
このポートは SocketListener がバインドされているポートならどの番号でもよい。<br>

接続要求が到着すると、ListenerSocket は Server 上に新しい ClientSocket を作成し、接続要求元のの ClientSocket をこの新しい ClientSocket に接続します。これで、両方の ClientSocket が自由に通信できるようになります。<br>
つまり、実際に通信を行うのは ClientSocket 同士であり、ListenerSocket は Server 側に新しい ClientSocket を作成し、つなぐ役割を担う。<br>
このように ListenerSocket がたくさんの ClientSocket を作成していくことで、Server は複数の要求に対応できる<br>

# WSGI(Web Server Gateway Interface)について

アプリケーションが好きなサーバーにデプロイできるように、アプリケーションとサーバーの間を取り持ち、全てのサーバーと同じ方法でアプリケーションを通信し、デプロイを可能にする<br>
WSGI が定義する内容
・任意の Web サーバがどのようにアプリケーションを呼び出すか<br>
・どのようなパラメータを送信するか<br>
・どのような結果を期待するか<br>
