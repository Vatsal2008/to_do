from db import get_connection
from datetime import date

def create_todo(task):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('INSERT INTO to_do(Task,Task_Date) VALUES(%s,%s)',
                   (task, date.today().strftime("%Y-%m-%d"),)
                   )

    connection.commit()
    connection.close()

def update_task_done(task_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("UPDATE to_do SET Is_Done = 1 WHERE Id = %s",
                   (task_id,)
       )

    affected = cursor.rowcount

    connection.commit()
    connection.close()

    return affected

def load_tasks():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM to_do")
    tasks = cursor.fetchall()

    return tasks

def delete_tasks(task_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM to_do WHERE Id = %s",
                   (task_id,)
    )

    affected = cursor.rowcount

    connection.commit()
    connection.close()

    return affected

def reset_auto_increment():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("ALTER TABLE to_do AUTO_INCREMENT = 1")
    conn.commit()
    conn.close()
