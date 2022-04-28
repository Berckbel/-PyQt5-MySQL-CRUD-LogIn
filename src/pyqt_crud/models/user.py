#!/usr/bin/env python3


from dataclasses import dataclass
from typing import Text


@dataclass
class User:
    username: Text
    password: Text
