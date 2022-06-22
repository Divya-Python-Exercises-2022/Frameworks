import db
from models import Bill

class BikeController:
    def list_bikes(self):
        return db.load_bikes()
        #return db.bikes

    def list_bikes_by_manufacturer(self, manufacturer):
        bikes = db.load_bikes()
        result = []
        for bike in bikes:
            if bike.manufacturer == manufacturer:
                result.append(bike)
        return result
    
    def add_bike(self, bike):
        current_list = db.load_bikes()
        current_list.append(bike)
        db.store_bikes(current_list)

    def remove_bike(self, id_: str):
        current_bikes = db.load_bikes()
        for bike in current_bikes:
            if bike.id == id_:
                current_bikes.remove(bike)
                db.store_bikes(current_bikes)

class ClientController:
    def list_clients(self):
        return db.load_clients()

    def add_client(self, client):
        current_list = db.load_clients()
        current_list.append(client)
        db.store_clients(current_list)

    def list_client_by_id(self, id_):
        result = []
        current_clients = db.load_clients()
        for client in current_clients:
            if client.id == id_:
                result.append(client)
        return result


    def remove_client(self, id_: str):
        current_clients = db.load_clients()
        for client in current_clients:
            if client.id == id_:
                current_clients.remove(client)
                db.store_clients(current_clients)


class PartnerController:
    def list_partners(self):
        return db.partners

    def add_partner(self, partner):
        db.partners.append(partner)

    def list_partner_by_id(self, id_):
        result = []
        for partner in db.partners:
            if partner.id == id_:
                result.append(partner)
        return result

    def remove_partner(self, id_: str):
        for partner in db.partners:
            if partner.id == id_:
                db.partners.remove(partner)

class BillController:
    def __init__(self, client_controller, partner_controller):
         self.client_controller =  client_controller
         self.partner_controller = partner_controller

    def add_bill(self, bill):
        db.bills.append(bill)

    def list_bill_by_client_id(self, client_id):
        result = []
        for bills in db.bills:
            if bills.client == client_id:
                result.append(bills)
        return result