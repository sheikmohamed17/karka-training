items_list = [
    {'name': 'Apple', 'category': 'Fruits'},
    {'name': 'Carrot', 'category': 'Vegetables'},
    {'name': 'Banana', 'category': 'Fruits'},
    {'name': 'Broccoli', 'category': 'Vegetables'},
]
fruit=[]
vegtable=[]
dic={}
def fruit_vegtable():
    for each in items_list:
        name=each["name"]
        cat=each["category"]
        if cat == "Fruits" :
            fruit.append(name)
        elif cat== "Vegetables" :
            vegtable.append(name)
    dic.update({"Vegetables": vegtable,"Fruits": fruit})        
    print(dic)
fruit_vegtable()
