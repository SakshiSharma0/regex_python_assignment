a,b,c=input("Enter three sides of triangles : ").split()
a=int(a)
b=int(b)
c=int(c)
if(a==b==c):
    print("Equilateral")
elif(a==b or a==c or b==c):
    print("Isoceles")
elif( (a*a+b*b==c*c) or (c*c+b*b==a*a) or (a*a+c*c==b*b)):
    print("Right Angled")
else:
    print("Enter valid side")