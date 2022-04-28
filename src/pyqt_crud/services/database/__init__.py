from typing import Text

import sqlite3


def connect(database: Text):
    return sqlite3.connect(database=database)
