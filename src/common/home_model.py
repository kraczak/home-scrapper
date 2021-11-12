from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional, List

import peewee

from common.utils import get_or_empty, any_a_in_any_b
from db.db_models import HomeDB


class FinishCondition(Enum):
    for_living = 'do zamieszkania'
    renovation = 'do remontu'
    refreshment = 'do odświeżenia'
    no_info = 'brak info'


class Heating(Enum):
    district = 'miejskie'


@dataclass
class Home:
    url: str
    title: str
    price: float
    area: float
    rooms: int
    insert_time: datetime = datetime.now()
    last_try_insert_time: datetime = datetime.now()
    address: str = None
    balcony: Optional[str] = None
    building_year: Optional[int] = None
    description: Optional[str] = None
    floor: Optional[int] = None
    building_type: Optional[str] = None
    elevator: Optional[str] = None
    state: Optional[FinishCondition] = None
    rent: Optional[float] = None
    parking_space: Optional[bool] = None
    heating: Optional[Heating] = None
    market: Optional[str] = None

    def __str__(self):
        return f'{self.address}, {self.price}, {self.area}, {self.state}, {self.url}, {self.insert_time}'

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.url == other.url or (self.address == other.address and self.price == other.price)

    def __hash__(self):
        return hash(self.address + str(self.price))

    def create(self):
        try:
            return HomeDB.insert(**self.__dict__) \
                .on_conflict(preserve=HomeDB.insert_time) \
                .execute()
        except peewee.IntegrityError as err:
            return None

    def address_search_list(self):
        return [get_or_empty(attr) for attr in [self.address, self.description, self.title]]

    def not_in(self, places: List[str]):
        return not any_a_in_any_b(places, self.address_search_list())

    def turned_key_finished(self):
        return self.state is None or self.state == "do zamieszkania"

    def built(self, after: int = None, before: int = None):
        result: bool = True
        if self.building_year is not None:
            if before is not None:
                result = self.building_year < before
            if after is not None:
                result = self.building_year >= after
        return result

    def secondary_market(self):
        return self.market is None or self.market == 'wtórny'


if __name__ == '__main__':
    a = Home(
        url='test',
        title='test',
        price=123.2,
        area=12311.5,
        rooms=5,
        address='wroclaw'
    )
