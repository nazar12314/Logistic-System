from location import Location
from typing import List
from itertools import count
from location import Location
import random


class Order:

    id_generator = count()

    def __init__(self, user_name, city, postoffice, items: List):
        self.user_name = user_name
        self.location = Location(city, postoffice)
        self.postoffice = postoffice
        self.vehicle = None
        self.orderId = next(self.id_generator)

    def calculateAmount(self):
        order_sum = 0
        for item in self.items:
            order_sum += item.price
        return order_sum

    def assignVehicle(self, vehicle):
        if vehicle.isAvailable:
            self.vehicle = vehicle
            vehicle.isAvailable = False

    @staticmethod
    def set_id():
        return random.randint(1, 10000000)


    def __str__(self):
        return f"Your order number is {self.orderId}"
