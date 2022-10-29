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