import TodoApp.Model.DataBaseHandler as db

class TaskListViewController:
    def __init__(self, view, db_handler):
        self.view = view
        self.db_handler = db_handler
        
    def add_task(self, task_name):
        self.view.add_task(task_name)
