import sqlite3

class DataBaseHandler:
    def __init__(self):
        self._connection = sqlite3.connect("todo_app.db")
        self._cursor = self._connection.cursor()
        self._added_task_id = 0
        self.creat_table()
    
    def creat_table(self):
        self._cursor.execute("CREATE TABLE IF NOT EXISTS task(name, is_resolved)")
        self._connection.commit()
    
    def add_task(self, task_name, is_resolved):
        self._cursor.execute("INSERT INTO task (name, is_resolved) VALUES (?, ?)", (task_name, is_resolved))
        self._connection.commit()
    
    def delete_task(self, task_name):
        self._cursor.execute("DELETE FROM task WHERE name = ?", (task_name,))
        self._connection.commit()
    
    def load_tasks(self):
        self._cursor.execute("SELECT name, is_resolved FROM task")
        return self._cursor.fetchall()
