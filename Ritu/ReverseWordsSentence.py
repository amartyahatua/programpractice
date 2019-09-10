def reverseWord(word):
    temp=""
    for i in range(len(word)-1,-1,-1):
        temp=temp+word[i]

    return temp

word='hello'


stentence="Hello! How are you?"

words=stentence.split(" ")
result=''
for i in range(len(words)):
    result=result+reverseWord(words[i])+" "

print(stentence)
print(result)

