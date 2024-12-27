
mark = []

print ("Enter 3 Numbers")
for i in range(1,4):
   num = int (input("Enter num :"+str(i)+" "))
   mark.append(num)
print("Entered Numbers are :",mark)
print("---------------------------")

total =0
for i in mark:
   total = total+i

print ("Total Value :", total)
average = total/3
print ("Average Value :",average)






