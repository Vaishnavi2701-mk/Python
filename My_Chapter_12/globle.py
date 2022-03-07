a=76                       # this is globle number

def num():
    global a
    print("The number is",a)

    a=89                          # we are changinh globle a

    print(f"The number is {a}")

num()                            # closing the function

print(f"The number is {a}")       # once we changed the goble number it reamins the same thats why it wil l print 89