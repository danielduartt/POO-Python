class DatabaseConn:

    def __init__(self) -> None:
        self.__database = 'Postgres'
        self._conn = '//connection_string' #protected
        self.user = "Duarte"

    def get_database(self) -> None:
        print(self.__database)

    def _testing_connection(self) -> None:
        print("Connection Ok!")

class Repository(DatabaseConn):
    def __init__(self) -> None:
        super().__init__()

    def select(self) -> None:
        self._testing_connection()
        print("connecting to {}".format(self._conn))
        print("SELECT *FROM table")

'''
db = DatabaseConn()
print(db.user)
print(db._conn) #da no mesmo kkkkkkk, 0 '_' é apenas uma convenção, apesar de conseguir ser acessado pelos objs
'''

repo = Repository()
repo.select()

