# HTTPS について

HTTPSは単に「有効」か「無効」かで決まるものだと思いがちです。

しかし、それよりもはるかに複雑です。

!!! tip
    もし急いでいたり、HTTPSの仕組みについて気にしないのであれば、次のセクションに進み、さまざまなテクニックを使ってすべてをセットアップするステップ・バイ・ステップの手順をご覧ください。

利用者の視点から **HTTPS の基本を学ぶ**に当たっては、次のリソースをオススメします: <a href="https://howhttps.works/" class="external-link" target="_blank">https://howhttps.works/</a>.

さて、**開発者の視点**から、HTTPSについて考える際に念頭に置くべきことをいくつかみていきましょう：

* HTTPSの場合、**サーバ**は**第三者**によって生成された**「証明書」を持つ**必要があります。
    * これらの証明書は「生成」されたものではなく、実際には第三者から**取得**されたものです。
* 証明書には**有効期限**があります。
    * つまりいずれ失効します。
    * そのため**更新**をし、第三者から**再度取得**する必要があります。
* 接続の暗号化は**TCPレベル**で行われます。
    * それは**HTTPの1つ下**のレイヤーです。
    * つまり、**証明書と暗号化**の処理は、**HTTPの前**に行われます。
* **TCPは "ドメイン "について知りません**。IPアドレスについてのみ知っています。
    * 要求された**特定のドメイン**に関する情報は、**HTTPデータ**に入ります。
* **HTTPS証明書**は、**特定のドメイン**を「証明」しますが、プロトコルと暗号化はTCPレベルで行われ、どのドメインが扱われているかを**知る前**に行われます。
* **デフォルトでは**、**IPアドレスごとに1つのHTTPS証明書**しか持てないことになります。
    * これは、サーバーの規模やアプリケーションの規模に寄りません。
    * しかし、これには**解決策**があります。
* **TLS**プロトコル(HTTPの前に、TCPレベルで暗号化を処理するもの)には、**<a href="https://en.wikipedia.org/wiki/Server_Name_Indication" class="external-link" target="_blank"><abbr title="サーバー名表示">SNI</abbr></a>**と呼ばれる**拡張**があります。
    * このSNI拡張機能により、1つのサーバー（**単一のIPアドレス**を持つ）が**複数のHTTPS証明書**を持ち、**複数のHTTPSドメイン/アプリケーション**にサービスを提供できるようになります。
    * これが機能するためには、**パブリックIPアドレス**でリッスンしている、サーバー上で動作している**単一の**コンポーネント(プログラム)が、サーバー内の**すべてのHTTPS証明書**を持っている必要があります。

* セキュアな接続を取得した**後**でも、通信プロトコルは**HTTPのまま**です。
    * コンテンツは**HTTPプロトコル**で送信されているにもかかわらず、**暗号化**されています。


サーバー（マシン、ホストなど）上で**1つのプログラム/HTTPサーバー**を実行させ、**HTTPSに関する全てのこと**を管理するのが一般的です。

**暗号化された HTTPS リクエスト** を受信し、**復号化された HTTP リクエスト** を同じサーバーで実行されている実際の HTTP アプリケーション（この場合は **ReadyApi** アプリケーション）に送信し、アプリケーションから **HTTP レスポンス** を受け取り、適切な **HTTPS 証明書** を使用して **暗号化** し、そして**HTTPS** を使用してクライアントに送り返します。

このサーバーはしばしば **<a href="https://en.wikipedia.org/wiki/TLS_termination_proxy" class="external-link" target="_blank">TLS Termination Proxy</a>**と呼ばれます。

TLS Termination Proxyとして使えるオプションには、以下のようなものがあります：

* Traefik（証明書の更新も対応）
* Caddy (証明書の更新も対応)
* Nginx
* HAProxy


## Let's Encrypt

Let's Encrypt以前は、これらの**HTTPS証明書**は信頼できる第三者によって販売されていました。

これらの証明書を取得するための手続きは面倒で、かなりの書類を必要とし、証明書はかなり高価なものでした。

しかしその後、**<a href="https://letsencrypt.org/" class="external-link" target="_blank">Let's Encrypt</a>** が作られました。

これはLinux Foundationのプロジェクトから生まれたものです。 自動化された方法で、**HTTPS証明書を無料で**提供します。これらの証明書は、すべての標準的な暗号化セキュリティを使用し、また短命（約3ヶ月）ですが、こういった寿命の短さによって、**セキュリティは実際に優れています**。

ドメインは安全に検証され、証明書は自動的に生成されます。また、証明書の更新も自動化されます。

このアイデアは、これらの証明書の取得と更新を自動化することで、**安全なHTTPSを、無料で、永遠に**利用できるようにすることです。

## 開発者のための HTTPS

ここでは、HTTPS APIがどのように見えるかの例を、主に開発者にとって重要なアイデアに注意を払いながら、ステップ・バイ・ステップで説明します。

### ドメイン名

ステップの初めは、**ドメイン名**を**取得すること**から始まるでしょう。その後、DNSサーバー（おそらく同じクラウドプロバイダー）に設定します。

おそらくクラウドサーバー（仮想マシン）かそれに類するものを手に入れ、<abbr title="変わらない">固定の</abbr> **パブリックIPアドレス**を持つことになるでしょう。

DNSサーバーでは、**取得したドメイン**をあなたのサーバーのパプリック**IPアドレス**に向けるレコード（「`Aレコード`」）を設定します。

これはおそらく、最初の1回だけあり、すべてをセットアップするときに行うでしょう。

!!! tip
    ドメイン名の話はHTTPSに関する話のはるか前にありますが、すべてがドメインとIPアドレスに依存するため、ここで言及する価値があります。

### DNS

では、実際のHTTPSの部分に注目してみよう。

まず、ブラウザは**DNSサーバー**に**ドメインに対するIP**が何であるかを確認します。今回は、`someapp.example.com`とします。

DNSサーバーは、ブラウザに特定の**IPアドレス**を使用するように指示します。このIPアドレスは、DNSサーバーで設定した、あなたのサーバーが使用するパブリックIPアドレスになります。

<img src="/img/deployment/https/https01.svg">

### TLS Handshake の開始

ブラウザはIPアドレスと**ポート443**（HTTPSポート）で通信します。

通信の最初の部分は、クライアントとサーバー間の接続を確立し、使用する暗号鍵などを決めるだけです。

<img src="/img/deployment/https/https02.svg">

TLS接続を確立するためのクライアントとサーバー間のこのやりとりは、**TLSハンドシェイク**と呼ばれます。

### SNI拡張機能付きのTLS

サーバー内の**1つのプロセス**だけが、特定 の**IPアドレス**の特定の**ポート** で待ち受けることができます。

同じIPアドレスの他のポートで他のプロセスがリッスンしている可能性もありますが、IPアドレスとポートの組み合わせごとに1つだけです。

TLS（HTTPS）はデフォルトで`443`という特定のポートを使用する。つまり、これが必要なポートです。

このポートをリッスンできるのは1つのプロセスだけなので、これを実行するプロセスは**TLS Termination Proxy**となります。

TLS Termination Proxyは、1つ以上の**TLS証明書**（HTTPS証明書）にアクセスできます。

前述した**SNI拡張機能**を使用して、TLS Termination Proxy は、利用可能なTLS (HTTPS)証明書のどれを接続先として使用すべきかをチェックし、クライアントが期待するドメインに一致するものを使用します。

今回は、`someapp.example.com`の証明書を使うことになります。

<img src="/img/deployment/https/https03.svg">

クライアントは、そのTLS証明書を生成したエンティティ（この場合はLet's Encryptですが、これについては後述します）をすでに**信頼**しているため、その証明書が有効であることを**検証**することができます。

次に証明書を使用して、クライアントとTLS Termination Proxy は、 **TCP通信**の残りを**どのように暗号化するかを決定**します。これで**TLSハンドシェイク**の部分が完了します。

この後、クライアントとサーバーは**暗号化されたTCP接続**を持ちます。そして、その接続を使って実際の**HTTP通信**を開始することができます。

これが**HTTPS**であり、純粋な（暗号化されていない）TCP接続ではなく、**セキュアなTLS接続**の中に**HTTP**があるだけです。

!!! tip
    通信の暗号化は、HTTPレベルではなく、**TCPレベル**で行われることに注意してください。

### HTTPS リクエスト

これでクライアントとサーバー（具体的にはブラウザとTLS Termination Proxy）は**暗号化されたTCP接続**を持つことになり、**HTTP通信**を開始することができます。

そこで、クライアントは**HTTPSリクエスト**を送信します。これは、暗号化されたTLSコネクションを介した単なるHTTPリクエストです。

<img src="/img/deployment/https/https04.svg">

### リクエストの復号化

TLS Termination Proxy は、合意が取れている暗号化を使用して、**リクエストを復号化**し、**プレーン (復号化された) HTTP リクエスト** をアプリケーションを実行しているプロセス (例えば、ReadyApi アプリケーションを実行している Uvicorn を持つプロセス) に送信します。

<img src="/img/deployment/https/https05.svg">

### HTTP レスポンス

アプリケーションはリクエストを処理し、**プレーン(暗号化されていない)HTTPレスポンス** をTLS Termination Proxyに送信します。

<img src="/img/deployment/https/https06.svg">

### HTTPS レスポンス

TLS Termination Proxyは次に、事前に合意が取れている暗号(`someapp.example.com`の証明書から始まる)を使って**レスポンスを暗号化し**、ブラウザに送り返す。

その後ブラウザでは、レスポンスが有効で正しい暗号キーで暗号化されていることなどを検証します。そして、ブラウザはレスポンスを**復号化**して処理します。

<img src="/img/deployment/https/https07.svg">

クライアント（ブラウザ）は、レスポンスが正しいサーバーから来たことを知ることができます。 なぜなら、そのサーバーは、以前に**HTTPS証明書**を使って合意した暗号を使っているからです。

### 複数のアプリケーション

同じサーバー（または複数のサーバー）に、例えば他のAPIプログラムやデータベースなど、**複数のアプリケーション**が存在する可能性があります。

特定のIPとポート（この例ではTLS Termination Proxy）を扱うことができるのは1つのプロセスだけですが、他のアプリケーション/プロセスも、同じ**パブリックIPとポート**の組み合わせを使用しようとしない限り、サーバー上で実行することができます。

<img src="/img/deployment/https/https08.svg">

そうすれば、TLS Termination Proxy は、**複数のドメイン**や複数のアプリケーションのHTTPSと証明書を処理し、それぞれのケースで適切なアプリケーションにリクエストを送信することができます。

### 証明書の更新

将来のある時点で、各証明書は（取得後約3ヶ月で）**失効**します。

その後、Let's Encryptと通信する別のプログラム（別のプログラムである場合もあれば、同じTLS Termination Proxyである場合もある）によって、証明書を更新します。

<img src="/img/deployment/https/https.svg">

**TLS証明書**は、IPアドレスではなく、**ドメイン名に関連付けられて**います。

したがって、証明書を更新するために、更新プログラムは、認証局（Let's Encrypt）に対して、**そのドメインが本当に「所有」し、管理している**ことを**証明**する必要があります。

そのために、またさまざまなアプリケーションのニーズに対応するために、いくつかの方法があります。よく使われる方法としては:

* **いくつかのDNSレコードを修正します。**
    * これをするためには、更新プログラムはDNSプロバイダーのAPIをサポートする必要があります。したがって、使用しているDNSプロバイダーによっては、このオプションが使える場合もあれば、使えない場合もあります。
* ドメインに関連付けられたパブリックIPアドレス上で、（少なくとも証明書取得プロセス中は）**サーバー**として実行します。
    * 上で述べたように、特定のIPとポートでリッスンできるプロセスは1つだけです。
    * これは、同じTLS Termination Proxyが証明書の更新処理も行う場合に非常に便利な理由の1つです。
    * そうでなければ、TLS Termination Proxyを一時的に停止し、証明書を取得するために更新プログラムを起動し、TLS Termination Proxyで証明書を設定し、TLS Termination Proxyを再起動しなければならないかもしれません。TLS Termination Proxyが停止している間はアプリが利用できなくなるため、これは理想的ではありません。


アプリを提供しながらこのような更新処理を行うことは、アプリケーション・サーバー（Uvicornなど）でTLS証明書を直接使用するのではなく、TLS Termination Proxyを使用して**HTTPSを処理する別のシステム**を用意したくなる主な理由の1つです。

## まとめ

**HTTPS**を持つことは非常に重要であり、ほとんどの場合、かなり**クリティカル**です。開発者として HTTPS に関わる労力のほとんどは、これらの**概念とその仕組みを理解する**ことです。

しかし、ひとたび**開発者向けHTTPS**の基本的な情報を知れば、簡単な方法ですべてを管理するために、さまざまなツールを組み合わせて設定することができます。

次の章では、**ReadyApi** アプリケーションのために **HTTPS** をセットアップする方法について、いくつかの具体例を紹介します。🔒