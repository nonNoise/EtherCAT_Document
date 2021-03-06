===================================================
EtherCAT 開発記録
===================================================

.. image:: ./img/top.JPG
   :scale: 15%

　
はじめに
---------------------------------------------------

このサイトは、産業用通信規格であるEtherCATの開発を行う際にメモした内容です。


EtherCATは、数ある産業用通信規格の中の一つで、民生用のPCで使用されている有線LANを使用し、
特別な機械を付けづに産業機器を制御出来る仕組みです。他にも利点があり、EtherCATの特徴として
「冗長性ある通信」「高速伝送」「同期動作」「その他の通信規格をラップする仕組み」などがあります。

EtherCATについては公式の内容を参考にしてください。

https://www.ethercat.org/jp.htm


★NEW 同人誌が発売になりました！
---------------------------------------------------

.. image:: ./img/C96.jpg
   :scale: 20%

**◎　電子書籍版(PDF)**

    https://artifactnoise.stores.jp/items/5c29dcefc49cf353509aa4cc

**◎　リアル冊子（フルカラー）**

    https://www.switch-science.com/catalog/5919/


★NEW モジュールが発売になりました！
---------------------------------------------------

.. image:: ./img/EtherCAT_LAN9252_TOP.jpg

**◎　AN-201_EtherCATスレーブ評価基板LAN9252使用**

    https://www.switch-science.com/catalog/5917/

**◎　AN-202_LED16モジュール**

    https://www.switch-science.com/catalog/5918/



目次
---------------------------------------------------

.. toctree::
    :maxdepth: 1

    rst/S01
    rst/S02_1

-  EtherCATの通信について

-  EtherCATのプロトコルについて

- コラム  EtherCATを動かしてみよう

    ★以上の内容を同人誌にまとめました！

    https://www.switch-science.com/catalog/5919/


-  EtherCATライブラリについて

-  EtherCATで自作ハードウェアを接続してみる

-  EtherCAT-Pの規格について

-  EtherCATの得意分野、不得意な分野

-  EtherCAT応用事例集

コラム
---------------------------------------------------

.. toctree::
    :maxdepth: 1

    rst/M01
    rst/M02
    rst/C01
    rst/C02

- Windowsで試す方法（調査中)

- MacOSで試す方法（調査中)

※以上の内容は常に変化と変更があります。書かない場合もあります。書籍化になる場合もあります。参考程度に。



購入サイト
---------------------------------------------------

- `EtherCAT GPIO16ポート LAN9252使用評価ボード <https://www.switch-science.com/catalog/5917/>`_

- `EtherCATモジュール用LEDx16ボード <https://www.switch-science.com/catalog/5917/>`_



著者について
---------------------------------------------------

本開発日誌は、ArtifactNoise,LLPに所属する北神が書いております。
 
ArtifactNoise,LLPは、EtherCATのメンバーとして登録されてます。

https://www.ethercat.org/jp/members/members_02F13528E14E4087BDE04CA4664FE382.htm

また、ベンダーIDも取得し、製品の開発についても前向きに検討しております。


ArtifactNoise,LLP

.. image:: ./img/logo-mini-320-132.png
	:alt: ArtifactNoise
	:scale: 80%
	:target: http://artifactnoise.com


-----------------------------------------------------------------
管理情報
-----------------------------------------------------------------
:管理者: 北神 雄太(Yuta Kitagami)
:連絡先: kitagami@Artifactnoise.com
:公開日: 2019/01/30 
:更新　: 2019/02/05
:更新　: 2019/05/13   モジュールの説明追加
:更新　: 2019/10/30   スイッチサイエンスにて発売開始

.. raw:: html

    <meta name="google-site-verification" content="ZZJWIExpSI4kqI2OdgaFy0BoygvFoBtrRHVR7wK2lBM" />
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-24204483-5"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'UA-24204483-5');
    </script>

