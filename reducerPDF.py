from PyPDF2 import PdfReader, PdfWriter

def reducer_pdf(pdf_result):

    reader = PdfReader(pdf_result)
    writer = PdfWriter()

    for page in reader.pages:
        page.compress_content_streams()  # This is CPU intensive!
        writer.add_page(page)

    with open(pdf_result, "wb") as f:
        writer.write(f)