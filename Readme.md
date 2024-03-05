# これは何？
 - あるPNG画像に入ったExif情報を、別のJPG画像にコピーする簡単なツールです。

 - 使用ケースとして、[VRCImageHelper](https://github.com/m-hayabusa/VRCImageHelper) で取得したPNGをLightroom等で現像してJPGとして書き出した後に、元のPNGからExif情報を持ってくることを想定しています。（現像ソフトで書きだすとPNGに入っていたExifが無視されて消えるため。）
 - 1枚ずつでしか使えません。[Backlog]

## 使用方法
1. [Release](https://github.com/Nyataro-vr/EXIFcopyPNGtoJPG/releases) のAssetsから実行ファイルのzip (EXIFcopyPNGtoJPG_releaseXX.zip)をダウンロードしてください。

2. zipを解凍後、中のexeを実行してください。詳しくは同梱のHowtoUse.txtを参照してください。


- - - -
### 参考情報：自分でビルドする場合
中身はPythonスクリプトをpyinstallerでビルドした簡単なものなので、WindowsのPython環境を使いローカルでビルドすることも可能です。需要は分かりませんが個人メモを兼ねて記載しておきます。

Windows10でのビルドを確認しています。

Windows11でも同様に出来ると思いますが仔細は異なる可能性があります。
#### 手順
1. **Python 3.12のインストール**
Microsoft StoreからPython 3.12をインストールします。

2. **仮想環境のセットアップ**
Powershell でスクリプトのフォルダへ移動し、以下コマンドを実行してvenv用のフォルダを作成します。  
`> python -m venv exif_copy_py`

3. **仮想環境の有効化**
作成した仮想環境をactivateします。  
`> .\exif_copy_py\Scripts\activate`

4. **tkinterのインストール**
GUI用のtkinterをpipを使ってインストールします。  
`> pip3 install pytk`

5. **Exif用モジュールのインストール**
piexifをpipを使ってインストールします。  
`> pip3 install piexif`

6. **Pillowのインストール**
Pillowをpipを使ってインストールします。  
`> pip install Pillow`

7. **pyinstallerのインストール**
実行ファイル作成のためにpyinstallerをpipを使ってインストールします。  
`> pip install pyinstaller`

8. **実行ファイルの作成**
スクリプトを指定してpyinstallerを実行します。  
`> pyinstaller .\exif_copy_exe.py --onefile --noconsole`

以上で、"…\EXIFcopyPNGtoJPG\dist\exif_copy_exe.exe"に実行ファイルが作成されます。