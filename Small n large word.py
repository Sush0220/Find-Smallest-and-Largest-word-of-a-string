import array as words

def SmallLargeWord(str1):
    w=""
    words=[]
    str1+=" "
    for i in range(len(str1)):
        if(str1[i]!=' '):
            w+=str1[i]
        else:
            words.append(w)
            w=" "
    sm=lg=words[0]
    for j in range(len(words)):
        if(len(sm)>len(words[j])):
            sm=words[j]
        elif(len(lg)<len(words[j])):
            lg=words[j]
    return sm,lg

str1=input("Enter string= ")
print(str1)
sm,lg=SmallLargeWord(str1)
print("Smallest word= ",sm)
print("Largest Word= ",lg)
