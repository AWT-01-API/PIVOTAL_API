import ConfigParser
import os


class ReadCfg:

    @staticmethod
    def get_value(attribute):
        prop = os.getcwd().replace("\\", "/")
        prop = prop.split("PIVOTAL_API")[0] + 'PIVOTAL_API/config.ini'
        parser = ConfigParser.RawConfigParser(allow_no_value=True)
        parser.read(prop)
        return parser.get("Pivotal", attribute)


