import os

from models import Bike, Client, Partner, Bill
import pickle

#clients = []

partners = []

bills = []

def load_bikes():
    try:
        with open('bikes.pickle', 'rb') as file:
             bikes_loaded = pickle.load(file)
        return bikes_loaded
    except FileNotFoundError:
        bike = []
        store_bikes(bike)
        return bike

def store_bikes(bike):
    with open('bikes.pickle', 'wb') as file:
        pickle.dump(bike, file)

load_bikes()

def load_clients():
    try:
        with open('clients.pickle', 'rb') as file:
             clients_loaded = pickle.load(file)
        return clients_loaded
    except FileNotFoundError:
        client = []
        store_clients(client)
        return client

def store_clients(client):
    with open('clients.pickle', 'wb') as file:
        pickle.dump(client, file)

load_clients()
