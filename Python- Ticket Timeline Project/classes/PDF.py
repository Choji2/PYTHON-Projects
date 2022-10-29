from fpdf import FPDF

class PDF(FPDF):
    """
    This class sole purpose is to utilize the Header and the Footer functions of FPDF
    """
    def header(self):
        self.image("source\\timeline-solid.png", 538.5, 10, w=20, h=20)

    def footer(self):
        # Go to 1.5 cm from bottom
        self.set_y(-15)
        # Select Arial italic 8
        self.set_font('Arial', 'B', 8)
        # Print centered page number
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

    def newpage(self):
        self.add_page()
