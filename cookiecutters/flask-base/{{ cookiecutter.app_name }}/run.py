from services.application import create_app


if __name__ == '__main__':
    create_app().run(debug=True, port=8080)
