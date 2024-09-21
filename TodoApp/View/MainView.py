import tkinter as tk

class MainView(tk.Frame):
    def __init__(self, root, controller, task_list_view, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        root.geometry("300x400")
        
        self.pack()
        self.controller = controller
        self.task_list_view = task_list_view
        
        self._main_label = tk.Label(self, text="TodoApp")
        self._task_input_frame = tk.Frame(self)
        self._task_name_input = tk.Entry(self._task_input_frame, bd=1, relief="solid")
        self._task_name_input.bind("<Return>", self._input_task_enter)
        self._add_button = tk.Button(self._task_input_frame, text="New", command=self._new_button_command)
    
    def put_modules(self):
        self._main_label.pack()
        self.task_list_view.pack(fill="both", expand=True)
        self._task_name_input.pack(side="left")
        self._add_button.pack(side="right")
        self._task_input_frame.pack()
        
    def _new_button_command(self):
        self.controller.add_task()
        
    def get_task_name_input(self):
        return self._task_name_input.get()
    
    def clear_task_name_input(self):
        self._task_name_input.delete(0, tk.END)
        
    def _input_task_enter(self, event):
        self._new_button_command()
