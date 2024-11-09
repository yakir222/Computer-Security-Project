from typing import List, Union
from fastapi import APIRouter, HTTPException
import server.dal.customer as customer
import server.services.customer_service as customer_service
# import server.services.customer_service as customer_service

class CustomerRouter(APIRouter):
    def __init__(self) -> None:
        super().__init__()
        self._init_router()

    def _init_router(self):
        self.add_api_route(path="", endpoint=self.add_customer, methods=["POST"], responses={"201":{"description":"OK", "model": customer.Customer}}, status_code=201)
        self.add_api_route(path="", endpoint=self.get_customer, methods=["GET"],  responses={"200":{"description":"OK", "model": customer.Customer}}, status_code=200)

    def add_customer(self, _customer: customer.Customer):
        try:
            customer = customer_service.add_customer(_customer)
            return customer
        except Exception as e:
            raise HTTPException(500, detail="Unable to create user!")

    def get_customer(self, name: str = None, id: int = None) -> Union[customer.Customer, List[customer.Customer]]:
        if id is not None:
            return customer_service.get_customer(_id=id)
        if name:
            return customer_service.get_customers(name)
