comment=input("Enter the comment\n")
spam=False
if("make a lot of money" in comment):
     spam=True
elif("buy now" in comment):
    spam=True
elif("subscribe this" in comment):
    spam=True
elif("click this" in comment):
    spam=True
else:
    spam=False
if(spam):
    print("This comment is spam!")
else:
    print("This comment is not a spam!")    


