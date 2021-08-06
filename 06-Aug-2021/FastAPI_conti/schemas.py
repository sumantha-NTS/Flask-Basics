from pydantic import BaseModel

### post method as request body
class blog(BaseModel):
    title: str
    author: str