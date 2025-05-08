from enum import Enum
from typing import Optional


class CustomerType(Enum):
    INSTITUTION = "institution"
    INDIVIDUAL = "individual"

    @classmethod
    def of(cls, name: str) -> Optional['CustomerType']:
        for item in cls:
            if item.name == name:
                return item
        return None
