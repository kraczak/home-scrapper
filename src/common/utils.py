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
    url = "https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/wroclaw/?search%5Bfilter_float_price%3Afrom%5D=200000&search%5Bfilter_float_price%3Ato%5D=700000&search%5Bfilter_float_price_per_m%3Afrom%5D=1&search%5Bfilter_float_price_per_m%3Ato%5D=20&search%5Bfilter_enum_market%5D%5B0%5D=primary&search%5Bfilter_enum_market%5D%5B1%5D=secondary&search%5Bfilter_float_m%3Afrom%5D=30&search%5Bfilter_float_m%3Ato%5D=50&search%5Bfilter_enum_rooms%5D%5B0%5D=two&search%5Bfilter_enum_rooms%5D%5B1%5D=three"
    url2 = 'https://www.olx.pl/nieruchomosci/wroclaw/?search%5Bfilter_float_m%3Afrom%5D=30&search%5Bfilter_float_m%3Ato%5D=70&search%5Bfilter_float_price%3Afrom%5D=280000&search%5Bfilter_float_price%3Ato%5D=700000&search%5Bfilter_float_price_per_m%3Ato%5D=13000&search%5Bfilter_enum_rooms%5D%5B0%5D=two&search%5Bfilter_enum_rooms%5D%5B1%5D=three&page=0'

    print(get_params_from_url(url))
    print(get_params_from_url(url2))
