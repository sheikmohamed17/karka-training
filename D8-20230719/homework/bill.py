user_food={"milk":1.02,"popcorn":2.5,"bread":2.5}
product1=input("Enter the Product:")
product2=input("Enter the product:")
#if product1 != user_food[0]and product2 != user_food[0]:
if (product1==user_food[2] and product2==user_food[1])or(product2==user_food[1] and product1==user_food[2]):
    # if product1 or product2==user_food[2]:
        print("The Price of ",user_food["popcorn"]+user_food["bread"])
#     # print("The Rate of Product is:",user_food["milk"])
# elif product1 and product2!=user_food[1]:
elif (product1 ==user_food[0]or product2==user_food[0])and (product1==user_food[1] or product2==user_food[1]):
        # if product1 or product2==user_food[2]:
            print("The Price of",user_food["milk"]+user_food["bread"])
# print(user_food[0])
# if (product1==user_food[0]and product2==user_food[1])or(product1==user_food[1]and product2==user_food[0]):
#     eprint("The Total amount of your bill:",user_food["milk"]+user_food["popcorn"])