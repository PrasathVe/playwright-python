# class Travel:
#     South = "Enjoy the Travel!"
#     def gotoBangalore(self):
#         print("Going for Business Purpose")
#     def gotoChennai(self):
#         print("Going for Planned Vacation")
#     def gotoGoa(self):
#         print ("Going for Party")
from platform import processor

# ramesh = Travel()
# suresh = Travel()
#
# ramesh.gotoBangalore()
# suresh.gotoGoa()
# print(suresh.South)
#_________________________________________________________
class laptop:
# created Variables
    brand = ""
    processor = ""
    ram = ""
#Creaed Objects & Assigned Values to the property
dell = laptop()
dell.ram="64GB"
dell.processor = "Intel"
dell.brand = "Dell"
hp = laptop()
hp.ram="16GB"
hp.brand="hp"
hp.processor="Rayzon"
apple = laptop()
apple.brand = "Apple"
apple.processor="ARM"
apple.ram="128GB"

def printModels():
    print (dell.brand,dell.processor,dell.ram)
    print (hp.brand,hp.processor,hp.ram)
    print (apple.brand,apple.processor,apple.ram)
printModels()
