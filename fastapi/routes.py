from controller import BikeController, ClientController, PartnerController, BillController

from models import Bike, Client, Partner, Bill
from fastapi import APIRouter


bike_routes = APIRouter()

bike_controller = BikeController()
client_controller = ClientController()
partner_controller = PartnerController()
bill_controller = BillController()


@bike_routes.get('/bikes')
def get_bikes():
    return bike_controller.list_bikes()


@bike_routes.get('/bikes/by_manufacturer')
def get_bikes_by_manufacturer(manufacturer: str):
    return bike_controller.list_bikes_by_manufacturer(manufacturer)


@bike_routes.post('/bikes')
def post_bike(bike: Bike):
    bike_controller.add_bike(bike)


@bike_routes.delete('/bikes/{id_}')
def delete_bike(id_: str):
    bike_controller.remove_bike(id_)


@bike_routes.get('/clients')
def get_clients():
    return client_controller.list_clients()


@bike_routes.get('/clients/by_id')
def get_client_by_id(id_: str):
    return client_controller.list_client_by_id(id_)


@bike_routes.post('/clients')
def post_clients(client: Client):
    client_controller.add_client(client)


@bike_routes.delete('/clients/{id_}')
def delete_client(id_: str):
    client_controller.remove_client(id_)


@bike_routes.get('/partners')
def get_partners():
    return partner_controller.list_partners()


@bike_routes.get('/partners/by_id')
def get_partner_by_id(id_: str):
    return partner_controller.list_partner_by_id(id_)


@bike_routes.post('/partners')
def post_partners(partner: Partner):
    partner_controller.add_partner(partner)


@bike_routes.delete('/partners/{id_}')
def delete_partner(id_: str):
    partner_controller.remove_partner(id_)


@bike_routes.post('/bills')
def post_bills(bill: Bill):
    bill_controller.add_bill(bill)
