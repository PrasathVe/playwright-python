x = int(input())
y = int(input())
z = int(input())
n = int(input())
mylist = x,y,z
for i in range(n):
    for j in range(n):
        for k in range(n):
            if (i!=j and j!=k and k!=i):
                print(mylist[i], mylist[j],mylist[k])


