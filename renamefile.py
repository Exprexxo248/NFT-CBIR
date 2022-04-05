import magic
import os
import sys
import getopt

path = sys.argv[1]
print(path)
for filename in os.listdir(path):
  f = os.path.join(path,filename)
  newPath = os.Path.splitext(f)[0]
  os.rename(f,newPath)
