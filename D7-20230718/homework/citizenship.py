name=input("Enter the Name:")
gender=input("Enter the Gender:")
age=int(input("Enter your age:"))
if age>60 and gender=="Male":
    print("Hi",name,"You are a Senior Citizenship")
elif age>60 and gender=="Female":
    print("Hi Mrs.",name,"You are a Senior Citizenship")
elif (age<60 and age>18)and gender=="Male":
    print("Hi Mr.",name,"you are a Adult")
elif(age<60 and age>18)and gender=="Female":
        print("Hi Mrs.",name,"you are a Adult")
elif age<=18 and gender=="Male":
    print("Hi Mr.",name,"You is a Teenager")
elif age<=18 and gender=="Female":
    print("Hi Mrs.",name,"You is a Teenager")