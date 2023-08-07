# userDtails = [{
#     "name" : "saravana",
#     "e_mail" : "saravana@gmail.com",
#     "password" : "saravan@123",
#     "h":"L"
# },
# {
#     "name" : "benish",
#     "e_mail" : "benish@gmail.com",
#     "password" : "benish@123",
# },
# {
#     "name" : "kabeesh",
#     "e_mail" : "kabeesh@gmail.com",
#     "password" : "kabeesh@123",
# },
# {
#     "name" : "naathan",
#     "e_mail" : "naathan@gmail.com",
#     "password" : "naathan@123",
# }]
# e=input("email:")
# pw=input("psw:")
# for ed in userDtails:
#     if (e==ed["e_mail"] and pw==ed["password"]):
#         userDtails.append({"d":"g"})
# #         print(ed)
a=[1,2,1,3,3,5,10,10,7,1]
b=[]
for i in range(len(a)):
    if a[i]==a[i+1]:
        b.append(a[i])
        continue
print(b)
# num=0
# for c in a:
#     if c==a[num]:
#         b.append(a[num])
#     num=num+1
# print(b)