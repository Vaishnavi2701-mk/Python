import os

oldfile='sample.txt'
newfile='sample2.txt'

with open(oldfile) as f:
    content=f.read()

with open(newfile,'w') as f:
    f.write(content)

    os.remove(oldfile)
    