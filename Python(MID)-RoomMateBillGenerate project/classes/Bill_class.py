from operator import getitem
from classes.Flatmate_class import Flatmates

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
