from dataclasses import dataclass
from enum import Enum
from typing import Tuple

from common.search_params import ISearchParams


class Params(Enum):
    area: 'Params' = 'area'
    build_year: 'Params' = 'buildYear'
    price: 'Params' = 'price'


def param_range(prefix: Params, min_max: Tuple[int, int]):
    if min_max is None:
        return {}
    return {
        f'{prefix.value}Min': str(min_max[0]),
        f'{prefix.value}Max': str(min_max[1])
    }


const_params = {
    'by': 'DEFAULT',
    'direction': 'DESC',
    'distanceRadius': '0',
    'extras': '[BALCONY]',
    'limit': '100',
    'locations': '[cities_6-39]',
    'market': 'ALL',
}


@dataclass
class OtoDomParams(ISearchParams):

    def get_params(self):
        return {
            **const_params,
            **param_range(Params.area, self.area),
            **param_range(Params.build_year, self.build_year),
            **param_range(Params.price, self.price),
            'pricePerMeterMax': self.max_price_per_meter,
            'roomsNumber': self.get_rooms_number()
        }

    def get_rooms_number(self):
        result = []
        if 2 in self.rooms_num:
            result += ['TWO']
        if 3 in self.rooms_num:
            result += ['THREE']
        if 4 in self.rooms_num:
            result += ['FOUR']
        return str(result).replace('\'', '')
