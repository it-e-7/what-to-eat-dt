from pydantic import BaseModel

class Config(BaseModel):
    DEFAULT_REQUEST_SLEEPTIME = 1
    
    

config = Config()
