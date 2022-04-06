import time
dic1 = {}
dic2 = {}
a=int(input("\nEnter the number of variables you want in 1st Dictionary: "))
for i in range(0,a):
    x=input("Enter the key: ")
    y=int(input("Enter the values: "))
    dic1.update({x:y})
b=int(input("\nEnter the number of variables you want in 2nd Dictionary: "))
for i in range(0,b):
    x=input("Enter the key: ")
    y=int(input("Enter the values: "))
    dic2.update({x:y})
time.sleep(1)
print(f'Your both Dictionary are: {dic1}   {dic2}')
for key in dic2:
	if key in dic1:
		dic2[key] = dic2[key] + dic1[key]
	else:
		print("\nSorry You don't have any matching keys in both Dictionary!\n")
time.sleep(1)
print(f'\nYour new added dictionary is here: {dic2}\n')