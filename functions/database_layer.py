import psycopg2
from psycopg2.extras import RealDictCursor


class Database:
    def __init__(self):
        try:
            # TODO: Save credentials into AWS
            connection = psycopg2.connect(user="postgres",
                                          password="iamkazm98",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="socialmedia",
                                          cursor_factory=RealDictCursor)

            self.connection = connection

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def save_user(self, user):
        query = f"insert into user_table (uuid, first_name, last_name, email, password, profile_picture) VALUES ('{user.uuid}', '{user.first_name}', '{user.last_name}', '{user.email}', '{user.password}', '{user.profile_picture}') returning id"

        connection = self.connection

        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()

        result = cursor.fetchall()[0]['id']

        cursor.close()
        connection.close()

        return result

    def get_one(self, param, value):
        query = f"select * from user_table where {param} = '{value}'"

        connection = self.connection

        cursor = connection.cursor()
        cursor.execute(query)

        result = cursor.fetchall()

        cursor.close()
        connection.close()

        return result


