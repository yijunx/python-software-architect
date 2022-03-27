import logging

# advanced logging

logger = logging.getLogger(name=__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("test.log")
# file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(
    logging.Formatter(
        "%(levelname)s:%(name)s:%(asctime)s:%(levelname)s:MSG-%(msg)s:PROCESS-%(process)s:THREAD-%(thread)s"
    )
)
logger.addHandler(file_handler)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(
    logging.Formatter(
        "%(name)s:%(asctime)s:%(levelname)s:MSG-%(msg)s:PROCESS-%(process)s:THREAD-%(thread)s"
    )
)

logger.addHandler(stream_handler)