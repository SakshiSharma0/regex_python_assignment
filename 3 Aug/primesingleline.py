number=[2,3,4,5,6,11,34,3,19,7,21]

prime=[num for num in number if num>1 and all(num%i  !=0 for i in range(2,num))]
print(prime)