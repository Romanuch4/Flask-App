
import psycopg2
from psycopg2 import Error

try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(user="postgres",
                                  password="phpMyAdmin",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="blogdb")

    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    # Выполнение SQL-запроса
    create_table_query = "drop table if exists entries; create table entries(id serial primary key not null, date timestamp with time zone not null default now(), title varchar(80) not null, content text not null);"
    cursor.execute(create_table_query)
    connection.commit()
    print("Таблица успешно создана в PostgreSQL")

    insert_query = "INSERT INTO entries(title, content) VALUES('My first blog entry', 'This is some great content by Roman Krentovskyi');"
    cursor.execute(insert_query)
    insert_query = "INSERT INTO entries(title, content) VALUES('Done this task', 'No description :-)');"
    cursor.execute(insert_query)
    connection.commit()
    print("1 запись успешно вставлена")

    # Получить результат
    cursor.execute("SELECT * from entries")
    record = cursor.fetchall()
    print("Результат", record)

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
