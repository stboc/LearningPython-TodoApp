from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from TodoApp.View.TaskView import TaskView

class TaskViewController:
    def __init__(self, view:'TaskView', delete_callback):
        self._view = view
        self._delete_callback = delete_callback
        
    def delete_task(self):
        self._delete_callback(self._view)
