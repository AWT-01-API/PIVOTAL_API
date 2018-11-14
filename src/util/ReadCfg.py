import ConfigParser
import os


class ReadCfg:

    @staticmethod
    def get_value(attribute):
        prop = os.getcwd().replace("\\", "/")
        prop = prop.split("src")[0] + '/config.ini'
        parser = ConfigParser.RawConfigParser(allow_no_value=True)
        parser.read(prop)
        return parser.get("Pivotal", attribute)


