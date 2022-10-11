# importing required modules
import PyPDF2

# creating a pdf file object
pdfFileObj = open('samoa.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

i = 4
while i < 5:
    # creating a page object
    pageObj = pdfReader.getPage(i)
    # extracting text from page
    print(pageObj.extractText())
    i+=1


# closing the pdf file object
pdfFileObj.close()
