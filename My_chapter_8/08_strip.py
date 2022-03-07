#print(line)
#print(line.strip())

def removeandstrip(string, word):
    str=string.replace(word,"")
    return str.strip()
line="           dolly is good girl     "    
ans=removeandstrip(line, "dolly")
print(ans)
