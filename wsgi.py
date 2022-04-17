from app import app

if __name__ == "__main__":
    import logging
    logging.basicConfig(filename='flask.log',level=logging.DEBUG)
    app.run()