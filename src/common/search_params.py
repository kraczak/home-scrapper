from abc import ABC
from dataclasses import dataclass
from typing import Tuple, Optional


@dataclass
class ISearchParams(ABC):
    area: Tuple[int, int]
    price: Tuple[int, int]
    max_price_per_meter: int
    rooms_num: Tuple[int, int]
    build_year: Optional[Tuple[int, int]] = None

    def get_params(self):
        pass
