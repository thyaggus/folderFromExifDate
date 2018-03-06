#!/usr/bin/python

import sys
import os
import exifread
from shutil     import copyfile
from os         import listdir
from os.path    import isfile, join


root = "";

def moveFile (dir, file):
    directory = "./sorted/" + dir
    destiny = directory + "/" + file
        
    if not os.path.exists(directory):
        os.makedirs(directory)
    copyfile(file, destiny)
    


def extracData ():
    fileList = [fl for fl in listdir(".") if isfile(join(".", fl))]
    for file in fileList:
        if file.endswith(".jpeg") or file.endswith(".jpg") or file.endswith(".tiff") or file.endswith(".JPEG") or file.endswith(".JPG") or file.endswith(".TIFF"):
            tags = exifread.process_file(open(file, 'rb'))
            for tag in tags.keys():
                if tag in ('EXIF DateTimeOriginal'):
                    folder = str(tags[tag])
                    folder = folder[:10].replace(":", "-")
                    moveFile(folder, file)

def main():
    extracData()

if __name__ == "__main__":
    main()
    
    
    #### begin of experiment

def display(i, total):
	percent = i*100/total
	processed = int(percent*70/100)
	progress = ""
	blank = ""

	for p in range (i):
		progress = progress + "="
	for b in range (total - i):
		blank = blank + " "
	progress = progress + blank

    if i % 4 == 1:
    	print ("| [%s]", progress, end="")
	elif i % 4 == 2:
		print ("/ [%s]", progress, end="")
	elif i % 4 == 3:
		print ("- [%s]", progress, end="")
	else:
		print ("\\ [%s]", progress, end="")

def extracData ():
    fileList = [fl for fl in listdir(".") if isfile(join(".", fl))]
    totalFiles = len(fileList)
    for i range (totalFiles)
    	file = fileList[i]
        if file.endswith(".jpeg") or file.endswith(".jpg") or file.endswith(".tiff") or file.endswith(".JPEG") or file.endswith(".JPG") or file.endswith(".TIFF"):
            tags = exifread.process_file(open(file, 'rb'))
            for tag in tags.keys():
                if tag in ('EXIF DateTimeOriginal'):
                    folder = str(tags[tag])
                    folder = folder[:10].replace(":", "-")
                    moveFile(folder, file)
                    display(i, totalFiles)


#### end of experiment
