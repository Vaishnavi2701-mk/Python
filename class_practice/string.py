string1=input("Enter the first string:\n")
str=string1.lower()
string2=input("Enter the second string:\n")
substring=input("Enter the substring to check if it is present in string1 or not\n")

def reverse(str):
    str=str[::-1]
    return str
def equality(s1,s2):
    if s1==s2:
        return ("\niii)Two strings are equal")
    else:
        return ("\niv)Two strings are not equal")

print(f"\n First String entered by the user is:\n {string1}")
print(f"\n Second String entered by the user is:\n {string2}")

def sub(s):
    try:
        if s in string1:
            return (f"\nv)The substring {s} exist in the string {string1}")
        else:
            return (f"\nv)The substring {s} doesn't exist in the string {string1}")

    except ValueError as e:
        return (f"Please enter a valid value,\nYour iput results in an error {e}")
    

def palindrom(a,b):
    if a==b:
        return (f"\niv)The string {a} is palindrom as it is same when read in reverse ")
    else:
        return (f"\niv)The string {a} is not a palindrom as it is not same when read in reverse ") 



print("\ni) Length of the string is: ",len(string1))
ans=reverse(string1)
result=ans.lower()
print("\nii) Reverse of the string is: ", ans)
equal=equality(string1,string2)
print(equal)
print(palindrom(str,result))
print(sub(substring))
