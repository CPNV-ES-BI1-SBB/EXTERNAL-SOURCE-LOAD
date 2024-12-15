from types import SimpleNamespace


class ObjectToSQLTransformer:
    @staticmethod
    def object_to_sql(obj):
        """
        Converts a Python object (SimpleNamespace or list) into SQL `INSERT` statements.
        Dynamically generates table names from the object structure.
        """
        queries = []

        def process_object(data, table_name=None, parent_id=None):
            if isinstance(data, SimpleNamespace):
                current_table = table_name or "top_level"

                # Process fields
                fields = []
                values = []
                child_data = []

                for key, value in data.__dict__.items():
                    if isinstance(value, SimpleNamespace) or isinstance(value, list):
                        child_data.append((key, value))
                    else:
                        fields.append(key)
                        values.append(value if not isinstance(value, str) else f"'{value}'")

                # Include parent_id if present
                if parent_id is not None:
                    fields.append("parent_id")
                    values.append(parent_id)

                # Generate query
                if fields:
                    query = f"INSERT INTO {current_table} ({', '.join(fields)}) VALUES ({', '.join(map(str, values))});"
                    queries.append(query)

                # Process nested structures
                for child_key, child_value in child_data:
                    child_table = f"{current_table}_{child_key}"
                    process_object(child_value, child_table, parent_id=f"(SELECT MAX(id) FROM {current_table})")

            elif isinstance(data, list):
                # Process each element in the list
                for item in data:
                    process_object(item, table_name=table_name)

        # Start processing the object
        process_object(obj)

        return queries
