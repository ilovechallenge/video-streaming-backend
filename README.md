# movie_backend

# サーバ側構築
# このプロジェクトは Python/Django を使用しています。

# 開発環境の構築手順

#### １．Python仮想環境を作成します。
```
pip install virtualenv
python -m venv env
env\Scripts\activate.bat(Windows)
source env/bin/activate(macOS, Linux)
```
#### 2．プロジェクトに必要なPythonモジュールのインストール。
```
cd movie_backend
pip install -r requirements.txt
```
#### 3．バックエンドサーバ起動。
```
python manage.py runserver

起動後、プロジェクトのSwagger文書を127.0.0.1:8000/docsで確認できます。
```
