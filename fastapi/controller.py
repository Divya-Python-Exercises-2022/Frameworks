import db
from models import Bill

class BikeController:
    def list_bikes(self):
        return db.bikes

    def list_bikes_by_manufacturer(self, manufacturer):
        bikes = db.bikes
        result = []
        for bike in bikes:
            if bike.manufacturer == manufacturer:
                result.append(bike)
        return result
    
    def add_bike(self, bike):
        db.bikes.append(bike)
    
    def remove_bike(self, id_: str):
        for bike in db.bikes:
            if bike.id == id_:
                db.bikes.remove(bike)

class ClientController:
    def list_clients(self):
        return db.clients

    def add_client(self, client):
        db.clients.append(client)

    def list_client_by_id(self, id_):
        result = []
        for client in db.clients:
            if client.id == id_:
                result.append(client)
        return result


    def remove_client(self, id_: str):
        for client in db.clients:
            if client.id == id_:
                db.clients.remove(client)


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