items_list = [
    {'name': 'Apple', 'category': 'Fruits'},
    {'name': 'Carrot', 'category': 'Vegetables'},
    {'name': 'Banana', 'category': 'Fruits'},
    {'name': 'Broccoli', 'category': 'Vegetables'},
]
fruits=[]
veg=[]
dic={}
def fruit():
    for each_item in items_list:
        if each_item["category"]=="Fruits":
            fruits.append(each_item["name"])
        elif each_item["category"]=="Vegetables":
            veg.append(each_item["name"])
        dic.update({"Fruits":fruits,"veg":veg})
#     print(dic)
    print(dic)
fruit()

