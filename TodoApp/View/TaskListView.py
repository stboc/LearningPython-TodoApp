import tkinter as tk

class TaskListView(tk.Frame):
    def __init__(self, parent:tk.Frame):
        super().__init__(parent, bd=1, relief="solid")
        
    def append_task(self, task_view):
        task_view.pack(fill="x", padx=5)
    
    def delete_task(self, task_view):
        task_view.destroy()
