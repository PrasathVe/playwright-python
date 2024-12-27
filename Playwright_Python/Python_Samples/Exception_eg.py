try:
    a = int (input("Enter a value"))
    b = int (input("Enter b vallue"))
    print (a+b)
except Exception as e:
    print("Something",e)
finally:
    print("Something")