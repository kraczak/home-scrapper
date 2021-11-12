from copy import copy
from datetime import datetime

from peewee import *

from db import db


class BaseModel(Model):
    """A base model that will use our Postgresql database"""

    class Meta:
        database = db


class HomeDB(BaseModel):
    id = PrimaryKeyField()
    url = CharField(unique=True)
    title = TextField()
    price = DoubleField()
    area = DoubleField()
    rooms = IntegerField()
    address = TextField()
    description = TextField(null=True)
    balcony = TextField(null=True)
    building_year = IntegerField(null=True)
    floor = IntegerField(null=True)
    building_type = TextField(null=True)
    state = TextField(null=True)
    rent = DoubleField(null=True)
    parking_space = TextField(null=True)
    heating = TextField(null=True)
    market = TextField(null=True)
    insert_time = DateField(default=datetime.now)
    last_try_insert_time = DateField(default=datetime.now)

    def __str__(self):
        return str(self.__dict__['__data__'])

    def to_dataclass(self) -> 'Home':
        from common.home_model import Home
        kwargs = copy(self.__dict__['__data__'])
        for key in ['id']:
            kwargs.pop(key)
        return Home(**kwargs)


def initialize_db():
    db.connect()
    db.create_tables([HomeDB], safe=True)
    db.close()


if __name__ == '__main__':
    initialize_db()
