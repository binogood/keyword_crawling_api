from app import create_app as application


if __name__ == '__main__':
    app = application()
    app.run(host='0.0.0.0', port=41134, debug=True)