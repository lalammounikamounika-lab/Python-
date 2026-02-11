a = [66, 67, 68, 69, 70, 71, 72, 73, 74]

num = int(input("Enter a roll number: "))

for i in a:
    if i == num:
        print("She is already an accountant")
        break
else:
    a.append(num)
    print("She does not exist in the list, added to the list")
    print("Updated list:", a)