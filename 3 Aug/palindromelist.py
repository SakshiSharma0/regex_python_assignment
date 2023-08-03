no=[121,454,677,34,2,111]
palindrome=[]
for i in no:
    temp=i
    sum=0
    while(i>0):
        r=i%10
        sum=sum*10+r
        i=i//10
    if(sum==temp):
        palindrome.append(temp)
print(palindrome)