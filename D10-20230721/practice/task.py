# n=int(input("Enter the number:"))
# if(n%3==0 and n%5==0):
#     print("FizzBuzz")
# elif(n%3==0):
#     print("Fizz")
# elif(n%5==0):
#     print("Buzz")
# else:
#     print("Number:",n)
shifts=["morning","afternoon","evening","night"]
for  shift in shifts:
    
    if shift=="morning":
       for i in range(2,45,5): 
        print(i+1,shift)