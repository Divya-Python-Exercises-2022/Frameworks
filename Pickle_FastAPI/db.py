import os

from models import Bike, Client, Partner, Bill
import pickle

#bikes = []

clients = []

partners = []

bills = []

def load_bikes():
    # if os.path.isfile('bikes.pickle') is False:
    #     raise Exception('File not found')
    # with open('bikes.pickle', 'rb+') as f:
    #     bikes_loaded = pickle.load(f)
    # return bikes_loaded
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

bikes = load_bikes()