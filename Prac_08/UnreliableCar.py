"""
Github link: https://github.com/minhquan0902/CP1404Practical
"""
from Prac_06.car import Car

import random


class UnreliableCar(Car):
    price_per_km = 1.23

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string like a Car but with current fare distance."""
        return "{}, {}km on current fare, ${:.2f}/km".format(super().__str__(),
                                                             self.current_fare_distance,
                                                             self.price_per_km)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        distance_driven = super().drive(distance)
        if random.randint(1, 100) < self.reliability:
            self.current_fare_distance += distance_driven
        else:
            pass
        return distance_driven
