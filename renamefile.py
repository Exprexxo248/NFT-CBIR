import mimetypes
import magic
import os
import sys
import getopt

def get_extension(filePath):
  return "."+mime.from_file(filePath).split("/")[1]


path = sys.argv[1]
baseName = str(path.split("/")[-1])+"_"
mime = magic.Magic(mime=True)


for filename in os.listdir(path):
  filename = filename.split("_")[-1]
  oldFile = os.path.join(path,filename)
  ext = get_extension(oldFile)

  newName = baseName+filename.split(".")[0]+ext
  newFile = os.path.join(path,newName)

  os.rename(oldFile,newFile)

# for filename in os.listdir(path):
#   newName = filename.split("_")[-1]
#   oldFile = os.path.join(path,filename)
#   newFile = os.path.join(path,newName)

#   os.rename(oldFile,newFile)


