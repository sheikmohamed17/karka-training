items_list={"apple":9,"drinks":4,"water":2}
selected_item=input("Enter the items:")
quantity=input("Enter the Quatity")
if selected_item in items_list:
    for item in items_list:
      price=items_list[item]
      if item==selected_item:
        total_price=price*amount
        print(selected_item,price,amount)
        print("Total_price:"total_price)

else:
    print("Does not exist")
