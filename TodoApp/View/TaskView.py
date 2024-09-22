import tkinter as tk

class TaskView(tk.Frame):
    def __init__(self, parent:tk.Frame, task_name:str, is_resolved:bool):
        super().__init__(parent)
        
        self.controller = None
        
        self.task_name = tk.Label(self, text=f"{task_name}")
        self.task_name.pack(side="left")
        
        self._delete_button = tk.Button(self, text="x", command=self._delete_button_command)
        self._delete_button.pack(side="right")

        self._is_resolved = is_resolved
        self._resolve_button = tk.Button(self, text="[ ]", command=self._resolve_button_command)
        self._resolve_button.pack(side="right")
        
    def _resolve_button_command(self):
        if self._is_resolved :
            self._is_resolved = False
            self._resolve_button.config(text="[ ]")
        else :
            self._is_resolved = True
            self._resolve_button.config(text="[/]")

    def _delete_button_command(self):
        self.controller.delete_task()
        