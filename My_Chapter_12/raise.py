def raisvalue(num):
    try:
        return int(num)+1

    except:
        raise ValueError("This is not good!")


a=raisvalue("hgfhfhf")
print(a)