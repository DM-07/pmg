import numpy as np
import sys

def getName(fileName):
    #print(fileName)
    splitres = fileName.split("/")
    trueName = splitres[len(splitres) - 1]
    return trueName # return base file name

def combinecsv(fileName, fileIndex):
    try:
        a = open(fileName, "r")
    except:
        print("No such file named " + fileName, file=sys.stderr)
        return -1
    filerow = 0
    trueName = getName(fileName)
    if trueName[-4:] != ".csv":
        print(fileName + " is not a csv file", file=sys.stderr)
        return -1
    for fileLine in a:
        if fileIndex == 1 and filerow == 0: # first file in the series
            print(fileLine.strip() + ",\"filename\"")
        elif filerow != 0:
            print(fileLine.strip() + ",\"" + trueName + "\"")
        filerow = filerow + 1
    a.close() # close file
    return 0

if __name__ == "__main__":
    listLen = len(sys.argv)
    #print(listLen)
    if listLen == 1:
        print("Please specify csv files", file=sys.stderr)
        sys.exit(0)
    fileList = sys.argv[1:]
    for i in range(listLen - 1):
        fileName = fileList[i]
        res = combinecsv(fileName, i+1)
        if res != 0: # some error occurred, exit
            sys.exit(0)
