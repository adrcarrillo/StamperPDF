import argparse
import makeStamp
import makeWatermark
import reducerPDF

"""
from tqdm import tqdm
from time import sleep
"""


"""
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
a = args.accumulate(args.integers)
print(type(a))
print(a)
"""

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
    #content_pdf=r'Z0-GH0171.pdf'
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
    """
    pbar = tqdm(total=100)
    for i in range(10):
        pbar.update(10)
        sleep(0.1)
    pbar.close()
    """
