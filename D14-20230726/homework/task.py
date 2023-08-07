userDtails = [{
    "name" : "saravana",
    "e_mail" : "saravana@gmail.com",
    "password" : "saravan@123",
},
{
    "name" : "benish",
    "e_mail" : "benish@gmail.com",
    "password" : "benish@123",
},
{
    "name" : "kabeesh",
    "e_mail" : "kabeesh@gmail.com",
    "password" : "kabeesh@123",
},
{
    "name" : "naathan",
    "e_mail" : "naathan@gmail.com",
    "password" : "naathan@123",
}]

def login():
    emailid=input("Enter the E-Mail-id:")
    password=input("Enter the password:")
    for each_id in userDtails:
        if emailid==each_id["e_mail"]:
            if password==each_id["password"]:
                print("Login succesfful")
            else:
                print("Enter the correct password")
        else:
            print("enter the correct id")
        break
# login=login()
def register():
    email=input("Email:")
    username=input("Name:")
    passwrd=input("Password:")
    crtpasswrd=input("crt password:")
    for id in userDtails:
        if email==id["e_mail"]:
            print("Go to Login")
        elif email!=id["e_mail"]:
            if passwrd!=crtpasswrd:
                print("Enter the Correct Password")
            new_user={"name":username,"e_mail":email,"password":passwrd}
    userDtails.append(new_user)
    print(userDtails)
    print("---Successfully Registered---")
            
Login_or_register=input("Login or register:")
if Login_or_register=="Login":
    login()
elif Login_or_register=="register":
    register()



    
    
