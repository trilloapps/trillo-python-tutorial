import logging
import sys

log = logging.getLogger('')
log.setLevel(logging.INFO)
formatter = logging.Formatter("%(levelname)s - %(message)s")

ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(formatter)
log.addHandler(ch)




class Log:

    @staticmethod
    def info(message):
        log.info(message)

    @staticmethod
    def error(message):
        log.error(message)

    @staticmethod
    def warn(message):
        log.warning(message)
