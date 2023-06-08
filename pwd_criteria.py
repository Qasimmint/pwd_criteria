def passwordCheck(pwd):
    spe_char = ("!", "@", "#", "$", "%", "&")

    if len(pwd)!=8:
        return False

    if any(x.isupper() for x in pwd) and any(y.islower() for y in pwd) and any(z.isdigit() for z in pwd) and any(char in pwd for char in spe_char):
        print("Password Correct")

    else:
        print("Wrong Password")

by_user = input("Enter: ")
passwordCheck(by_user)
