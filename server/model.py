from datetime import datetime, date
from pydantic import BaseModel, StrictStr


class ProfileModel(BaseModel):
    name: StrictStr
    company: StrictStr
    dob: date
    address: StrictStr
    location: dict
    about: StrictStr


class UserModel(BaseModel):
    id: StrictStr
    email: StrictStr
    username: StrictStr
    profile: ProfileModel
    apiKey: StrictStr
    roles: list[StrictStr]
    createdAt: datetime
    updatedAt: datetime
