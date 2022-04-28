#!/usr/bin/env python3
from typing import Text, Tuple

from pyqt_crud.models.user import User


def internal_to_user(internal: Tuple[Text, Text]):
    username, password = internal
    return User(username, password)
