# Bitly URL shortener

This is a script that allows you to shorten URLs using the Bitly API. If you provide a Bitlink, it will return the total number of clicks for that Bitlink.

### How to install

To use this script, you will first need to get a Bitly access token. You can get it from the Bitly website after registration. It will look something like this: "9f70cd85814b5fe2936abf685b". Store the token as an environment variable named BITLY_TOKEN.

Python3 should already be installed.

Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### How to run

In your terminal, navigate to the directory containing the script, then run the script with the command `python main.py [URL]`, replacing `[URL]` with the URL you want to shorten or the Bitlink you want to get the click count for.
```
python main.py https://example.com
```

### Project Goals

This code was written for educational purposes.


# Обрезка ссылок с помощью Битли

Это скрипт, позволяющий сокращать URL с помощью API Bitly. Если вы введете Bitlink, он вернет общее количество кликов по этому Bitlink.

### Как установить

Чтобы использовать этот скрипт, сначала вам нужно получить токен доступа Bitly. Вы можете найти его на сайте Bitly после регистрации. Он будет выглядеть примерно так: "9f70cd85814b5fe2936abf685b". Храните токен в виде переменной окружения с именем BITLY_TOKEN.

Python3 должен быть уже установлен.

Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Как запустить

В терминале перейдите в каталог, содержащий скрипт, затем запустите скрипт командой `python main.py [URL]`, заменив `[URL]` на URL, который вы хотите сократить, или на Bitlink, для которого вы хотите получить количество кликов.
```
python main.py https://example.com
```

### Цель проекта

Код написан в образовательных целях.