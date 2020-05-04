import psycopg2


def connect_to_database():
    try:
        conn = psycopg2.connect(user="postgres", password="postgres", host="localhost", port="5436", database="postgres")
        return conn
    except (Exception, psycopg2.OperationalError) as e:
        raise SystemExit('Failed to connect to database.', e)


def create_table_books(conn):
    try:
        with conn:
            with conn.cursor() as cursor:
                table_books = '''CREATE TABLE books
                (KEY TEXT PRIMARY KEY,
                TITLE TEXT NOT NULL,
                FIRSTPUBLISH TEXT NOT NULL);'''
                cursor.execute(table_books)
                print("Table books successfully created")

    except(Exception, psycopg2.DatabaseError) as e:
        raise SystemExit('Error while creating books table', e)


def create_table_subjects(conn):
    try:
        with conn:
            with conn.cursor() as cursor:
                table_subjects = '''CREATE TABLE subjects
                (ID SERIAL PRIMARY KEY,
                SUBJECT TEXT NOT NULL,
                BOOK_KEY TEXT NOT NULL,
                FOREIGN KEY (book_key) REFERENCES books(key) ON DELETE CASCADE);'''
                cursor.execute(table_subjects)
                print("Table subjects successfully created")
    except(Exception, psycopg2.DatabaseError) as e:
        raise SystemExit('Error while creating subjects table', e)
