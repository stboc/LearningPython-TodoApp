import TodoApp.Model.DataBaseHandler as db
import TodoApp.View.TaskView as tv
import TodoApp.Controller.TaskViewController as tvc

class TaskListViewController:
    def __init__(self, view, db_handler:db.DataBaseHandler):
        self.view = view
        self.db_handler = db_handler
        
        loaded_tasks = db_handler.load_tasks()
        self._task_view_list = []
        for loaded_task in loaded_tasks:
            self.add_task(loaded_task[0], loaded_task[1], False)
        
    def add_task(self, task_name, is_resolved=False, is_saved=True):
        if is_saved:
            self.db_handler.add_task(task_name, is_resolved)
        task_view = tv.TaskView(self.view, task_name, is_resolved)
        task_view_controller = tvc.TaskViewController(task_view, self.delete_task)
        task_view.controller = task_view_controller
        self.view.append_task(task_view)
        self._task_view_list.append(task_view)
    
    def delete_task(self, task_view:tv.TaskView):
        self.db_handler.delete_task(task_view.task_name)
        self._task_view_list.remove(task_view)
    
    def _delete_task_callback(self, task_view:tv.TaskView):
        self.view.delete_task(task_view)
