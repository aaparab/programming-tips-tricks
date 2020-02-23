# General purpose Python tips (not Jupyter)

########################################
# General
########################################
# documentation:
def foo(bar):
    """ This is a docstring. """

foo.__doc__
# $ 'This is a docstring. '

########################################
# Measure program execution time
########################################
from time import time
start = time()
# Program code
end = time()
print("Time to execute: {} seconds.".format(end - start))

########################################
# Format printing large numbers
########################################
"{:_}".format(123456789)
# >> '123_456_789

########################################
# Create path if not exists:
########################################
import pathlib
pathlib.Path("my/dir/location").mkdir(parents=True, exists_ok=True)

########################################
# Running shell commands in Python
########################################
import subprocess
# When using the subprocess module, to save the standard output
# to a variable, add "stdout=subprocess.PIPE" to the call.
cp = subprocess.run(["ls", "-al"], stdout=subprocess.PIPE)
print(cp.stdout.decode("ascii"))

########################################
# Merge/split pdf files
########################################

# Reference: https://www.geeksforgeeks.org/working-with-pdf-files-in-python/
# To solve error or printing blank page, see [here](https://stackoverflow.com/a/51331661/8100373)
import PyPDF2

# see number of pages
pdfFileObj = open('EAD-1.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages) 

# merge pdfs
def PDFmerge(pdfs, output):  
    pdfMerger = PyPDF2.PdfFileMerger() # creating pdf file merger object 

    for pdf in pdfs: # appending pdfs one by one 
        pdfMerger.append(PyPDF2.PdfFileReader(f), 'rb')

    with open(output, 'wb') as f: # writing combined pdf to output pdf file 
        pdfMerger.write(f)
        
# pdf split
def PDFsplit(pdf, splits): 
    pdfFileObj = open(pdf, 'rb') # creating input pdf file object 
      
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj) # creating pdf reader object 
      
    start = 0 # starting index of first slice     
    end = splits[0] # starting index of last slice 
    
    for i in range(len(splits)+1): 
        pdfWriter = PyPDF2.PdfFileWriter() # creating pdf writer object for (i+1)th split 
          
        outputpdf = pdf.split('.pdf')[0] + str(i) + '.pdf' # output pdf file name 

        for page in range(start,end): # adding pages to pdf writer object 
            pdfWriter.addPage(pdfReader.getPage(page)) 
          
        with open(outputpdf, "wb") as f: # writing split pdf pages to pdf file 
            pdfWriter.write(f) 
  
        
        start = end # interchanging page split start position for next split 
        try: # setting split end positon for next split 
            end = splits[i+1] 
        except IndexError: # setting split end position for last split 
            end = pdfReader.numPages 

    pdfFileObj.close() 










