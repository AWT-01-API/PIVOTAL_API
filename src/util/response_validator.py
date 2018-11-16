import jsonschema
import simplejson as json
from src.util.read_file import ReadFle

"""
class with validation methods.
"""
class ResponseValidator:

    """
    validation json schema.
    :param validation_file name of the schema to use.
    :param validation_obj object to validate.
    """
    @staticmethod
    def validate_schema(validation_file, validation_obj):
        schema_data = ReadFle.get_file_validator(validation_file)
        schema = json.loads(schema_data)
        # this line do the validation.
        jsonschema.validate(validation_obj.json(), schema)

    """
    validation of the status code.
    :param response to get status_code.
    """
    @staticmethod
    def validate_status_code(response):
        assert response.status_code is 200


