from pydantic.dataclasses import dataclass
from typing import Text

from pydantic import validator


@dataclass
class User:
    username: Text
    password: Text

    @validator('username')
    def username_alnum(cls, value: Text):
        assert value.isalnum(), 'Username must be alphanumeric.'
        return value

    @validator('username')
    def username_size(cls, value: Text):
        assert len(value) >= 8, 'Username should have at least 8 characters'
        assert len(value) <= 24, 'Username should have maximum 24 characters'
        return value

    @validator('password')
    def password_size(cls, value: Text):
        assert len(value) >= 8, 'Password should have at least 8 characters'
        assert (
            len(value) <= 24
        ), 'Password should have maximum of 24 characters'
        return value
