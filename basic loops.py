
def isprime(num):
    if num > 1:
        if num == 2:
            return True
        for n in range(2, num):
            if (num % n) == 0:
                return False
        return True


i = 1
while i <= 100:
    print(i)
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    if isprime(i):
        print("Prime")
    i += 1
    print()

