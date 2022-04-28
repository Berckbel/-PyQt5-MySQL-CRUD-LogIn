from typing import Optional, Text

from pyqt_crud.models.user import User
from ...adapters import user as adapter


def create_table(connection):
    cursor = connection.cursor()
    query = """CREATE TABLE IF NOT EXISTS `users` (
        username VARCHAR(21) NOT NULL,
        password VARCHAR(24) NOT NULL
    )"""
    cursor.execute(query)
    connection.commit()


def fetch(username: Text, password: Text, connection) -> Optional[User]:
    cursor = connection.cursor()
    query = """SELECT *
    FROM `users`
    WHERE username = ? AND password = ?"""
    cursor.execute(query, (username, password))
    response = cursor.fetchone()
    return adapter.internal_to_user(response)


def insert(user: User, connection) -> User:
    """Creates an user in the database

    Args:
        connection (IDb): db2 compliant connection.
        user (User): User information

    Returns:
        user (User): Created user
    """
    cursor = connection.cursor()
    query = """INSERT INTO `users` (username, password) VALUES (?, ?)"""
    res = cursor.execute(query, (user.username, user.password))
    connection.commit()
    return user
