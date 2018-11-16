import os

"""
class to read resources.
"""


class ReadFle:
    """
    get schema.
    """

    @staticmethod
    def get_file_validator(file_name):
        file_schema = open(os.path.abspath('features/resources/' + file_name))
        schema = file_schema.read()
        file_schema.close()
        return schema
