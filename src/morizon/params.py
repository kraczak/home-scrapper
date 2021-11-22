from dataclasses import dataclass
from enum import Enum
from typing import Tuple

from common.search_params import ISearchParams


class Params(Enum):
    price: 'Params' = 'price'
    area: 'Params' = 'living_area'
    rooms: 'Params' = 'number_of_rooms'
    price_per_meter: 'Params' = 'price_m2'

    def template(self, _from: bool = False, _to: bool = False):
        if _from:
            return f'ps[{self.value}_from]'
        if _to:
            return f'ps[{self.value}_to]'
        return f'ps[{self.value}]'


def param_range(prefix: Params, min_max: Tuple[int, int]):
    if min_max is None:
        return {}
    return {
        f'ps[{prefix.value}_from]': f'{min_max[0]}',
        f'ps[{prefix.value}_to]': f'{min_max[1]}'
    }


@dataclass
class MorizonParams(ISearchParams):

    def get_params(self):
        return {
            **param_range(Params.area, self.area),
            **param_range(Params.price, self.price),
            Params.price_per_meter.template(_to=True): self.max_price_per_meter,
            **self.get_rooms_number()
        }

    def get_rooms_number(self):
        i = 0
        result = {}
        if 2 in self.rooms_num:
            result[f'{Params.rooms.template()}[{i}]'] = 'two'
            i += 1
        if 3 in self.rooms_num:
            result[f'{Params.rooms.template()}[{i}]'] = 'three'
            i += 1
        if 4 in self.rooms_num:
            result[f'{Params.rooms.template()}[{i}]'] = 'four'
            i += 1
        return result
