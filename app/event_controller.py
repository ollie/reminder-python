from app.events import Events
from app.table  import Table

class EventController:
    def list(self):
        events = Events().near_today()

        table = Table()
        table.events = events
        table.config()
        table.draw()
