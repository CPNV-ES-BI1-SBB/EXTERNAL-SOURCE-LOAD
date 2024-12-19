import unittest

from app.helpers.json_to_object import JsonToObjectTransformer


class TestJsonToObjectTransformer(unittest.TestCase):
    def test_simple_json(self):
        # Given
        json_data = '{"name": "Alice", "age": 30, "is_employee": true}'

        # When
        obj = JsonToObjectTransformer.json_to_object(json_data)

        # Then
        self.assertEqual(obj.name, "Alice")
        self.assertEqual(obj.age, 30)
        self.assertEqual(obj.is_employee, True)

    def test_nested_json(self):
        # Given
        json_data = '{"user": {"name": "Bob", "age": 25}, "status": "active"}'

        # When
        obj = JsonToObjectTransformer.json_to_object(json_data)

        # Then
        self.assertEqual(obj.user.name, "Bob")
        self.assertEqual(obj.user.age, 25)
        self.assertEqual(obj.status, "active")

    def test_json_with_list(self):
        # Given
        json_data = '{"names": ["Alice", "Bob", "Charlie"], "active": true}'

        # When
        obj = JsonToObjectTransformer.json_to_object(json_data)

        # Then
        self.assertEqual(obj.names, ["Alice", "Bob", "Charlie"])
        self.assertEqual(obj.active, True)

    def test_nested_list(self):
        # Given
        json_data = '{"groups": [{"id": 1, "name": "Admins"}, {"id": 2, "name": "Users"}]}'

        # When
        obj = JsonToObjectTransformer.json_to_object(json_data)

        # Then
        self.assertEqual(len(obj.groups), 2)
        self.assertEqual(obj.groups[0].id, 1)
        self.assertEqual(obj.groups[0].name, "Admins")
        self.assertEqual(obj.groups[1].id, 2)
        self.assertEqual(obj.groups[1].name, "Users")


if __name__ == "__main__":
    unittest.main()
