# class grandpa():
#     def house (self):
#         print ("Take my House")
#
# class dad(grandpa):# Multi level inheritance
#     def shares(self):
#         print("Take my shares")
# class mom ():
#     def food(self):
#         print("Take the Sweets")
# class son(dad,mom):# Multiple Inheritance
#     def job(self):
#         print("I have my job")
#
# mark = son()
# mark.job()
# mark.shares()
# mark.food()
# mark.house()
#Single, Multiple, Multy level, hierarchical(2 Son inherits single parent) & Hybrid(combination of multiple and Multilevel) Inheritance is possible in python

# Super Keyword
class yellow():
    def __init__(self):
        print("A")
    def display(self):
        print("I am in class yellow")
class a():
    def display(self):
        print("I am in class a")
class b(yellow):
    super(yellow)
    def display(self):
        print("I am in class b")

obj = b()


