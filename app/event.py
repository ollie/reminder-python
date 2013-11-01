import datetime

class Event:
    def from_row(row):
        event = Event()

        event.set_id(       row['id']       )
        event.set_show(     row['show']     )
        event.set_birthday( row['birthday'] )
        event.set_nameday(  row['nameday']  )
        event.set_payment(  row['payment']  )
        event.set_year(     row['year']     )
        event.set_month(    row['month']    )
        event.set_day(      row['day']      )
        event.set_name(     row['name']     )
        event.separators = False

        return event

    def today():
        event = Event()

        event.set_birthday( False  )
        event.set_nameday(  False  )
        event.set_payment(  False  )
        event.set_name(     'Dnes' )
        event.event_date = datetime.date.today()
        event.separators = True

        return event

    def set_id(self, value):
        self.id = value

    def set_show(self, value):
        self.show = self.boolean(value)

    def set_birthday(self, value):
        self.birthday = self.boolean(value)

    def set_nameday(self, value):
        self.nameday = self.boolean(value)

    def set_payment(self, value):
        self.payment = self.boolean(value)

    def set_year(self, value):
        self.year = value

    def set_month(self, value):
        self.month = value

    def set_day(self, value):
        self.day = value

    def set_name(self, value):
        self.name = value

    def boolean(self, value):
        if value:
            return True
        else:
            return False

    def localized_event_date(self):
        return self.event_date.strftime('%d. %m. %Y')

    def name_with_kind(self):
        name = self.name
        kind = self.kind()

        if self.kind():
            name = '{name} {kind}'.format(name=name, kind=kind)

        if self.birthday:
            years = datetime.date.today().year - self.year
            name  = '{name} ({years})'.format(name=name, years=years)

        return name

    def kind(self):
        if self.birthday:
            return 'narozeniny'
        elif self.nameday:
            return 'svátek'
        elif self.payment:
            return 'platba'

    # We need to set the event date for sorting. There is a problem though,
    # we cannot simply set the current year for all events.
    #
    # We locate current month in the range and split it in two parts.
    # We then take the event month and ask a few questions:
    #
    # If the month is in the left part and is higher than the current month,
    # it means we are looking at the end of the previous year and we have
    # to decrement the year by one.
    #
    # If, however, the month is in the right part and is lower than the current month,
    # we are looking at the start of the next year and we have to increment it by one.
    #
    #                  event -> vv      vv <- current month
    # Watch out for this: [ 10, 11, 12, 01, 02, 03, 04 ]
    # Or that:            [ 09, 10, 11, 12, 01, 02, 03 ]
    #                  current month -> ^^  ^^ <- event
    def set_event_date(self, months, date):
        event_year = date.year

        index_of_current_month = months.index(date.month)

        left_part  = months[:index_of_current_month + 1]
        right_part = months[index_of_current_month:]

        if self.month in right_part and self.month < date.month:
            event_year += 1
        elif self.month in left_part and self.month > date.month:
            event_year -= 1

        self.event_date = datetime.date(event_year, self.month, self.day)
