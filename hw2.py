# Cloud Computing Homework 2 - Docker
# Author: Ian Simon

import os, socket

def listTextFiles ():
    resultFile = open("../output/result.txt", "a")
    resultFile.write("List of text files in /home/data:\n")
    for file in os.listdir("../data"):
        if file.endswith(".txt"):
            resultFile.write(file + "\n")
    
    resultFile.close()


def countWords ():
    resultFile = open("../output/result.txt", "a")
    resultFile.write("\nWord Counts & Total:\n")
    total = 0
    highest = 0
    highestName = ""
    for file in os.listdir("../data"):
        if file.endswith(".txt"):
            filepath = os.path.join("../data", file)
            txtfile = open(filepath, "r")
            data = txtfile.read()
            txtfile.close()

            words = data.split()
            num = len(words)
            total += num

            if num > highest:
                highest = num
                highestName = file

            resultFile.write("Words in " + file + ": " + str(num) + "\n")
    
    resultFile.write("Total words: " + str(total) + "\n")

    if highestName == "":
        resultFile.write("No Files found with text, therefore no file has maximum word count\n")
    else:
        resultFile.write("File with maximum words: " + highestName + " with " + str(highest) + "\n")
    
    resultFile.close()


def getIP ():
    resultFile = open("../output/result.txt", "a")
    resultFile.write("\nIP Address:\n")
    resultFile.write(str(socket.gethostbyname(socket.gethostname())))
    resultFile.close()

    resultFile = open("../output/result.txt", "r")
    data = resultFile.read()
    print(data)


listTextFiles()
countWords()
getIP()