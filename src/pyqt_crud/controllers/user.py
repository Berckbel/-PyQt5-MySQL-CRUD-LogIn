#!/usr/bin/env python3

from typing import Optional, Text
from ..models.user import User, fetch, create_table
from ..services.database import connect


class UserController:
    connection = None

    def __init__(self, database: Text):
        self.connection = connect(database)
        create_table(self.connection)

    def fetch(self, username: Text, password: Text) -> Optional[User]:
        return fetch(username, password, self.connection)
