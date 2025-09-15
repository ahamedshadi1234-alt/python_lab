numbers = input("Enter the numbers:")
num = numbers.split()
print(num)
over=[]

for i in num:
    i=int(i)
    if i < 100:
        over.append(i)
    else:
        over.append("over")

print(over)        
