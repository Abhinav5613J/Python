a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=input("Enter the operators to perform the calculations('+','-','*','/'): ")
if(c=="+"):
  print("Your answer is: ",a+b)
elif(c=="-"):
  print("Your answser is: ",a-b)
elif(c=="*"):
  print("Your answer is: ",a*b)
elif(c=="/"):
  print("Your answer is: ",a/b)
else:
  print("Please enter the valid operator!")
