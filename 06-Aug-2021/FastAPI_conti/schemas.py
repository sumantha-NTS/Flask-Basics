from pydantic import BaseModel
from typing import Optional

### post method as request body
class blog(BaseModel):
    title: str
    author: str