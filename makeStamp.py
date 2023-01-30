from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import inch
import datetime

def make_stamp(x,y):
    """
    # To review real paper size
    import PyPDF2

    pdf = PyPDF2.PdfFileReader("01.pdf","rb")
    p = pdf.getPage(0)

    w_in_user_space_units = p.mediabox.getWidth()
    h_in_user_space_units = p.mediabox.getHeight()

    # 1 user space unit is 1/72 inch
    w_in = float(p.mediabox.getWidth()) * 0.013889
    h_in = float(p.mediabox.getHeight()) * 0.013889

    # 1 user space unit is 1/72 inch
    # 1 inch unit is 96 pixels
    #w = float(p.mediabox.getWidth()) * 0.013889 * 96
    #h = float(p.mediabox.getHeight()) * 0.013889 * 96
    w = int(p.mediabox.getWidth()) * 0.013889 * 96
    h = int(p.mediabox.getHeight()) * 0.013889 * 96

    print(pdf.metadata)
    print(str(w_in) + " in")
    print(str(h_in) + " in")
    print(str(w) + " px")
    print(str(h) + " px")
    """

    # Canvas
    c = canvas.Canvas("stamp.pdf",pagesize=landscape(A4)) #Size A4 Landcape

    # Stamp position
    #x_pos = 6*inch
    #y_pos = 2*inch
    x_pos = x*inch
    y_pos = y*inch


    # Choose Color
    c.setStrokeColorRGB(1,.051,0)
    c.setFillColorRGB(1,.051,0)

    # Define a large font
    c.setFont("Helvetica-Bold", 14)

    # Draw big rectangle
    w_rec1 = 150
    h_rec1 = 80
    c.rect(x_pos,y_pos,w_rec1,h_rec1, stroke=1, fill=0)

    # Draw small rectangle
    w_rec2 = 100
    h_rec2 = 30
    c.rect((x_pos+25),(y_pos+25),w_rec2,h_rec2, stroke=1, fill=0)

    # Write text
    #c.drawString(630,330,"Stamp")
    c.drawCentredString((x_pos+75),(y_pos+63), "EFECTIVE ON")
    c.drawCentredString((x_pos+75),(y_pos+7), "CONTROLLED")

    #Time
    timex = datetime.datetime.now()
    timex = timex.strftime("%Y/%m/%d")

    # Define a small font
    c.setFont("Helvetica", 14)
    c.drawCentredString((x_pos+75),(y_pos+36), timex)

    #The showPage method causes the canvas to stop drawing
    c.showPage()
    #Save the PDF
    c.save()