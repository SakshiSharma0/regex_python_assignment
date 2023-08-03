words=['tent','nest','try','nice','test','asha']
sentence=[]
for ch in words:
    if(ch[0]==ch[-1]):
        sentence.append(ch)
print(sentence)