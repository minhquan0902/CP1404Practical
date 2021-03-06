"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
Github Link: https://github.com/minhquan0902/CP1404Practical/tree/master/Prac_04
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_month = int(input("How many months? "))

    for month in range(1, number_of_month + 1):
        income = float(input("Enter income for month{:2}: ".format(month) ))
        incomes.append(income)
    income_report(number_of_month, incomes)




def income_report(number_of_month, incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_month + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))




main()