class MainViewController:
    def __init__(self, view, task_list_view_controller):
        self.main_view = view
        self.task_list_view_controller = task_list_view_controller
        
    def add_task(self):
        task_name = self.main_view.get_task_name_input()
        self.task_list_view_controller.add_task(task_name)
        self.main_view.clear_task_name_input()
