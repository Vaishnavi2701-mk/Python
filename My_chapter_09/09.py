f1='this.txt'
f2='sample.txt'

with open(f1) as f:
    content1=f.read()
with open(f2) as f:
    content2=f.read()


if content1==content2:
    print(" two files are identicle")

else:
    print(" two files are not same")    

