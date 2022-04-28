#!/usr/bin/env python3


from dataclasses import dataclass
from typing import Optional, Text


@dataclass
class User:
    username: Text
    password: Text


def create_table(connection):
    with connection.cursor() as cursor:
        query = """CREATE TABLE IF NOT EXISTS `user` (
            username VARCHAR(21) NOT NULL,
            password VARCHAR(24) NOT NULL
        )"""
        cursor.execute(query)
        connection.commit()


def fetch(username: Text, password: Text, connection) -> Optional[User]:
    with connection.cursor() as cursor:
        query = """SELECT username
        FROM `user`
        WHERE username = ? AND password = ?"""
        cursor.execute(query, (username, password))
        return cursor.fetchone()


def insert(user: User, connection) -> User:
    """Creates an user in the database

    Args:
        connection (IDb): db2 compliant connection.
        user (User): User information

    Returns:
        user (User): Created user
    """
    with connection.cursor() as cursor:
        query = """INSERT INTO `users` (username, password) VALUES (?, ?)"""
        res = cursor.insert(query, (user.username, user.password))
        print(res)
        connection.commit()
        return user
