import logging
import sys

logging.basicConfig(stream=sys.stdout, format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)

appLogger = logging
