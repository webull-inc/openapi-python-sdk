# coding=utf-8

from enum import Enum

class EasyEnum(Enum):
    def __str__(self):
        return self.name
    
    @classmethod
    def from_string(cls, s):
        for item in cls:
            if item.name == s:
                return item
        raise ValueError(cls.__name__ + ' has no value matching ' + s)