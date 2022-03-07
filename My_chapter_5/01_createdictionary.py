mydict={"mej":"Table",
         "khubsurat":"beautiful",
         "aai":"mother",
         "kitab":"book"}


print("Your options are\n",mydict.keys())
user=input("Enter your option\n")
print("Your value is::-",mydict.get(user))