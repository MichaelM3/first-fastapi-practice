from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel
from uuid import UUID, uuid4

T = TypeVar("T")

class UserSchema(BaseModel):
    id: Optional[UUID] = uuid4()
    username: str
    email: str
     
