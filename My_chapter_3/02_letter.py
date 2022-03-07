letter='''Dear <|Name|>,
        Many many congratulations to you,
        you are selected!
         <|Date|>'''
name=input("Enter the name\n")
date=input("Enter the date\n")        
letter=letter.replace("<|Name|>",name)  
letter=letter.replace("<|Date|>",date)

#lat=letter.replace("many",name) if I store the changes in the new variable then it will not change,thus save it in original variable.
print(letter)

