from PyPDF2 import PdfWriter, PdfReader

# Input file path and print the pdf files in that path
path = input("Enter the folder location: ")

inputpdf = PdfReader(open(path, "rb"))

for i in range(len(inputpdf.pages)):
    output = PdfWriter()
    output.add_page(inputpdf.pages[i])
    with open("document-page%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)