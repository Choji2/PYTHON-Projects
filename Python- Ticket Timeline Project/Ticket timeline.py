# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 16:31:21 2021

@author: vac59186
"""

from datetime import datetime
from datetime import date
from fpdf import FPDF
import getpass
import sys

now = datetime.now()
dte = now.strftime("%m-%d-%Y")

start = datetime.now()
user = getpass.getuser()


def generate_logs(now):
    curr = now.strftime("%m/%d/%Y %H:%M:%S:%f")
    log = {}
    count = 0
    live = True

    print('Enter # to stop and save the log. Press @ to stop and not save.')
    while live:

        entry = input('> ')

        if entry == '#' and count == 0:
            print('No data for log to be created and saved.')

        elif entry == '#':
            end = datetime.now()
            down = end - start
            #print_file(log, down)
            pdf = PDF()
            generate_pdf(log, down, pdf)

            live = False

        elif entry == '@':

            ext = input('Are you sure you want to quit without saving?(Y/N)')

            if ext == 'Y' or ext == 'y':
                print('No log file created.')
                sys.exit()

        else:
            count += 1
            now = datetime.now()
            curr = str(now.strftime("%m/%d/%Y %H:%M:%S:%f")[:-3])

            log[curr] = entry
            print(f'{now.strftime("%m/%d/%Y %H:%M:%S:%f")[:-3]}')


def print_file(log, down):
    loc = input("Issue location: ")
    cli = input("Client: ")

    dte = now.strftime("%d-%m-%Y")

    filename = f'C:/Users/{user}/Documents/{dte}_{loc}_{cli}.txt'
    f = open(filename, "w")
    log_len = len(log)

    f.write(F'________________________Created {now.strftime("%d/%m/%Y %H:%M:%S")}________________________\n\n')
    f.write(f'Issue location: {loc} \nClient: {cli}\n')
    f.write(f'___________________________________________________________________________\n\n\n')

    for i in range(log_len):
        tempk = list(log)
        tempv = list(log.values())

        f.write(f'{tempk[i]} | {tempv[i]}\n\n')



    f.write(f'*Estimated downtime:{down}')

    print(f'File saved as {filename}')

    f.close()


def prolif(temp, pdf):
    """
    This method allows the Lines to not overflow to the sides.
    magic is the number of characters it takes to start a new line

    :param temp:
    :param pdf:
    :return:
    """
    n = len(temp)
    magic = 95
    if n > magic:
        pdf.cell(w=538.5, h=15, txt=str(temp[:magic]), ln=1, fill=True)
        prolif(temp[magic: n-1], pdf)

    else:
        pdf.cell(w=538.5, h=15, txt=temp, ln=1, fill=True)


class PDF(FPDF):

    def header(self):
        pass

    def newpage(self):
        self.add_page()



def generate_pdf(log, down, pdf):
    loc = input("Issue location: ")
    cli = input("Client: ")
    user = getpass.getuser()
    filename = 'timeline.pdf'
    n = len(log)

    pdf = PDF(orientation='P', unit='pt', format='A4')
    pdf.newpage()

    today = date.today()

    pdf.set_font(family='Helvetica', size=24, style='B')
    pdf.cell(w=0, h=80, txt=f'Ticket Time Line', align='C', ln=1)

    pdf.set_font(family='Helvetica', size=7, )
    pdf.cell(w=0, h=10, txt='| Created ' + str(today.month) + '/' + str(today.day) + '/' + str(today.year),
              align='R', ln=1)

    pdf.set_font(family='Helvetica', size=24, style='B')
    pdf.cell(w=300, h=40, txt=f"Location: {loc}", ln=1, )

    pdf.set_text_color(255, 255, 255)
    pdf.set_fill_color(0, 0, 0)

    pdf.set_font(family='Helvetica', size=18, style='B')

    pdf.cell(w=300, h=40, txt=f"Client: {cli}", ln=1, fill=True, )
    pdf.cell(w=10, h=10, ln=1)

    pdf.set_fill_color(255, 165, 0)

    pdf.set_font(family='Helvetica', size=7, )
    pdf.cell(w=450, h=10, )
    pdf.cell(w=0, h=20, txt=f"Duration: {down}", ln=1, fill=True, align='R')

    pdf.set_text_color(255, 255, 255)
    pdf.set_text_color(0, 0, 0)
    for i in range(n):
        tempk = list(log)
        tempv = list(log.values())

        if i == 0:
            pdf.set_text_color(81, 250, 255)
            pdf.set_fill_color(57, 57, 57)

            pdf.set_font(family='Helvetica', size=8, )
            pdf.cell(w=100, h=15, txt=tempk[i], fill=True)
            pdf.set_text_color(26, 255, 0)
            pdf.cell(w=438.5, h=15, txt=">START", ln=1, fill=True)

            pdf.set_text_color(0, 0, 0)

            pdf.set_fill_color(219, 219, 219)

            pdf.set_font(family='Helvetica', size=10)
            prolif(tempv[i], pdf)
            pdf.cell(w=10, h=10, ln=1)

        elif i == (n - 1):
            pdf.set_text_color(81, 250, 255)
            pdf.set_fill_color(57, 57, 57)

            pdf.set_font(family='Helvetica', size=8, )
            pdf.cell(w=100, h=15, txt=tempk[i], fill=True)

            pdf.set_text_color(255, 0, 0)
            pdf.cell(w=438.5, h=15, txt="END}", ln=1, fill=True)

            pdf.set_text_color(0, 0, 0)
            pdf.set_fill_color(219, 219, 219)

            pdf.set_font(family='Helvetica', size=10)
            prolif(tempv[i], pdf)

        else:
            pdf.set_text_color(81, 250, 255)
            pdf.set_fill_color(57, 57, 57)

            pdf.set_font(family='Helvetica', size=8, )
            pdf.cell(w=538.5, h=15, txt=tempk[i], ln=1, fill=True)

            pdf.set_text_color(0, 0, 0)
            pdf.set_fill_color(219, 219, 219)

            pdf.set_font(family='Helvetica', size=10)
            prolif(tempv[i], pdf)

            pdf.cell(w=10, h=10, ln=1)

    live = True
    while live:
        try:
            pdf.output(filename)
            input("Saved file at location:" + filename +
                  "\n (ENTER to QUIT)")
            live = False
        except:
            input("Could not save file at location:" + filename +
                  "\n Make sure file is closed if saved.\n (ENTER to Try again)")


generate_logs(now)
