import json
from types import SimpleNamespace


class JsonToObjectTransformer:
    @staticmethod
    def json_to_object(json_data: str):
        """
        Convert JSON string into a Python object dynamically.
        Nested JSON objects are recursively converted into SimpleNamespace instances.
        :param json_data: The JSON string to be converted.
        """

        def recursive_convert(data):
            if isinstance(data, dict):

                return SimpleNamespace(**{k: recursive_convert(v) for k, v in data.items()})
            elif isinstance(data, list):

                return [recursive_convert(item) for item in data]
            else:

                return data


        parsed_data = json.loads(json_data)
        return recursive_convert(parsed_data)

