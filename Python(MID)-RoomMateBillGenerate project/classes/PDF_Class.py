from fpdf import FPDF
from datetime import date


class PDFReport:
    """
    Creates a pdf OBJ
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, bill):
        """
        Generates a PDF for given Bill
        :param flatmates:
        :param bill:
        :return:
        """
        n = len(bill.flatmate_list)
        today = date.today()
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        pdf.image("sources\\house.png", w=30, h=30)
        pdf.set_font(family='Helvetica', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', align='C', ln=1)

        pdf.set_font(family='Helvetica', size=7, )
        pdf.cell(w=0, h=10, txt='| Created ' + str(today.month) + '/' + str(today.day) + '/' + str(today.year), align='R', ln=1)

        pdf.set_text_color(255, 255, 255)
        pdf.set_fill_color(0, 0, 0)

        pdf.set_font(family='Helvetica', size=18, style='B')

        pdf.cell(w=300, h=40, txt=str(bill.name), ln=1, fill=True, )
        pdf.cell(w=10, h=10, ln=1)

        pdf.set_font(family='Helvetica', size=15, style='B')
        pdf.set_text_color(0, 0, 0)

        pdf.cell(w=60, h=20, txt='Period:', )
        pdf.cell(w=100, h=20, txt=str(bill.day_period) + " days",)
        pdf.cell(w=80, h=20, txt='Flatmates: ', )
        pdf.cell(w=100, h=20, txt=str(n), )

        pdf.set_text_color(255, 255, 255)

        pdf.cell(w=100, h=20, txt='Amount:', fill=True)
        pdf.cell(w=100, h=20, txt="$"+str(bill.amount),  ln=1, fill=True)

        pdf.set_text_color(255, 255, 255)
        pdf.set_text_color(0, 0, 0)

        for i in range(n):
            pdf.cell(w=10, h=10, ln=1)
            pdf.set_font(family='Helvetica', size=11, style='B')
            pdf.cell(w=90, h=25, txt='Name', border=1 )
            pdf.set_font(family='Helvetica', size=10)
            pdf.cell(w=90, h=25, txt=str(bill.flatmate_list[(n-1)-i][1]["obj"].name), ln=1, border=1)

            pdf.set_font(family='Helvetica', size=11, style='B')
            pdf.cell(w=90, h=25, txt='Active Days' , border=1)
            pdf.set_font(family='Helvetica', size=10)
            pdf.cell(w=90, h=25, txt=str(bill.flatmate_list[(n-1)-i][1]["obj"].days_in_house), ln=1 , border=1)

            pdf.set_font(family='Helvetica', size=11, style='B')
            pdf.cell(w=90, h=25, txt='In House %', border=1)
            pdf.set_font(family='Helvetica', size=10)
            pdf.cell(w=90, h=25, txt=str(round(bill.flatmate_list[(n-1)-i][1]["obj"].percent_lived(bill) * 100, 2)), border=1, ln=1)

            pdf.set_font(family='Helvetica', size=13, style='B')

            pdf.set_text_color(255, 255, 255)

            pdf.cell(w=90, h=25, txt='Total: ', fill=True)
            pdf.set_font(family='Helvetica', size=11)
            pdf.cell(w=90, h=25, txt="$"+str(bill.flatmate_list[(n-1)-i][1]["obj"].pay), ln=1, fill=True)

            pdf.set_text_color(0, 0, 0)
            live = True

            while live:
                try:
                    pdf.output("output\\" + self.filename)
                    input("Saved file at location: output\\" + self.filename +
                          "\n (ENTER to QUIT)")
                    live = False
                except:
                    input("Could not save file at location: output\\" + self.filename +
                          "\n Make sure file is closed if saved.\n (ENTER to Try again)")

