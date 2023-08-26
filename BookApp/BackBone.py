from google_drive_downloader import GoogleDriveDownloader as g
import os
from datetime import datetime, timedelta

########################################################################################################################
BooksList = []
ImgList = []
global BookFile
global ImgFile
global output
global output2
global OutputBook
global KeyId
global ImgID
########################################################################################################################
try: BookFile = open("Keystorage/Keystorage.txt","r")
except:pass

try: ImgFile = open("Keystorage/Imgstorage.txt","r")
except:pass

output = "Keystorage/Keystorage.txt"
output2 = "Keystorage/Imgstorage.txt"
OutputBook ="Books/"
KeyId = ""
ImgID = ""
########################################################################################################################


def checkFile():
    global BookFile; global ImgFile
    global output;global output2
    global KeyId


    if (os.path.isfile("Keystorage/Keystorage.txt")):
        temp = datetime.fromtimestamp(os.path.getatime("Keystorage/Keystorage.txt")).strftime('%d/%m/%Y')
        DateOfFile = datetime.strptime(temp, "%d/%m/%Y")

        DateOnMachine = datetime.now()

        if DateOfFile + timedelta(days=30) < DateOnMachine:

            g.download_file_from_google_drive(file_id=KeyId,dest_path=output,unzip = True)
            g.download_file_from_google_drive(file_id=ImgID, dest_path=output2, unzip=True)

            try:BookFile = open("Keystorage/Keystorage.txt", "r")
            except:pass

            try:ImgFile = open("Keystorage/Imgstorage.txt", "r")
            except:pass

    else:
        try:
            os.mkdir("Keystorage")

            g.download_file_from_google_drive(file_id=KeyId, dest_path=output, unzip=True)
            g.download_file_from_google_drive(file_id=ImgID, dest_path=output2, unzip=True)

            try:BookFile = open("Keystorage/Keystorage.txt", "r")
            except:pass

            try:ImgFile = open("Keystorage/Imgstorage.txt", "r")
            except:pass

        except OSError as error:

            g.download_file_from_google_drive(file_id=KeyId, dest_path=output, unzip=True)
            g.download_file_from_google_drive(file_id=ImgID, dest_path=output2, unzip=True)

            try:BookFile = open("Keystorage/Keystorage.txt", "r")
            except:pass

            try:ImgFile = open("Keystorage/Imgstorage.txt", "r")
            except:pass

########################################################################################################################

def ReadBooksIn():

    if BooksList == []:
        checkFile()
        global BookFile
        BookFile = sorted(BookFile)

        for line in BookFile:
            temp =line.split(" ")

            try:
                temp[0]=temp[0].replace("\n","")
                temp[1] = temp[1].replace("\n", "")

            except IndexError:pass

            if temp[0] != 'Books.txt' and  temp[0] != "" and temp[0] != "Books.Exe" and temp[0] != "Imgstorage.txt":
                BooksList.append(temp)

            else:
                pass
    return BooksList

########################################################################################################################

def GetImgArray():

    if ImgList == []:
        checkFile()
        global ImgFile
        ImgFile =sorted(ImgFile)

        for line in ImgFile:
            temp = line.split(" ")

            try:
                temp[0] = temp[0].replace("\n","")
                temp[1] = temp[1].replace("\n", "")

            except IndexError:pass

            if temp[0] != 'Books.txt' and temp[0] != "" and temp[0] != "Books.Exe" and temp[0] != "Imgstorage.txt":
                if temp[1] != "":
                    ImgList.append(temp)
                else:
                    temp[1] = "img.jpg"
                    ImgList.append(temp)

            else:
                pass
    return ImgList

########################################################################################################################

def GetFile(x):
    y=x.split(",")
    print(y)

    if os.path.isdir("Books"):
        g.download_file_from_google_drive(file_id=y[1], dest_path=OutputBook+y[0], unzip=True)

    else:
        os.mkdir("Books")
        g.download_file_from_google_drive(file_id=x[0], dest_path=OutputBook+x[1], unzip=True)

########################################################################################################################

def UpdateFile():
    BooksList.clear()
    ImgList.clear()
    os.remove("Keystorage/Keystorage.txt")
    os.remove("Keystorage/Imgstorage.txt")
