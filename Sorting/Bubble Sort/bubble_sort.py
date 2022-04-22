a=int(input("Enter the number of element you want on your list: "))
l=[]
for i in range(0,a):
    x=int(input(f"\nENter the {i+1} element: "))
    l.append(x)
print("\nYour list is: ",l)

#Bubble Sort

for i in range(0,a):
     for j in range(0,a-i-1):
         if l[j]>l[j+1]:
             temp=l[j+1]
             l[j+1]=l[j]
             l[j]=temp
print(f"\nYour sorted list is: {l}\n")
