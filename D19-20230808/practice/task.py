
# size = int(input("n:"))
# for i in range(0, size):
#     for j in range(0, size):
#         print(j+i, end="")
#         j=j+i
#         i=i+1
#     print()
n=5
for i in range(n*n,0,-1):
    # print(i,end="")
    if i%n==0:
        print("\n")
    print(i,end=" ")