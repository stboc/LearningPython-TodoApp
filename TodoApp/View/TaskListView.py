import tkinter as tk
import TodoApp.View.TaskView as task

class TaskListView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bd=1, relief="solid")
        self._task_view_list = []
        
    def add_task(self, task_name):
        task_view = task.TaskView(self, task_name, self._delete_task)
        task_view.pack(fill="x", padx=5)
        self._task_view_list.append(task_view)
    
    def _delete_task(self, task_view):
        task_view.destroy()
        self._task_view_list.remove(task_view)
        
