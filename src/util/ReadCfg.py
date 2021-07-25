# import ConfigParser
import os
from configparser import ConfigParser


class ReadCfg:

    @staticmethod
    def get_value(attribute):
        project_path = os.getcwd().replace("\\", "/")
        print(project_path)
        prop = "%s/config.ini" % project_path

        try:
            parser = ConfigParser()
            parser.read(prop)
            return parser.get("Pivotal", attribute)
        except Exception:
            error = attribute + " not found on cfg.ini"
            raise Exception(error)
