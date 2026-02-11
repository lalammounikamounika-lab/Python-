num = int(input("Enter number: "))

last = num % 10  

while num >= 10:
    num = num // 10

first = num      

if first == last:
    print("Same")
else:
    print("Not Same")