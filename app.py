# coding: utf-8
from bottle import route, run, get, static_file, template, default_app

@get("/")
def index():
     return template('template/index')


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static/')


if __name__ == "__main__":
    run(host='localhost', port=8080)

application = default_app()