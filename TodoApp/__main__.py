import tkinter as tk
import TodoApp.View.MainView as mv
import TodoApp.View.TaskListView as tlv
import TodoApp.Controller.MainViewController as mvc
import TodoApp.Controller.TaskListViewController as tlvc
import TodoApp.Model.DataBaseHandler as dbh

class App:
    def __init__(self):
        root = tk.Tk()
        self._root = root
        
        main_view = mv.MainView(root, None, None)
        main_view_controller = mvc.MainViewController(main_view, None)
        main_view.controller = main_view_controller
        task_list_view = tlv.TaskListView(main_view)
        main_view.task_list_view = task_list_view
        data_base_handler = dbh.DataBaseHandler()
        task_list_view_controller = tlvc.TaskListViewController(task_list_view, data_base_handler)
        main_view_controller.task_list_view_controller = task_list_view_controller

        self._main_view = main_view
        self._main_view_controller = main_view_controller
        self._task_list_view = task_list_view
        self._task_list_view_controller = task_list_view_controller
        self._data_base_handler = data_base_handler
        
    def run(self):
        self._main_view.put_modules()
        self._root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()
