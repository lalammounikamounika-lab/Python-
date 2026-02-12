library_users = {599: " chaya ", 580: "amulya", 573: "teju"}
roll_no = int(input("Enter your roll number: "))
if roll_no in library_users:
    print("User exists!")
else:
    name = input("User not found. Enter your name to register: ")
    library_users[roll_no] = name
print(f"Name: {library_users[roll_no]}, Roll No: {roll_no}")