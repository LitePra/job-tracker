from pydantic import BaseModel, ConfigDict, Field, StringConstraints
from typing_extensions import Annotated

NonBlankString = Annotated[str, StringConstraints(strip_whitespace=True,min_length=1)]

class JobSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True,extra='forbid')
    id: str
    title: NonBlankString
    stack: NonBlankString
    experience: int = 0
    apply: bool

class JobCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True,extra='forbid')
    title: NonBlankString
    stack: NonBlankString
    experience: int = 0
    apply: bool = False

class JobUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True,extra='forbid')
    title: NonBlankString | None = None
    stack: NonBlankString | None = None
    apply: bool | None = None