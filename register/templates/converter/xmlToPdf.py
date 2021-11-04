from decimal import Decimal
from lxml import etree, objectify

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch, mm
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle


class XMLtoPDF(object):
    def __init__(self, xml_file, pdf_file):
        self.xml_file = xml_file
        self.pdf_file = pdf_file

        self.xml_obj = self.readFileXML()

    def coord(self, x, y, unit=1):
        x, y = x * unit, self.height - y * unit
        return x, y

    def createPDF(self):
        self.canvas = canvas.Canvas(self.pdf_file, pagesize=letter)
        width, self.height = letter
        styles = getSampleStyleSheet()
        xml = self.xml_obj

        address = """ <font size="14">
        Osoba skladajaca wniosek:</font>
        <font size="10"><br/>
        <br/>
        Imie: %s<br/>
        Nazwisko: %s<br/>
        Numer dowodu: %s<br/>
        Telefon: %s<br/>
        </font>
        """ % (xml.dane_zgloszajacego.imie, xml.dane_zgloszajacego.nazwisko, xml.dane_zgloszajacego.numer_dowodu,
               xml.dane_zgloszajacego.telefon)
        p = Paragraph(address, styles["Normal"])
        p.wrapOn(self.canvas, width, self.height)
        p.drawOn(self.canvas, *self.coord(18, 50, mm))

        order_number = '<font size="14"><b>Order #%s </b></font>' % xml.numer_zgloszenia
        p = Paragraph(order_number, styles["Normal"])
        p.wrapOn(self.canvas, width, self.height)
        p.drawOn(self.canvas, *self.coord(18, 20, mm))

        order_number = '<font size="12"><b>Dane pojazdu: </b></font>'
        p = Paragraph(order_number, styles["Normal"])
        p.wrapOn(self.canvas, width, self.height)
        p.drawOn(self.canvas, *self.coord(18, 59, mm))

        data = []
        #data.append(["Item ID", "Name", "Price", "Quantity", "Total"])
        #grand_total = 0
        #for item in xml.order_items.iterchildren():
        #    row = []
        #    row.append(item.id)
        #    row.append(item.name)
        #    row.append(item.price)
        #    row.append(item.quantity)
        #    total = Decimal(str(item.price)) * Decimal(str(item.quantity))
        #    row.append(str(total))
        #    grand_total += total
        #    data.append(row)
        #data.append(["", "", "", "Grand Total:", grand_total])
        #t = Table(data, 1.5 * inch)

        data.append(["Rodzaj pojazdu: ", xml.rodzaj_pojazdu])
        data.append(["Rok produkcji: ", str(xml.rok_produkcji) + " r"])
        data.append(["Waga: ", str(xml.waga) + " kg"])
        data.append(["Dlugosc pojazdu: ", str(xml.dlugosc) + " cm"])
        data.append(["Szerokosc pojazdu: ", str(xml.szerokosc) + " cm"])
        data.append(["Glebokosc zanurzenia: ", str(xml.glebokosc_zanurzenia) + " cm"])
        data.append(["Wysokosc n.p.m.: ", str(xml.wysokosc_nad_poziomem_wody) + " cm"])

        t = Table(data, 1.7 * inch)
        t.setStyle(TableStyle([
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black)
        ]))
        t.wrapOn(self.canvas, width, self.height)
        t.drawOn(self.canvas, *self.coord(18, 105, mm))

        txt = "Zamieszczone zalaczniki:"
        p = Paragraph(txt, styles["Normal"])
        p.wrapOn(self.canvas, width, self.height)
        p.drawOn(self.canvas, *self.coord(18, 116, mm))

        data2 = []
        data2.append(["Dopuszczenie pojazdu: ", xml.zalaczniki.dopuszczenie_pojazdu])
        data2.append(["Dowod wlasnosci: ", xml.zalaczniki.dopuszczenie_pojazdu])
        t2 = Table(data2, 1.7 * inch)
        t2.setStyle(TableStyle([
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black)
        ]))
        t2.wrapOn(self.canvas, width, self.height)
        t2.drawOn(self.canvas, *self.coord(18, 130, mm))


    def readFileXML(self):
        with open(self.xml_file) as f:
            xml = f.read()
        return objectify.fromstring(xml)

    def savePDF(self):
        self.canvas.save()

