from models import Bike, Client, Partner, Bill

bikes = [
    Bike(id='B1', name="Adventure Pro", manufacturer="Trek", year="2002"),
    Bike(id='B2', name="Something", manufacturer="Trek", year="2002"),
    Bike(id='B3', name="Pro", manufacturer="Mercedes", year="2002"),
    Bike(id='B4', name="Mountain 3", manufacturer="Trek", year="2002"),
    Bike(id='B5', name="E-Bike", manufacturer="Trek", year="2002")
]

clients = [
    Client(id='C1', name='Client_1', email='client_1@email', address='street 1'),
    Client(id='C2', name='Client_2', email='client_2@email', address='street 2'),
    Client(id='C3', name='Client_3', email='client_3@email', address='street 3'),
    Client(id='C4', name='Client_4', email='client_4@email', address='street 4'),
    Client(id='C5', name='Client_5', email='client_5@email', address='street 5')
]

partners = [
    Partner(id='P1', name='Partner_1', email='Part_1@email', bike='B1'),
    Partner(id='P2', name='Partner_2', email='Part_2@email', bike='B2'),
    Partner(id='P3', name='Partner_3', email='Part_3@email', bike='B3'),
    Partner(id='P4', name='Partner_4', email='Part_4@email', bike='B4'),
    Partner(id='P5', name='Partner_5', email='Part_5@email', bike='B5')
]

bills = [
    Bill(status='Pending',client=clients[0].id, partner=partners[1].id, bill_strategy='KM', total_price=100)
]
#bikes[0].json()