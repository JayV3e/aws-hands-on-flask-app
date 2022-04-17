from app import app
import logging
import logging.handlers as handlers
import wsgi

logger = logging.getLogger('MainProgram')
logger.setLevel(10)
logHandler = handlers.RotatingFileHandler('flask.log',maxBytes =1000000, backupCount=1)
logger.addHandler(logHandler)
logger.info("Logging configuration done")

if __name__ == "__main__":
    server=  wsgi.WSGIServer(('0.0.0.0', 5000), app, log=logger)
    server.serve_forever()