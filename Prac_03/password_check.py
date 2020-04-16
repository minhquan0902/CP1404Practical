"""
CP1404/CP5632 - Practical
github link: https://github.com/minhquan0902/cp1404practicals/tree/master/Prac_03
"""

MIN_LENGTH = 1
MAX_LENGTH = 10

def main():
    password = get_password()
    len(password)
    while len(password) > MAX_LENGTH or len(password) < MIN_LENGTH:
        print("Your password must between 1-10")
        password = input()
    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_password():
    password = input("Enter your password between 1 character and 10 characters: ")
    return password

if __name__ == '__main__':
    main()