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
    print("Start processing ...")
    fileList = [fl for fl in listdir(".") if isfile(join(".", fl))]
    for file in fileList:
        if file.endswith(".jpeg") or file.endswith(".jpg") or file.endswith(".tiff") or file.endswith(".JPEG") or file.endswith(".JPG") or file.endswith(".TIFF"):
            tags = exifread.process_file(open(file, 'rb'))
            for tag in tags.keys():
                if tag in ('EXIF DateTimeOriginal'):
                    folder = str(tags[tag])
                    folder = folder[:10].replace(":", "-")
                    moveFile(folder, file)
     print("Finished")

def main():
    extracData()

if __name__ == "__main__":
    main()
