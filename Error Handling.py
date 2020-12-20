def Divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print("The second input cannot be 0")
        return None


# First 3 print statements should throw an exception
print(Divide(1, 0))
print(Divide(2, 0))
print(Divide(3, 0))
print(Divide(5, 5))
print(Divide(100, 5))
print(Divide(3, 2))
