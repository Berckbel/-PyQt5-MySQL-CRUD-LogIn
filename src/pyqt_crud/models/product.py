#!/usr/bin/env python3


from typing import Text
from decimal import Decimal

from pydantic.dataclasses import dataclass


@dataclass
class Product:
    sku: Text
    name: Text
    price: Decimal
    category: Text
