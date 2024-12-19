import unittest
from types import SimpleNamespace
from app.helpers.object_to_sql import ObjectToSQLTransformer


class TestObjectToSQLTransformer(unittest.TestCase):
    def test_returns_list_of_queries(self):
        #Given
        obj = SimpleNamespace(name="Alice", age=30, is_active=True)

        # When
        queries = ObjectToSQLTransformer.object_to_sql(obj)

        #Then
        self.assertIsInstance(queries, list)

        for query in queries:
            self.assertIsInstance(query, str)


if __name__ == "__main__":
    unittest.main()
