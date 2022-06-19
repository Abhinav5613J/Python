import time
a=int(input("Enter the number of elment you want in Dictionary: "))
dic={}
lst=[]
if(a>=3):
    for i in range(0,a):
            x=input("Enter the value of key: ")
            y=int(input("Enter the value: "))
            dic.update({x:y})
    print("Your Dictionary is here:\n ",dic)
    time.sleep(1)
    for x,y in dic.items():
        lst.append(y)
    lst.sort(reverse=True)
    print(f'\nYour Three largest number are: {lst[0:3]}\n')
else:
    print("\nPlease select 3 or more values for this code!\n")
