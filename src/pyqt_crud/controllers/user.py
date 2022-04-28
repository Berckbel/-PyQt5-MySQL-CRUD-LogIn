#!/usr/bin/env python3

from typing import Optional, Text
from ..models.user import User
from ..services.database.user import create_table, insert, fetch


class UserController:
    connection = None

    def __init__(self, connection):
        self.connection = connection
        create_table(self.connection)

    def register(self, user: User) -> User:
        return insert(user, self.connection)

    def fetch(self, username: Text, password: Text) -> Optional[User]:
        return fetch(username, password, self.connection)
