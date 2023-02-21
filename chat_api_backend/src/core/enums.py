
import enum


class BaseClass(enum.Enum):

    @classmethod
    def choices(cls):
        return [(item.value, item.name) for item in cls]


class GenderTypes(BaseClass):
    MALE = 'Male'
    FEMALE = 'Female'
