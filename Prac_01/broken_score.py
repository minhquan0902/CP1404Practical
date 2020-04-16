"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score= float(input("Enter score:"))
    if score < 0 or score >100:
        print("Invalid score")
    elif 90< score <=100:
        print("Excellent")
    elif 0<= score <50:
        print("Pass")
    else:
        print("Bad")


if __name__ =='__main__':
    main()

