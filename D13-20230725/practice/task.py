# fruits=["apple","pineapple","grapes"]
# vegtabes=["tomato","brinjal"]
# print(fruits[0])
# fruits.append("pineapple")#add the element at last
# fruits[1]="orange"#replace the element
# fruits.insert(1,"cherry")#add the element in particular place
# print(fruits)
# fruits_vegtables=fruits+vegtabes#combine the two strings
# print(fruits_vegtables)
# detailes={"name":"sheik_mohamed","place":"tirunelvelli"}
# detailes["age"]=21#add the element in dictnory
# detailes.update({"e_mail-id":"safeeqameen@gmail.com","website":"sheik_mohamed_al-ameen"})
# print(detailes)
# freinds=["Bhoobathi","Sathya Tharma","Sheik mohamed","Shobith","bhuvana","Shalini","Renisha"]
# print(freinds[0])
# if my_detailils[7]["Name"]=="Ajil":
#     print("New Freind is Added")
# else:
# #     print("Doesn't added")
# selected_item=input("Enter the Hobbies:")
# for detailes in my_detailils:
#     detailes["hobbies"].append("coding")
#     print(detailes)
#     if selected_item==detailes["hobbies"]:
#         print(detailes[Name])
my_detailils=[{"Name":"Sheik Mohamed","Place":"Eruvadi","hobbies":["Cricket","Football","Travelling"]},{"Name":"sobith","Place":"Kaliyakavilai","hobbies":["Playing","Movies","Traveilng"]},{"Name":"Sham","Place":"Monday_Market","hobbies":["Cricket","Traveling","Movies"]},{"Name":"Boobathi","Place":"Parvathipuram","hobbies":["Writing","Dancing","Traveling"]},{"Name":"Renisha","Place":"Marthandam","hobbies":["Music","Drawing","Gardening"]},{"Name":"Shalini","Place":"Kulachal","hobbies":["Dancing","Drawing","Book Reading"]},{"Name":"Bhuvana","Place":"VellaMadam","hobbies":["Craft","Gardening","Drawing"]}]
my_detailils.append({"Name":"Ajil","place":"nagercoil","hobbies":["watching movies"]})
selected_item=input("Enter the Hobbies:")
for detail in my_detailils:
    for hobbie in detail["hobbies"]:
        if selected_item==hobbie:
            print(detail["Name"])
 
