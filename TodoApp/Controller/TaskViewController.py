class TaskViewController:
    def __init__(self, view, delete_callback):
        self._view = view
        self._delete_callback = delete_callback
        
    def delete_task(self):
        self._delete_callback(self.view)
