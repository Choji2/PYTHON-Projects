from operator import getitem


class Bill:
    """
    OBJ that contains information about a Bill: name, amount, and period.
    """

    def __init__(self, amount, name, day_period):
        self.flatmate_list = None
        self.amount = amount
        self.name = name
        self.day_period = day_period

    def get_flatmates(self):
        """
        This function creates the OBJs of flatmates dynamically for each bill.
        :return:
        """
        live = True
        iteration = 0
        flatmate_dic = {}

        while live:

            iteration += 1
            print("Please enter Flatmate")
            name = input("Name: ")
            good_input = True
            while good_input:
                try:
                    period = int(input("Period: "))
                    while period < 1 or period > self.day_period:
                        period = int(input("Period must be between 1 and " + str(self.day_period) + "\nPeriod: "))
                    good_input = False
                except:
                    print("Period must be a number.")

            flatmate_dic[iteration] = {
                "obj": Flatmates(name, period),
                "value": period}
            q = input("Add another Flatmate? (Enter=Yes, N=No)").lower()
            if q == 'n':
                live = False

        flatmate_sort = sorted(flatmate_dic.items(),
                               key=lambda x: getitem(x[1], 'value'))

        self.flatmate_list = flatmate_sort

    def print_flatmates(self):
        """
        Simple method tha prints the contents of each flatmate.
        :return:
        """
        print("______", self.name, "______\nBill Amount: $", self.amount, "\n***********")
        n = len(self.flatmate_list)
        for i in range(n):
            print("Name: ", self.flatmate_list[(n-1)-i][1]["obj"].name)
            print("Days in: ", self.flatmate_list[(n-1)-i][1]["obj"].days_in_house)
            print("Percentage in house/period: ", round(self.flatmate_list[(n-1)-i][1]["obj"].percent_lived(self) * 100, 2),
                  "%")
            print("Pay: $", self.flatmate_list[(n-1)-i][1]["obj"].pay, "\n*************")

class Flatmates:
    """
    OBJ to hold information about flatmate: name, days_in_house,and pay.
    """

    def __init__(self, name, days_in_house):
        self.pay = None
        self.name = name
        self.days_in_house = days_in_house
        print("****Flatmate Created")
        print("Name:", self.name, "\nPeriod: ", self.days_in_house, "\n")

    def percent_lived(self, bill):
        return round(self.days_in_house / bill.day_period, 2)

    def set_pay(self, pay):
        self.pay = pay


def bill_split(pay, flatmates, period):
    """
    This method splits the bill amount for each flatmate, per bill OBJ.
    :param pay:
    :param flatmates:
    :param period:
    :return:
    """
    n = len(flatmates)
    c = n - 1
    percent = round(flatmates[c][1]["value"] / period, 2)

    if percent == 1:
        percent = .90

    if n == 1:
        flatmates[c][1]["obj"].set_pay(round(pay, 2))
    else:
        match = 0
        for j in range(n):
            if flatmates[c][1]["value"] == flatmates[c - j][1]["value"]:
                match += 1

        if match == n:
            new_pay = pay / n

            for a in range(n):
                flatmates[a][1]["obj"].set_pay(round(new_pay, 2))

        elif match != n and match > 1:
            new_pay = pay / (n - percent)

            for k in range(match):
                flatmates[c - k][1]["obj"].set_pay(round(new_pay, 2))
            bill_split(pay - match * new_pay, flatmates[0:c - match + 1], period)
        else:
            new_pay = pay / (n - percent)

            flatmates[c][1]["obj"].set_pay(round(new_pay, 2))
            bill_split(pay - new_pay, flatmates[0:c], period)


house = Bill(300, "House", 30)
house.get_flatmates()
bill_split(house.amount, house.flatmate_list, house.day_period)
house.print_flatmates()
