"""
Section imports.
"""
from src.util.ReadCfg import ReadCfg
import logging

"""
This class is to logs.
"""
class logger:

    #filename read from properties.
    def __init__(self):
        # set up logging to file - see previous section for more details
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%m-%d %H:%M',
                            filename=ReadCfg.get_value("log_path"))
        # define a Handler which writes INFO messages or higher to the sys.stderr
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        # set a format which is simpler for console use
        formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
        # tell the handler to use this format
        console.setFormatter(formatter)
        # add the handler to the root logger
        logging.getLogger('').addHandler(console)

    """Return a message type debug.
    @msg receive a text.
    """
    @staticmethod
    def debug(msg):
        logging.debug(msg)

    """Return a message type error.
    @msg receive a text.
    """
    @staticmethod
    def error(msg):
        logging.error(msg)

    """Return a message type info.
    :msg receive a text.
    """
    @staticmethod
    def info(msg):
        logging.info(msg)

    """Return a message type warning.
    :msg receive a text.
    """
    @staticmethod
    def warning(msg):
        logging.warning(msg)

    """Return a message type critical.
    :msg receive a text.
    """
    @staticmethod
    def critical(msg):
        logging.critical(msg)
