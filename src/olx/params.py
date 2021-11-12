from dataclasses import dataclass
from enum import Enum
from typing import Tuple, Optional

from common.search_params import ISearchParams


class Params(Enum):
    price: 'Params' = 'filter_float_price'
    area: 'Params' = 'filter_float_m'
    rooms: 'Params' = 'filter_enum_rooms'
    price_per_meter: 'Params' = 'filter_float_price_per_m'


def param_range(prefix: Params, min_max: Tuple[int, int]):
    if min_max is None:
        return {}
    return {
        f'search[{prefix.value}:from]': f'[{min_max[0]}]',
        f'search[{prefix.value}:to]': f'[{min_max[1]}]'
    }


@dataclass
class OlxParams(ISearchParams):

    def get_params(self):
        return {
            **param_range(Params.area, self.area),
            **param_range(Params.price, self.price),
            Params.price_per_meter: self.max_price_per_meter,
            **self.get_rooms_number()
        }

    def get_rooms_number(self):
        i = 0
        result = {}
        if 2 in self.rooms_num:
            result[f'search[{Params.rooms}][{i}]'] = ['two']
            i += 1
        if 3 in self.rooms_num:
            result[f'search[{Params.rooms}][{i}]'] = ['three']
            i += 1
        if 4 in self.rooms_num:
            result[f'search[{Params.rooms}][{i}]'] = ['four']
            i += 1
        return result




