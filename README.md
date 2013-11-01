# Reminder
This is a simple Python 3 command-line application to display upcoming and past events like birthdays, namedays and payments. It looks two months ahead and one month back.

This isn't really an application, it's just a bunch of scripts to print out events. It doesn't let you do anything. Data manipulation is done via editing the `db/data.py` file and reloading the data from scratch (i.e. running `python3 db/recreate.py`).

If you have a Mac, it can be hooked into [GeekTool](http://itunes.apple.com/cz/app/geektool/id456877552?mt=12) and displayed on your desktop.

## Installation
    $ git clone git://github.com/ollie/reminder-python.git # Clone this repo
    $ cd reminder-python                                   # Get in
    $ cp db/data.py.example db/data.py                     # Prepare your data file
    # Edit your data file db/data.py
    $ python3 db/recreate.py                               # Load your data into database
    $ ./run.py                                             # Run the application
    $ python3 run.py                                       # Run the application alternatively

## Running the application
    $ cd path/to/reminder-python # You need to `cd` to the application directory so it finds the database file
    $ ./run.py
