x = int(input("Enter 1st Number: "))
y = int(input("Enter 2nd Number: "))
z = int(input("Enter 3rd Number: "))
n = int(input("Enter Number of Combinations: "))
mylist = x,y,z
for i in range(n):
    for j in range(n):
        for k in range(n):
            if (i!=j and j!=k and k!=i):
                print(mylist[i], mylist[j],mylist[k])


