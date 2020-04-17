import keyword

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


def check_Identifier():
    input_identifier = input("Enter the identifier name: ")
    s = input_identifier
    # short way -->
    '''
    if s.isidentifier():
        print("Valid")
    '''
    keywords = keyword.kwlist
    special = "!@:;',./|\#%^&*-"
    fal = 0
    tru = 0
    if s in keywords:
        fal += 1
    if any(i in special for i in s):
        fal += 1
    for i in range(len(s)):
        if s[0].isdigit() or s[i] == " ":
            fal += 1
    if all(i.isalnum() for i in s):
        tru += 1
    if any(i == '_' or i == '$' for i in s):
        tru += 1
    if fal == 0 and tru != 0:
        print("Valid Identifier!!")
    else:
        print("Invalid Identifier!!")


def check_Email():
    input_Email = input("Enter the Email: ")
    e = input_Email
    r = "abcdefghijklmnopqrstuvwxyz._0123456789/\*-"
    if "@" in e:
        t = e.partition("@")
        if all(i in r for i in t[0]):
            if all(j in r for j in t[2]) and (t[2].endswith(".com") or t[2].endswith(".in")):
                print("Valid Email!!")
            else:
                print("Invalid Email!!")
