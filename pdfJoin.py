from os import listdir, mkdir, startfile
from os.path import isfile, join, exists
from PyPDF2 import PdfMerger
import re
import os
import glob
import shutil
import string

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
    merger = PdfMerger()    
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

def joinPDF():
    # Input file path and print the pdf files in that path
    rootdir = input("Enter the folder location: ")
    arrayLoader(rootdir)
    # for file in os.listdir(rootdir):
    #     d = os.path.join(rootdir, file)
    #     if os.path.isdir(d):
    #         rootDirStack.append(d)

    for folders in rootDirStack:
        arrayLoader(folders)



def purgeArrayLoader(filePath):
    splitDirty = filePath.rsplit('\\',1)
    if (str("Output") == str(splitDirty[1])):
        moveAndEmpty(filePath)

    else:
        for file in os.listdir(filePath):
            d = os.path.join(filePath, file)
            if os.path.isdir(d):
                rootDirStack.append(d)


def moveAndEmpty(filePath):
    sourcePath = filePath.rsplit('\\',1)
    for file in os.listdir(filePath):
        d = os.path.join(filePath, file)
        if os.path.isfile(d):
            dest = shutil.move(d,sourcePath[0], copy_function = shutil.copytree)
    os.rmdir(filePath)


def purgeOutputFolder():
    rootdir = input("Enter the folder location: ")
    purgeArrayLoader(rootdir)

    for folders in rootDirStack:
        purgeArrayLoader(folders)

# def deleteEmptyFolder():
#     deleteInput = input("Enter the delete folder location: ")
#     os.rmdir(deleteInput)

# def moveFileUp():
#     moveInput = input("Enter the move folder location: ")
#     destination = moveInput.rsplit('\\',1)
#     print(destination[0])


answer = input("Enter 1 to Join or 2 to purge Output:")
match str(answer):
    case "1":
        joinPDF()
    case "2":
        purgeOutputFolder()
    case _:
        print("Sorry, invalid request.")
