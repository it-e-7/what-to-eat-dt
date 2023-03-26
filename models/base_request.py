import requests
import json
import logging
from pydantic import BaseModel
import time
from config import config
import logging

log = logging.getLogger(__name__)

class BaseRequest(BaseModel):
    sleeptime: float = config.DEFAULT_REQUEST_SLEEPTIME

    def request(self,url:str,method:str)->dict:
        time.sleep(self.sleeptime)

        try:
            res = None
            if method.lower() == "get":
                res = requests.get(url,headers=None)
            else:
                pass
            return {} if res is None else json.loads(res.content)
        except(
            requests.exceptions.Timeout,
            requests.exceptions.ConnectionError,
            requests.exceptions.HTTPError,
            requests.exceptions.RequestException
        ) as ex:
            log.warning(ex)
            return{}