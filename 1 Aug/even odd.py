n=float(input("Enter a no to check even or odd: "))

if((type(n)==int) or (type(n)==float)):
  if(n%2==0):
    print("Even")
  else:
    print("Odd")
else:
  print("Enter a valid number!")