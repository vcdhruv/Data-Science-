from logger import logging

def addition(a,b):
    logging.debug("addition is taking place.")
    return a+b

logging.debug("addition function is called.")
addition(10,15)


from logging.handlers import RotatingFileHandler

def logger_with_rotating_file_handler():
    logger = logging.getLogger('rotating_logger')
    logger.setLevel(logging.DEBUG)
    
    rotating_handler = RotatingFileHandler('rotating_app.log', maxBytes=2000, backupCount=5)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    rotating_handler.setFormatter(formatter)
    
    logger.addHandler(rotating_handler)
    
    for i in range(100):
        logger.debug('This is debug message number {}'.format(i))

# Test the function
logger_with_rotating_file_handler()

def logger_with_context():
    logger = logging.getLogger("contextual_information")
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("context_app.log")
    formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(funcName)s-%(lineno)d-%(message)s")
    file_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)

    def test_func():
        logger.debug('This is a debug message')
        logger.info('This is an info message')
        logger.warning('This is a warning message')
        logger.error('This is an error message')
        logger.critical('This is a critical message')
    
    test_func()
logger_with_context()

def logging_with_dictionary():
    logger = logging.getLogger('my_logger')

    file_handler = logging.FileHandler('dictionary_app.log')
    console = logging.StreamHandler()

    