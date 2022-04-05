import magic
import os
import sys
import getopt

ExceptType=["GIF","text","ASCII"]
path = sys.argv[1]
print(path)
for filename in os.listdir(path):
  f = os.path.join(path,filename)
  string = magic.from_file(f)
  if any(x in string for x in ExceptType):
    os.remove(f)
