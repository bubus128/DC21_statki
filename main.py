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

        address = """ <font size="9">
        SHIP TO:<br/>
        <br/>
        %s<br/>
        %s<br/>
        %s<br/>
        %s<br/>
        </font>
        """ % (xml.address1, xml.address2, xml.address3, xml.address4)
        p = Paragraph(address, styles["Normal"])
        p.wrapOn(self.canvas, width, self.height)
        p.drawOn(self.canvas, *self.coord(18, 40, mm))

        order_number = '<font size="14"><b>Order #%s </b></font>' % xml.order_number
        p = Paragraph(order_number, styles["Normal"])
        p.wrapOn(self.canvas, width, self.height)
        p.drawOn(self.canvas, *self.coord(18, 50, mm))

        data = []
        data.append(["Item ID", "Name", "Price", "Quantity", "Total"])
        grand_total = 0
        for item in xml.order_items.iterchildren():
            row = []
            row.append(item.id)
            row.append(item.name)
            row.append(item.price)
            row.append(item.quantity)
            total = Decimal(str(item.price)) * Decimal(str(item.quantity))
            row.append(str(total))
            grand_total += total
            data.append(row)
        data.append(["", "", "", "Grand Total:", grand_total])
        t = Table(data, 1.5 * inch)
        t.setStyle(TableStyle([
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black)
        ]))
        t.wrapOn(self.canvas, width, self.height)
        t.drawOn(self.canvas, *self.coord(18, 85, mm))

        txt = "Thank you for your business!"
        p = Paragraph(txt, styles["Normal"])
        p.wrapOn(self.canvas, width, self.height)
        p.drawOn(self.canvas, *self.coord(18, 95, mm))

    def readFileXML(self):
        with open(self.xml_file) as f:
            xml = f.read()
        return objectify.fromstring(xml)

    def savePDF(self):
        self.canvas.save()


if __name__ == "__main__":
    xml = "order.xml"
    pdf = "letter.pdf"
    doc = XMLtoPDF(xml, pdf)
    doc.createPDF()
    doc.savePDF()
