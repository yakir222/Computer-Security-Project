import server.dal.customer as customer
import server.services.db_services as db_services

def get_customer(_id: int = None) -> customer.Customer:
    rv = None
    if _id is not None:
        rv = db_services.get_customer_by_id(_id)
    if rv is None:
        raise RuntimeError("An error occurred")
    c_model = customer.Customer(**rv)
    return c_model

def get_customers(name: str = None) -> customer.Customer:
    rv = None
    if name is not None:
        rv = db_services.get_customers_by_name(name)

    if rv is None:
        raise RuntimeError("An error occurred")
    c_model = [customer.Customer(**cust) for cust in rv]
    return c_model

def add_customer(_customer: customer.Customer) -> customer.Customer:
    print(f"Adding customer: {_customer}")
    db_services.create_customer(_customer)
    return db_services.get_customer_by_id(_customer.id)
