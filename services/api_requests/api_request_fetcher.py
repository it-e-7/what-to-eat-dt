
from typing import List, Dict
from models import BaseRequest

class KaKaoApiRequestFetcher(BaseRequest):
    
    data_requests: List[Dict] | None = None

    def fetch_datas(self):
        self.data_requests = self.request(
            method='get', 
            url='https://place.map.kakao.com/main/v/27306859'
        )
        print(self.data_requests)