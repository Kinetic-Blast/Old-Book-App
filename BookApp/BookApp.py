import eel
import BackBone

eel.init('Web')


@eel.expose
def GetBookNames():
   eel.GetBooks(BackBone.ReadBooksIn(),BackBone.GetImgArray())

@eel.expose
def GetFile(x):

   print(x)
   BackBone.GetFile(x)

@eel.expose
def UpdateFile():

   try:BackBone.UpdateFile()
   except:pass

   GetBookNames();



eel.start('hello.html',mode = "--app")      # Start (this blocks and enters loop)