import re
from typing import Optional, List
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from common.home_model import Home
from common.service_manager_interface import BaseServiceManager
from common.utils import any_a_in_any_b


class MorizonManager(BaseServiceManager):
    base_url = 'https://www.morizon.pl/mieszkania/wroclaw/'



    async def get_href_from_listing_page(self, html: str) -> List[str]:
        soup = BeautifulSoup(html, 'lxml')

        offers = soup.find_all('tr', attrs={'class': 'wrap'})
        hrefs = []
        for offer in offers:
            rel = offer.get('rel', None)
            if rel != 'external':
                offer_link = offer.find('a', href=True)['href']
                offer_address = ' '.join(offer.find('i', attrs={'data-icon': 'location-filled'}).next.split()[1:])
                if not any_a_in_any_b(self.filter_addresses, [offer_link, offer_address]):
                    hrefs.append(offer_link)
        return [urljoin(self.base_url, url) for url in hrefs]

    async def parse_home_ad_page(self, url: str, html: str) -> Optional[Home]:
        soup = BeautifulSoup(html, 'lxml')
        try:
            data = [t.text for t in soup.find_all('p', attrs={'class': re.compile('css-.*')})]

            def get_value_from_list(name: str, data: List[str]):
                for val in data:
                    match val.lower().split(': '):
                        case []:
                            return None
                        case [el] if name.lower() in el:
                            return el
                        case [el1, el2] if name.lower() in el1:
                            return el2
                return None

            source = get_value_from_list('Prywatne', data)
            m_price = get_value_from_list('Cena', data)
            floor = get_value_from_list('Poziom', data)
            state = get_value_from_list('Umeblowane', data)
            market = get_value_from_list('Rynek', data)
            building_type = get_value_from_list('Rodzaj zabudoway', data)
            area = get_value_from_list('Powierzchnia', data)
            room_no = get_value_from_list('Liczba Pokoi', data)

            title = soup.find_all('h1', attrs={'data-cy': 'ad_title'})[0].text
            description = soup.find_all('div', attrs={'class': 'css-g5mtbi-Text'})[0].text
            price = soup.find_all('h3', attrs={'class': 'css-okktvh-Text eu5v0x0'})[0].text
            #     area = self.find_all_or_none(soup, 'div', attrs={'aria-label': 'Powierzchnia'})
            #     building_year = self.find_all_or_none(soup, 'div', attrs={'aria-label': 'Rok budowy'})
            #     room_no = self.find_all_or_none(soup, 'div', attrs={'aria-label': 'Liczba pokoi'})
            #     floor = self.find_all_or_none(soup, 'div', attrs={'aria-label': 'Piętro'})
            #     rent = self.find_all_or_none(soup, 'div', attrs={'aria-label': 'Czynsz'})
            #     state = self.find_all_or_none(soup, 'div', attrs={'aria-label': 'Stan wykończenia'})
            #     balcony = self.find_all_or_none(soup, 'div', attrs={'aria-label': 'Balkon / ogród / taras'})
            #     parking_space = self.find_all_or_none(soup, 'div', attrs={'aria-label': 'Miejsce parkingowe'})
            #     heating = self.find_all_or_none(soup, 'div', attrs={'aria-label': 'Ogrzewanie'})
            #     market = self.find_all_or_none(soup, 'div', attrs={'aria-label': 'Rynek'})
            #
            home = Home(
                url=url,
                title=title,
                description=description,
                price=price,
                area=area,
                rooms=room_no, market=market,
                floor=floor, state=state
            )
            return home
        except Exception as err:
            print(err)
            print(f"Could not parse {url}")
            return None

    @staticmethod
    def find_all_or_none(soup, name, attrs):
        try:
            return soup.find_all(name, attrs=attrs)[0].text.split(':')[1]
        except IndexError:
            return None
