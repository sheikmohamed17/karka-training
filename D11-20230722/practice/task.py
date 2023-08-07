# gold_rates_monthly=[{"month":"Jan","goldrate":300},{"month":"Feb","goldrate":3281},{"month":"Mar","goldrate":1750},{"month":"Apr","goldrate":500},[{}]]
# min_value=gold_rates_monthly[0]["goldrate"]
# max_value=gold_rates_monthly[0]["goldrate"]
# min_month=gold_rates_monthly[0]["month"]
# max_month=gold_rates_monthly[0]["month"]
# for gold_rate_monthly in gold_rates_monthly:
#     print("Gold rate",gold_rate_monthly["goldrate"])
#     if gold_rate_monthly["goldrate"]<=min_value:
#         min_value=gold_rate_monthly["goldrate"]
#         min_month=gold_rate_monthly["month"]
#     if gold_rate_monthly["goldrate"]>=max_value:
#         max_value=gold_rate_monthly["goldrate"]
#         max_month=gold_rate_monthly["month"]
# print("Max Value:",max_value,"Max_month",max_month)
# print("min value:",min_value,"Min_month",min_month) 
# This task will explain to analyses the data to find the month with min and max gold rate along with the total cost of each jewel for the months with the min and max god rates.


monthly_jwel_rate = [
    {"month":"Jan",
     "gold_rate":2000,
     "jwels_list":[{
         "name":"chain",
         "making_charge":12
     },{
         "name":"ring",
         "making_charge":10
     }]},
     {"month":"Feb",
     "gold_rate":4000,
     "jwels_list":[{
         "name":"chain",
         "making_charge":12
     },{
         "name":"ring",
         "making_charge":10
     }]},
     {"month":"March",
     "gold_rate":3600,
     "jwels_list":[{
         "name":"chain",
         "making_charge":12
     },{
         "name":"ring",
         "making_charge":10
     }]},
     {"month":"April",
     "gold_rate":3678,
     "jwels_list":[{
         "name":"chain",
         "making_charge":12
     },{
         "name":"ring",
         "making_charge":10
     }]},
     {"month":"May",
     "gold_rate":4500,
     "jwels_list":[{
         "name":"chain",
         "making_charge":12
     },{
         "name":"ring",
         "making_charge":10
     }]},
]

# below to find the minium and maximum gold rate 

min_rate = monthly_jwel_rate[0]["gold_rate"]
max_rate = 0
min_max_data  = {}
for jwel_data in monthly_jwel_rate:

    gold_rate = jwel_data["gold_rate"]
    month = jwel_data['month']

    if gold_rate <= min_rate:
        min_rate = gold_rate
        min_rate_month = month

    if gold_rate >= max_rate:
        max_rate = gold_rate
        max_rate_month = month

min_max_data['min_month_rate'] = {
    "month":min_rate_month,
    "gold_rate":min_rate,
    }
min_max_data['max_month_rate'] = {
    "month":max_rate_month,
    "gold_rate":max_rate}

# below code is to find the amount for minimum and maxium gold rate jwells 

for jwels_data in monthly_jwel_rate:

    jwels_list = jwels_data["jwels_list"]
    gold_rate = jwels_data["gold_rate"]
    month = jwels_data['month']
    for jwels in jwels_list:
        making_charge = gold_rate *(jwels["making_charge"]/100)
        gst = gold_rate * .18
        total = gold_rate + making_charge + gst
        if month == min_rate_month:
            min_max_data['min_month_rate'][jwels['name']] = total
        elif month == max_rate_month:
            min_max_data['max_month_rate'][jwels['name']] = total
            

print(min_max_data)
