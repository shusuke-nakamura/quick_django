# quick_django

## 仮想環境

python -m venv django3

## django のインストール

pip install django==3.2

## アプリの作成

python manage.py startapp main

## アプリを実行する

python manage.py runserver

## マイグレーションファイルを作成する

python manage.py makemigrations アプリ名

## マイグレーションファイルによって実施される SQL の確認

python manage.py sqlmigrate アプリ名 マイグレーション名

## マイグレーションを実施する

python manage.py migrate

## 管理ユーザの作成

python manage.py createsuperuser
db_user/db_pass12345

## Django Shell

python manage.py shell
