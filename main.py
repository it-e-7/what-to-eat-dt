import typing
import logging

from services import KaKaoApiRequestFetcher

if __name__ == '__main__':
    kakao_fetcher = KaKaoApiRequestFetcher()
    kakao_fetcher.fetch_datas()