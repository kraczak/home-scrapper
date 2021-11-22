from typing import List, Dict, Any
from urllib.parse import urlparse, parse_qs


def get_or_empty(val):
    return val or ''


def fun(val, val2) -> bool:
    return False if val is None else val == val2


def any_a_in_any_b(place_list: List[str], list_of_strings_to_check: List[str]):
    return any((place in attr.lower()) for attr in list_of_strings_to_check for place in place_list)


def get_params_from_url(url) -> Dict[Any, list]:
    parsed_url = urlparse(url)
    params = parsed_url[4]
    return parse_qs(params)


if __name__ == '__main__':
    url = 'https://www.morizon.pl/mieszkania/wroclaw/?ps%5Bprice_from%5D=250000&ps%5Bprice_to%5D=600000&ps%5Bprice_m2_to%5D=12500&ps%5Bliving_area_from%5D=25&ps%5Bliving_area_to%5D=60&ps%5Bnumber_of_rooms_from%5D=2&ps%5Bnumber_of_rooms_to%5D=3&ps%5Bfloor_from%5D=1&ps%5Bfloor_to%5D=10&ps%5Bbuild_year_from%5D=2000&ps%5Bbuild_year_to%5D=2021&ps%5Bhas_balcony%5D=1'

    print(get_params_from_url(url))
