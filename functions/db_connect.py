import psycopg2


# TODO: Save creditonals into AWS
def connect_db():
    try:
        connection = psycopg2.connect(user="kazm",
                                    password="kazm98",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="social_media")

        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print(connection.get_dsn_parameters(), "\n")
        
        # Print PostgreSQL version
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")
    
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
