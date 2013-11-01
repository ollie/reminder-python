import sqlite3
import datetime

from app.event import Event

class Events:
    def __init__(self):
        self.db = sqlite3.connect('db/events.sqlite')
        self.db.row_factory = sqlite3.Row

    def near_today(self):
        date = datetime.date.today()
        # date = datetime.date(2013, 11, 1)
        events = self.near_date(date)
        return events

    def near_date(self, date):
        months = []

        for delta_month in range(-1, 3):
            month = date.month + delta_month

            if month > 12:
                month -= 12
            elif month < 1:
                month += 12

            months.append(month)

        cursor = self.db.cursor()
        cursor.execute(
            '''
                SELECT *
                FROM "events"
                WHERE
                    "show" = 1
                    AND "month" IN ({months})
            '''.format(months=self.join(months))
        )

        events = []

        for row in cursor:
            event = Event.from_row(row)
            event.set_event_date(months, date)
            events.append(event)

        events.append(Event.today())
        events = sorted(events, key = lambda event: event.event_date, reverse = True)

        return events

    def join(self, a_list):
        joined = ', '.join([ str(i) for i in a_list ])
        return joined

