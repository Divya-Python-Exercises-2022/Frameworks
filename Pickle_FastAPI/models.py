import datetime
from pydantic import BaseModel


class Bike(BaseModel):
    id: str
    name: str
    manufacturer: str
    year: str

class Person(BaseModel):
    id: str
    name: str
    email: str

class Client(Person):
    address: str

class Partner(Person):
    bike: str

class Bill(BaseModel):
    status: str = 'Pending'
    client: str
    partner: str
    bill_strategy: str
    total_price: int = 0
