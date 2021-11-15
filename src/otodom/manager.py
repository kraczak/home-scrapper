from typing import Optional, List
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from common.home_model import Home
from common.service_manager_interface import BaseServiceManager


class OtoDomManager(BaseServiceManager):
    base_url = "https://www.otodom.pl/pl/oferty/sprzedaz/mieszkanie/wroclaw"

    async def get_href_from_listing_page(self, html: str) -> List[str]:
        soup = BeautifulSoup(html, 'lxml')
        data = soup.find_all('a', href=True, attrs={'data-cy': 'listing-item-link'})
        # addresses = [a.text for a in soup.find_all('span', attrs={'class': 'css-17o293g es62z2j22'})]
        # data = [d for i, d in enumerate(data) if not any(a for a.lower() in self.filter_addresses if a in addresses[i])]
        return [urljoin(self.base_url, item['href']) for item in data]

    async def parse_home_ad_page(self, url: str, html: str) -> Optional[Home]:
        soup = BeautifulSoup(html, 'lxml')
        try:
            title = soup.find_all('h1', attrs={'data-cy': 'adPageAdTitle'})[0].text
            description = soup.find_all('div', attrs={'data-cy': 'adPageAdDescription'})[0].text
            address = soup.find_all('a', attrs={'aria-label': 'Adres'})[0].text
            price = soup.find_all('strong', attrs={'aria-label': 'Cena'})[0].text
            area = self.find_all_or_none(soup, 'div', attrs={'aria-label': 'Powierzchnia'})
            building_year = self.find_all_or_none(soup, 'div', attrs={'aria-label': 'Rok budowy'})
            room_no = self.find_all_or_none(soup, 'div', attrs={'aria-label': 'Liczba pokoi'})
            floor = self.find_all_or_none(soup, 'div', attrs={'aria-label': 'Piętro'})
            rent = self.find_all_or_none(soup, 'div', attrs={'aria-label': 'Czynsz'})
            state = self.find_all_or_none(soup, 'div', attrs={'aria-label': 'Stan wykończenia'})
            balcony = self.find_all_or_none(soup, 'div', attrs={'aria-label': 'Balkon / ogród / taras'})
            parking_space = self.find_all_or_none(soup, 'div', attrs={'aria-label': 'Miejsce parkingowe'})
            heating = self.find_all_or_none(soup, 'div', attrs={'aria-label': 'Ogrzewanie'})
            market = self.find_all_or_none(soup, 'div', attrs={'aria-label': 'Rynek'})

            return Home(
                url=f'{url}#map',
                title=title,
                description=description,
                price=price,
                address=address, area=area, building_year=int(building_year),
                rooms=room_no, balcony=balcony, market=market,
                heating=heating, floor=floor, state=state,
                rent=rent, parking_space=parking_space
            )
        except:
            print(f'Could not parse {url}')
            return None

    @staticmethod
    def find_all_or_none(soup, name, attrs):
        try:
            return soup.find_all(name, attrs=attrs)[0].text.split(':')[1]
        except IndexError:
            return None
