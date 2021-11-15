from dataclasses import dataclass
from typing import Tuple, Optional

from olx.params import OlxParams
from otodom.params import OtoDomParams


@dataclass
class ParamsManager:
    area: Tuple[int, int]
    price: Tuple[int, int]
    max_price_per_meter: int
    rooms_num: Tuple[int, int]
    build_year: Optional[Tuple[int, int]] = None

    def get_olx_params(self):
        return OlxParams(**self.__dict__).get_params()

    def get_otodom_params(self):
        return OtoDomParams(**self.__dict__).get_params()

