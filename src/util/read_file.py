import os

"""
class to read resources.
"""


class ReadFile:
    """
    get schema.
    """

    @staticmethod
    def get_file_validator(file_name):
        schema_path = os.path.abspath('test/features/resources/' + file_name)
        print("schema path: \n%s" % schema_path)
        file_schema = open(schema_path)
        schema = file_schema.read()
        file_schema.close()
        return schema
