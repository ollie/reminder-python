class Table:
    def config(self):
        self.load_lines()

    def load_lines(self):
        self.lines        = []
        self.longest_line = 0

        for event in self.events:
            line   = self.event_line(event)
            length = len(line)

            if length > self.longest_line:
                self.longest_line = length

            self.lines.append({ 'line': line, 'separators': event.separators })

    def event_line(self, event):
        line = '{date} | {name}'.format(date = event.localized_event_date(), name = event.name_with_kind())
        return line

    def draw(self):
        self.headline('Narozeniny, svátky, platby…')

        for line in self.lines:
            if line['separators']:
                self.separator()

            print(line['line'])

            if line['separators']:
                self.separator()

    def headline(self, text):
        print(text)
        self.separator()

    def separator(self):
        if not hasattr(self, 'separator_line'):
            self.separator_line = '-' * self.longest_line

        print(self.separator_line)
