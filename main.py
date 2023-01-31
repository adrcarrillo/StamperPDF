import argparse
import makeStamp
import makeWatermark
import reducerPDF

def run():

    # To be reviewed
    parser = argparse.ArgumentParser(prog = 'StamperPDF',description='A PDF Stamper script.', epilog='software Alpha 0.10')
    parser.add_argument('filename')
    parser.add_argument('-x', nargs='?', type=int, default=6, help ='Insert "x" distance in inches (integer number) : Default = 6 inch')
    parser.add_argument('-y', nargs='?', type=int, default=2, help ='Insert "y" distance in inches (integer number) : Default = 2 inch')
    args = parser.parse_args()
    content_pdf = args.filename
    x = args.x
    y = args.y
    print("Starting..")

    makeStamp.make_stamp(x,y) #Make stamp
    stamp_pdf=r'stamp.pdf'
    print("stamp.pdf done...")

    i = (len(content_pdf)-4) # Count string lenght
    model_name=content_pdf[:i] # Split .pdf
    pdf_result=model_name+'_marked.pdf'
    makeWatermark.watermark(content_pdf, stamp_pdf, pdf_result) # Marked
    print("Marked done...")

    reducerPDF.reducer_pdf(pdf_result)
    print("Reduced PDF file done...")
    print('Complete!')

if __name__ == "__main__":
    run()

