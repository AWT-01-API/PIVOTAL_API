from src.util.logger import logger

class logger_handler:
    # Here will be the instance stored.
    __instance = None

    """
    :return instance.
    """
    @staticmethod
    def get_instance():
        """ Static access method. """
        if logger_handler.__instance is None:
            logger_handler.__instance = logger()
        return logger_handler.__instance
