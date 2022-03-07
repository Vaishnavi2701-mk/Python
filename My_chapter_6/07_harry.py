post=input("Enter the post\n")

if ("harry" in post):
    print("yes, post is talking about harry")
elif("HARRY" in post):
          print(" yes, post is talking about HARRY")
elif("Harry" in post):
    print("yes, this post is talking about harry")
else:
    print("This post is not talking about harry")             