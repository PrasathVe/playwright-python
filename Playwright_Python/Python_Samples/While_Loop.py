#simple while loop
i=100
while(i>=10):
    print (i)
    i=i-10

# find the factorial for the user input value
giv_value = int (input())
fact = 1
while (giv_value >0):
        fact = fact*giv_value
        giv_value=giv_value-1
print("Factorial Value of the number is:",fact)


