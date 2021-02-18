# импортируем необходимые сущности библиотеки bottle
from bottle import route
from bottle import run

# регистрируем обработчик пути /hello/ с помощью декоратора route
@route("/")
def hello_world():
    return "Hello World!"  # Возвращаем приветственное сообщение

if __name__ == "__main__":
    # Запускаем веб-сервер с помощью функции run: указываем адрес узла и порт
    run(host="localhost", port=8080, debug=True)
    # Булев флаг debug=True запускает сервер в режиме отладки