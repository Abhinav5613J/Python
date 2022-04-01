dic={}
a=int(input("Enter the number of elements you want in your list: "))
for i in range(0,a):
  x=input("Enter your key for your elements: ")
  y=input("Enter your value for this particular key: ")
  dic.update({x:y})
print("\n",dic)
