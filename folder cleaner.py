import os
import shutil
list = []
i = 0 
destinationdir = 'folder name'
while os.path.exists(destinationdir):
    destinationdir += str(i)
    i+=1
os.makedirs(destinationdir)
os.path.abspath(__file__)
list = os.listdir('folder name')
for x in list:
    print (x)
    if x == __file__:
        continue
    shutil.move(x,destinationdir)
