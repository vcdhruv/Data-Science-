import logging 

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s-%(name)s-%(levelname)s-%(message)s",
    datefmt="%Y-%M-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

logger1 = logging.getLogger("module1")

def add(a,b):
    result = a + b
    logger1.debug(f"adding {a} + {b} = {result}")
    return result

def subtract(a,b):
    result = a - b
    logger1.debug(f"subtracting {a} - {b} = {result}")
    return result

def multiply(a,b):
    result = a * b
    logger1.debug(f"multiplying {a} * {b} = {result}")
    return result

def divide(a,b):
    try:
        result = a/b
        logger1.debug(f"dividing {a} / {b} = {result}")
    except ZeroDivisionError:
        logger1.error(f"divide by zero error")
        result = 0
    return result

add(5,4)
subtract(5,4)
multiply(5,4)
divide(8,4)
divide(8,0)