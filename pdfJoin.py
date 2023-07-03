from os import listdir, mkdir, startfile
from os.path import isfile, join, exists
from PyPDF2 import PdfFileMerger
import re
import os
import glob

#holds the order from the original directory
rootDirStack = []

def pdfJoin(path):
    pdffiles = [f for f in listdir(path) if isfile(join(path, f)) and '.pdf' in f]

    fileName = pdffiles[0]

    m = re.search('(?<=_)(.*)(?<=_)(.*)(?=.pdf)', fileName)
    newFileName = m.group(0)
    #Input the name of the result file
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
    #startfile(path+'\\Output\\'+newFileName)

def arrayLoader(filePath):
    if not exists(filePath+'\\Output'):
        testPath = filePath + '/*.pdf'
        if len(glob.glob(testPath)) <= 1:
            for file in os.listdir(filePath):
                d = os.path.join(filePath, file)
                if os.path.isdir(d):
                    rootDirStack.append(d)
        else:
            pdfJoin(filePath)

            
# Input file path and print the pdf files in that path
rootdir = input("Enter the folder location: ")

for file in os.listdir(rootdir):
    d = os.path.join(rootdir, file)
    if os.path.isdir(d):
        rootDirStack.append(d)

for folders in rootDirStack:
    arrayLoader(folders)
