from enum import Enum


class Gender(Enum):

    MALE = 'MALE'
    FEMALE = 'FEMALE'
    OTHER = 'OTHER'

    @classmethod
    def choices(cls):
        return *((enum.name, enum.value) for enum in cls),
