# py-http-server
自作http-server

# Socketについて
SocketにはClientとListenerがある。ブラウザはClient, ServerはClient,Listenrの両方を持つ\\
ListenerSocketはIPとポートにバインドして、Clientが接続するのを待つ。\\
Webサイトのアドレスをブラウザに入力したとき、ブラウザは自分の側でクライアントソケットを作成し、ウェブサイトのドメインのDNS解決によって得られたIPアドレスを使ってウェブサーバに接続しようとします。（デフォルトでは、ポート番号80が使用される）\\
このポートはSocketListenerがバインドされているポートならどの番号でもよい。\\

接続要求が到着すると、ListenerSocketはServer上に新しいClientSocketを作成し、接続要求元ののClientSocketをこの新しいClientSocketに接続します。これで、両方のClientSocketが自由に通信できるようになります。\\
つまり、実際に通信を行うのはClientSocket同士であり、ListenerSocketはServer側に新しいClientSocketを作成し、つなぐ役割を担う。\\
このようにListenerSocketがたくさんのClientSocketを作成していくことで、Serverは複数の要求に対応できる
