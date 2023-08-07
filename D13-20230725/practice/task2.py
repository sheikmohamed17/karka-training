my_detailils=[{"Name":"Sheik Mohamed","Place":"Eruvadi","hobbies":["Cricket","Football","Travelling"]},{"Name":"sobith","Place":"Kaliyakavilai","hobbies":["Playing","Movies","Traveilng"]},{"Name":"Sham","Place":"Monday_Market","hobbies":["Cricket","Traveling","Movies"]},{"Name":"Boobathi","Place":"Parvathipuram","hobbies":["Writing","Dancing","Traveling"]},{"Name":"Renisha","Place":"Marthandam","hobbies":["Music","Drawing","Gardening"]},{"Name":"Shalini","Place":"Kulachal","hobbies":["Dancing","Drawing","Book Reading"]},{"Name":"Bhuvana","Place":"VellaMadam","hobbies":["Craft","Gardening","Drawing"]}]
my_detailils.append({"Name":"Ajil","place":"nagercoil","hobbies":["watching movies"]})
selected_item=input("Enter the Hobbies:")
for detail in my_detailils:
    for hobbie in detail["hobbies"]:
        if selected_item==hobbie:
            my_detailils.update(["is eligible"]=="True")
            print(my_detailils["is eligible"])
            # print(detail["Name"])
        else:
            my_detailils.update("is eligible"=="False")
            print(my_detailils["is eligible"])
