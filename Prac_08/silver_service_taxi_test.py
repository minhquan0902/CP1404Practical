"""
Github link: https://github.com/minhquan0902/CP1404Practical
"""
from Prac_08.SilverServiceTaxi import SilverServiceTaxi


def main():
    my_silver_taxi = SilverServiceTaxi("Silver_Taxi_1", 100, 2)
    my_silver_taxi.drive(18)
    print("Taxi's current fare: ${}".format(my_silver_taxi.get_fare()))
    print(my_silver_taxi.__str__())


main()
