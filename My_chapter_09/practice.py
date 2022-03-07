#f=open('me.txt','r')
#f.write("Vaishnavi is good girl!")
#f.write("\nShe is really very good!")
#data=f.read()
#print(data)
#f.close()

#**with statement**#

with open("me.txt",'r') as f:   # no need toclose the function and read is the default mode
#with open('me.txt','r') as f:
    f.read(5)
