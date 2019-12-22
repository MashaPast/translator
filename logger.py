import logging

logging.basicConfig(format="%(asctime)s module '%(module)s' function '%(funcName)s' %(levelname)s -> %(message)s",
                    level=logging.DEBUG)

appLogger = logging
