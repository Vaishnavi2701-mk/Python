with open('p.txt') as f:
    ans=f.read()

    if 'twinkle' in ans:
        print("Twinkle is present in poem")
    else:
        print('Twinkle is not present')        
