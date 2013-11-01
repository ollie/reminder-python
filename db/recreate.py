import sqlite3
import os

import data

class Creator:
    def __init__(self):
        self.db_path = 'db/events.sqlite'

    def create(self):
        self.delete_db()
        self.create_db()
        self.create_table()
        self.insert_rows()

    def delete_db(self):
        if os.path.isfile(self.db_path):
            print('Removing %s' % self.db_path)
            os.remove(self.db_path)

    def create_db(self):
        self.db = sqlite3.connect(self.db_path)

    def create_table(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE "events" (
                "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                "show" boolean DEFAULT 1,
                "birthday" boolean,
                "nameday" boolean,
                "payment" boolean,
                "year" integer,
                "month" integer,
                "day" integer,
                "name" varchar(255)
            )
        ''')

    def insert_rows(self):
        cursor = self.db.cursor()
        print('Inserting events')

        insert_header = 'INSERT INTO "events" ("show", "birthday", "nameday", "payment", "year", "month", "day", "name") VALUES (:show, :birthday, :nameday, :payment, :year, :month, :day, :name)'
        insert_rows   = data.events()

        cursor.executemany(insert_header, insert_rows)
        self.db.commit()

if __name__ == '__main__':
    creator = Creator()
    creator.create()
