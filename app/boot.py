from app.event_controller import EventController

class App:
    def run(self):
        self.run_controller()

    def run_controller(self):
        controller = EventController()
        controller.list()
