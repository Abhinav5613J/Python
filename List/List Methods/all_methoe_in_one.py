import time
lst=[]
a=int(input("Enter the number of elements you want: "))
for i in range(0,a):
    b=input("Enter the elments: ")
    lst.append(b)
print("Your original list is: ",lst)
methods=["append()","clear()","copy()","count()","extend()","idex()","insert()","pop()","remove()","reverse()","sort()"]
time.sleep(1)
print("YOur method present for list are: ",methods)
c=input("Enter your method: ")
if(c=="append()" or c=="Append()"):
    a=input("Enter the element: ")
    lst.append(a)
    print("Your list after this method: ",lst)
elif(c=="clear()" or c=="Clear()"):
    lst.clear()
    print("Your list after this method: ",lst)
elif(c=="copy()" or c=="Copy()"):
    a=lst.copy()
    print("Your original list is: ",lst)
    print("Your copied list is: ",a)
elif(c=="count()" or c=="Count()"):
    a=input("Enter the elements present in list to count it's index: ")
    b=lst.count(a)
    print("Your index of selected elment is: ",b)
elif(c=="Extend()" or c=="extend()"):
    ext=[]
    a=int(input("Enter the number of element you want to extend: "))
    for i in range(0,a):
        b=input("Enter the elements for extending the current list: ")
        ext.append(b)
    lst.extend(ext)
    print("List after extending it: ",lst)
elif(c=="index()" or c=="Index()"):
    a=input("Enter the elment from list to find the index of that element: ")
    b=lst.index(a)
    print("Index of your element from list is: ",b)
elif(c=="insert()" or c=="Insert()"):
    a=int(input("Enter the index to insert element in list: "))
    b=input("Enter the element: ")
    lst.insert(a,b)
    print("Your list after inserting the element to a specific position: ",lst)
elif(c=="pop()" or c=="Pop()"):
    b=int(input("Enter the index to delete "))
    if(b>a):
        print("Please select the valid index.")
    else:
        lst.pop(b)
        print("The new list is: ",lst)
elif(c=="remove()" or c=="Remove()"):
    a=input("Enter the element from list to remove it: ")
    lst.remove(a)
    print("The list after using remove() method is: ",lst)
elif(c=="reverse()" or c=="Reverse()"):
    lst.reverse()
    print("The list after reversing it: ",lst)
elif(c=="sort()" or c=="Sort()"):
    lst.sort()
    print("List after sorting it: ",lst)
else:
    print("Please select the valid methods!")
