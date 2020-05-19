"""
Github link: https://github.com/minhquan0902/CP1404Practical
"""
from Prac_08.taxi import Taxi


def main():
    taxi = Taxi("Prius 1", 100)
    taxi.drive(40)
    print(taxi.__str__())
    print("Taxi's current fare: {}".format(taxi.get_fare()))
    taxi.start_fare()
    taxi.drive(100)
    print("Taxi detail - Name: {}, fuel: {}, price per km: {}".format(taxi.name, taxi.fuel, taxi.price_per_km))
    print("Taxi's current fare: {}".format(taxi.get_fare()))


main()
