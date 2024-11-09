from pydantic import BaseModel

class Customer(BaseModel):
    name: str
    id: int
    address: str
    animal: str
    feet_size: float
