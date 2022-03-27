import logging  # root logger
from logger import logger

# logging levels
# 5 levels
# DEBUG, INFO, WARNING, ERROR, CRITICAL
# default is >= WARNING

# this will only be set once by the first one
# thus it is not a good idea
# we need different loggers
# logging.basicConfig(
#     level=logging.DEBUG,
#     # filename="test.log",  # write to a file
#     format="%(asctime)s:%(levelname)s:MSG-%(msg)s:PROCESS-%(process)s:THREAD-%(thread)s"
# )

# working with above root logger is not the best idea


def add(x, y):
    """add function"""
    # logging.debug("ADD")
    # using logger instead of logging.debug!!!
    logger.info("ADD")
    return x + y


def subtract(x, y):
    """subtract function"""
    # logging.debug("SUBTRACT")
    logger.debug("SUBTRACT")
    return x - y


def devide(x, y):
    """subtract function"""
    # logging.debug("DEVIDE")
    logger.debug("DEIVDE")
    return x / y


if __name__ == "__main__":
    print(add(4, 3))
    print(subtract(4, 3))
