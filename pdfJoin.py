from os import listdir, mkdir, startfile
from os.path import isfile, join, exists
from PyPDF2 import PdfFileMerger
import re

# Input file path and print the pdf files in that path
path = input("Enter the folder location: ")
pdffiles = [f for f in listdir(path) if isfile(join(path, f)) and '.pdf' in f]
print('\nList of PDF Files:\n')
for file in pdffiles:
    print(file)

fileName = pdffiles[0]

#"_([A-Za-z0-9]+( [A-Za-z0-9]+)+)_([A-Za-z0-9]+( [A-Za-z0-9]+)+)\.pdf"gm

m = re.search('_([A-Za-z0-9]+( [A-Za-z0-9]+)+)_([A-Za-z0-9]+( [A-Za-z0-9]+)+)\.pdf', fileName)
mCleaner = re.search('([A-Za-z0-9]+( [A-Za-z0-9]+)+)_([A-Za-z0-9]+( [A-Za-z0-9]+)+)',m.group(0))
print(mCleaner.group(0))
newFileName = mCleaner.group(0)
#Input the name of the result file
#resultFile = input("\nEnter the name of the result file : ")
if '.pdf' not in newFileName:
    newFileName += '.pdf'

# Append the pdf files
merger = PdfFileMerger()
for pdf in pdffiles:
    merger.append(path+'\\'+pdf)

# If the Output directory does not exist then create one
if not exists(path+'\\Output'):
    mkdir(path+'\\Output')

# Write the merged result file to the Output directory
merger.write(path+'\\Output\\'+newFileName)
merger.close()

# Launch the result file
print('\n'+newFileName, 'Successfully created!!! at ', path+'\\Output\\')
startfile(path+'\\Output\\'+newFileName)
