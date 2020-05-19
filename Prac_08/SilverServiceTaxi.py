"""
Github link: https://github.com/minhquan0902/CP1404Practical
"""
from Prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * fanciness

    def __str__(self):
        return "{} plus flagfall of ${}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        # If distance > 0 then count the flag fall
        return round(super().get_fare() + self.flagfall if self.current_fare_distance != 0 else 0, 1)
