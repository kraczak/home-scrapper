import asyncio
from pprint import pprint
from typing import List

from common.constants import forbidden_places
from common.home_model import Home
from common.params_manager import ParamsManager
from olx.manager import OlxManager


def filter_places(home_list: List[Home], places_to_filter):
    filtered_result = []
    for home in home_list:
        if home and home.not_in(places_to_filter):
            if home.turned_key_finished() and home.built(after=2000, before=2022) and home.secondary_market():
                filtered_result.append(home)
    return filtered_result


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()

    params = ParamsManager(
        area=(30, 60),
        price=(280_000, 650_000),
        build_year=(2000, 2021),
        max_price_per_meter=13000,
        rooms_num=(2, 3)
    )

    for params in [params.get_olx_params()]:
        result = asyncio.run(OlxManager(params, forbidden_places).process(2))
        filtered_homes = filter_places(result, forbidden_places)

        unique_homes = list(set(filtered_homes))
        print()
        pprint(sorted(unique_homes, key=lambda x: x.url))
        print()
        print()
