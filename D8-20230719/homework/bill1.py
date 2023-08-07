user_food={"milk":1.02,"popcorn":2.5,"bread":2.5}
product1=input("Enter the product1:")
product2=input("Enter the product2:")
if (product1=="milk"and product2=="popcorn")or(product1=="popcorn"and product2=="milk"):
    print("The Total Bill is:",user_food["milk"]+user_food["popcorn"])
elif (product1=="popcorn" and product2=="bread")or(product1=="bread"or product2=="popcorn"):
    print("The total bill is:",user_food["popcorn"]+user_food["bread"])
elif (product1=="milk"and product2=="bread")or(product1=="bread"and product2=="milk"):
    print("The total bill is:",user_food["bread"]+user_food["milk"])
else:
    print("Please purchase the correct item")