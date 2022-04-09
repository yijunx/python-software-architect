from typing import Any

class Singleton(type):
    # it maintains all its instances here
    # in the _instances
    _instances= {}
    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwds)
        return cls._instances[cls]


class Logger(metaclass=Singleton):
    def log(self, msg):
        print(msg)

logger = Logger()
logger.log("hi")
logger2 = Logger()
logger.log("hi")

print(logger, logger2)  # they are one object!!!!!


# 1 breaks the OOP,
# 2 no control on creation, testing is really hard, cannot create new instance
# 3 bad on multithread