# Foobar
Демо-проект задачи 'foobar'.

Написать программу, которая принимает на вход последовательность чисел.
- Для каждого числа, делящегося на 3, программа должна выводить строку "foo"
- Для каждого числа, делящегося на 5, программа должна выводить строку "bar"
- Для каждого числа, делящегося и на 3 и на 5, программа должна выводить строку "foobar"

Развёрнутый проект (при первом открытии ссылки возможна задержка до 60 секунд): [https://foobar-6qgv.onrender.com](https://foobar-6qgv.onrender.com)

## Запуск проекта в контейнере Docker
Скачать образ и запустить контейнер:

```shell
docker run --rm -p 8000:8000 ghcr.io/albaranovsky/foobar:main
```

Открыть в браузере ссылку: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Запуск проекта локально
Клонировать репозиторий и перейти в него в командной строке:

```shell
git clone https://github.com/albaranovsky/foobar.git
```

```shell
cd foobar
```

Создать и активировать виртуальное окружение:

```shell
python3 -m venv venv
```

```shell
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```shell
python3 -m pip install --upgrade pip
```

```shell
pip install -r requirements.txt
```

Запустить сервер:

```shell
gunicorn app:app 
```

Открыть в браузере ссылку: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
