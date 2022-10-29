
from classes.Bill_class import Bill
from classes.PDF_Class import PDFReport
from datetime import datetime

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


def get_pdf(pdf, bill):
    live = True
    while live:
        try:
            pdf.generate(bill)
            live = False
        except:
            print("File: ", pdf.filename, " must be closed to save.")
            input("Press ENTER to re-run generation")


def main():
    today = datetime.today()
    house = Bill(300, "House Rent", 30)
    house.get_flatmates()
    bill_split(house.amount, house.flatmate_list, house.day_period)
    pdf_bill = PDFReport(f"generated_bill{today.year}-{today.month}-{today.day}-"
                         f"h{today.hour}-m{today.minute}.pdf")
    get_pdf(pdf_bill, house)


main()
