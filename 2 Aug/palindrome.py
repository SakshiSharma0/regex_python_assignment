n=int(input("Enter a no : "))
sum=0
temp=n
while(n>0):
    rem=int(n%10)
    sum=int(sum*10+rem)
    n//=10
if(temp==sum):
    print("Palindrome")
else:
    print("Not Palindrome")
