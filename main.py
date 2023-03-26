import typing
import logging

from services import KaKaoApiRequestFetcher

if __name__ == '__main__':
    pullRequestFetcher = KaKaoApiRequestFetcher()
    pullRequestFetcher.fetch_datas()