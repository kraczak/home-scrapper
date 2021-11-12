import asyncio
from abc import abstractmethod, ABC
from typing import List, Tuple, Callable, Protocol, Set, AsyncGenerator
from urllib.parse import urlparse, urlencode, urlunparse

import aiohttp
from bs4 import BeautifulSoup

from common.home_model import Home
from common.search_params import ISearchParams


async def fetch_one(url: str, session: aiohttp.ClientSession) -> Tuple[str, bytes]:
    async with session.get(url) as response:
        return url, await response.read()


async def run(urls):
    tasks = []

    # Fetch all responses within one Client session,
    # keep connection alive for all requests.
    async with aiohttp.ClientSession() as session:
        for url in urls:
            task = asyncio.ensure_future(fetch_one(url, session))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)
        # you now have all response bodies in this variable
        return responses


async def download_all_pages(url_list: List[str]):
    """ downloads all hyperlinks to ads from all listing pages """
    for page_html in await run(url_list):
        yield page_html


class Filter(Protocol):
    def __call__(self, soup: BeautifulSoup) -> Set[int]: ...


class BaseServiceManager(ABC):

    def __init__(self, home_params: ISearchParams, filter_addresses: List[Callable] = None):
        self.home_params = home_params
        self.filter_addresses = filter_addresses or []

    @abstractmethod
    async def get_params(self):
        pass

    @property
    @abstractmethod
    def base_url(self):
        pass

    async def get_listing_pages(self, n: int):
        """ returns list of hyperlinks to first n listing pages """
        new_query = await self.get_params()
        page_param = 'page'
        url_parts = list(urlparse(self.base_url))
        result = []
        for i in range(n):
            new_query.update({page_param: i})
            url_parts[4] = urlencode(new_query)
            result.append(urlunparse(url_parts))
        return result

    async def download_listing_pages(self, n: int):
        """ downloads first n listings pages """
        for page_html in await run(await self.get_listing_pages(n)):
            yield page_html

    @abstractmethod
    async def get_href_from_listing_page(self, html: str) -> List[str]:
        """ parses listing page html and returns all ads hyperlinks from that page """
        pass

    async def get_all_hrefs(self, n: int) -> List[str]:
        """ returns all hyperlinks from all listing pages """
        result = []
        async for _, page in self.download_listing_pages(n):
            result.extend(await self.get_href_from_listing_page(page))
        return result

    @abstractmethod
    async def parse_home_ad_page(self, url: str, html: str) -> Home:
        """ parses html of a ad page and returns Home object """
        pass

    async def process(self, n):
        all_ads_url_list = []
        for ad_url in await self.get_all_hrefs(n):
            all_ads_url_list.append(ad_url)
        result = []
        async for page_url, page_html in download_all_pages(all_ads_url_list):
            if page_html is not None:
                result.append(await self.parse_home_ad_page(page_url, page_html))
            else:
                print(f'{page_url} could not be visited')
        return result
