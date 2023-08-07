print("     HotPizza        ")
pizza=500
print(" Pizza Rate ",pizza)
orderedpizza=int(input("Enter the Number of Pizza Eaters"))
TotalPizza=orderedpizza*pizza
print(" Ordered Pizza rate only",TotalPizza)
print("Extra Topping Extra Tasty")
print(" ExtraTopping=80")
extraTopping=80
pizzawithextratopping=TotalPizza+extraTopping
print("     Rate of Pizza with Extra Topping",pizzawithextratopping)
print("Enjoy Drinks with Pizza")
rateofdrinks=45
Drinks=int(input("  Enter the Drinks"))
drinksrate=Drinks*rateofdrinks
print(" Drinks rate",drinksrate)
print(" Delivery_charge=50")
Ratewithoutgst=pizzawithextratopping+drinksrate+50
print(" Total Rate without GST",Ratewithoutgst)
Ratewithgst=Ratewithoutgst*0.18
print("Rate with GST",Ratewithgst+Ratewithoutgst)
