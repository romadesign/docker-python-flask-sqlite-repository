from src.domain.model.user import User
from src.lib.sqlite_based_repository import SqliteBasedRepository
from flask_jwt_extended import jwt_required, get_jwt_identity


class UserRepository(SqliteBasedRepository):
    def __init__(self, config, database=None, get_current_user_id=lambda: None):
        super().__init__(config, database)
        self.get_current_user_id = get_current_user_id

    @jwt_required()
    def get_current_user(self):
        current_identity = get_jwt_identity()
        cursor = self._conn().cursor()
        cursor.execute(
            "SELECT * FROM users where id = ?;", (current_identity,)
        )
        data = cursor.fetchone()

        if data is not None:
            return User(**data)    

    def get_by_username(self, username):
        cursor = self._conn().cursor()
        cursor.execute("SELECT * FROM users where username = ?;", (username,))

        data = cursor.fetchone()

        if data is not None:
            return User(**data)

    def get_user_by_username(self, username):
        cursor = self._conn().cursor()
        cursor.execute("""SELECT * FROM users WHERE username=?""", (username,))
        data = cursor.fetchone()
        if data is None:
            return None
        return User(**data)


    def get_user_by_id(self, id):
        cursor = self._conn().cursor()
        cursor.execute("SELECT * FROM users where id = ?;", (id,))
        data = cursor.fetchone()

        if data is not None:
            return User(**data)

    def get_all_users(self):
        cursor = self._conn().cursor()
        cursor.execute("""SELECT * FROM users """)
        usernames_records = cursor.fetchall()
        result = []
        for username_record in usernames_records:
            result.append(User(**username_record))
        return result

    def save_user(self, new_user):
        print(new_user)
        conn = self._conn()
        cursor = conn.cursor()
        cursor.execute(
            """INSERT or REPLACE INTO users 
                    ("id", "username", "name", "password", "user_rol", "phone_number", "e_mail", "address")
                        VALUES (:id, :username, :name, :password, :user_rol, :phone_number, :e_mail, :address)
            """,
            {
                "id": new_user.id,
                "username": new_user.username,
                "name": new_user.name,
                "password": new_user.password,
                "user_rol": new_user.user_rol,
                "phone_number": new_user.phone_number,
                "e_mail": new_user.e_mail,
                "address": new_user.address
            },
        )

        conn.commit()
  
   