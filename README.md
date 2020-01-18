# 学習管理アプリ

## virtualenvwrapperのインストール
```
$ pip install virtualenvwrapper
$ export WORKON_HOME=~/Envs
$ mkdir -p $WORKON_HOME
$ source /usr/local/bin/virtualenvwrapper.sh
```

## 環境構築

```
$ git clone git@github.com:kai-tanaka/study-app.git
$ cd study-app
$ mkvirtualenv studyapp
$ pip install -r requirements.txt
```