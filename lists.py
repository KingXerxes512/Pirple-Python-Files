myUniqueList = [] # List of unique entities
myLeftovers = [] # Will contain everything that attempts to be added to myUniqueList but is already contained

def func(addend):
    if addend in myUniqueList:
        myLeftovers.append(addend)
        return False
    else:
        myUniqueList.append(addend)
        return True
        
func(5)
func("5")
func(6.28)
func(3.1415926535)
# Everything past this point should get pushed to myLeftovers
func(5)
func("5")
func(3.1415926535)

print(myUniqueList)
print(myLeftovers)
