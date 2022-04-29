#!/usr/bin/env python3

from typing import Optional, Text

from ..models.user import User
from ..services.database.user import create_table, fetch, insert


class UserController:
    connection = None

    def __init__(self, connection):
        self.connection = connection
        create_table(self.connection)

    def register(self, user: User) -> User:
        return insert(user, self.connection)

    def login(self, username: Text, password: Text) -> bool:
        user = None
        try:
            user = fetch(username, password, self.connection)
        except Exception as _:
            pass
        return user is not None
