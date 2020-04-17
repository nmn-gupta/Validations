print("Press 1. for validate password")
print("Press 2. for validate Email")
print("Press 3. for validate Identifier name")
print("Press 4. for validate IPv4 address")


def check_Password():
    input_password = input("Enter the password: ")
    s = input_password
    special = ",.#@$%&^*_-"
    flag = 1
    l = len(s)
    if any(i.isspace() for i in s):
        print("Inavalid Password!!")
        print("There shouldn't be any space!!")


    elif not (l >= 5):
        print("Inavalid Password!!")
        print("Password must contain atleast five characters!!")


    elif not (l <= 10):
        print("Inavalid Password!!")
        print("Password contains atmost ten characters!!")


    elif not (any(i.isdigit() for i in s)):
        print("Inavalid Password!!")
        print("Password must contains atleast one digit!!")


    elif not (any(i in special for i in s)):
        print("Inavalid Password!!")
        print("Password must contain atleast one special character!!")


    elif not (any(i.isupper() for i in s)):
        print("Inavalid Password!!")
        print("Password must contain atleast one upper case alphabet!!")


    elif not (any(i.islower() for i in s)):
        print("Inavalid Password!!")
        print("Password must contain atleast one lower case alphabet!!")


    else:
        print("Valid Password")
