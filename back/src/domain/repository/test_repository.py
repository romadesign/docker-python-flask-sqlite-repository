from src.domain.model.test import Test
from src.lib.sqlite_based_repository import SqliteBasedRepository


class TestRepository(SqliteBasedRepository):
    def get_all_tests(self):
        cursor = self._conn().cursor()
        cursor.execute(
            """SELECT * 
                FROM tests
            """
        )
        tests_records = cursor.fetchall()
        results = []
        for testrecord in tests_records:
            # print(dict(testrecord), flush=True)
            results.append(
                Test(
                    id=testrecord["id"],
                    nombre=testrecord["nombre"],
                )
            )
        return results
