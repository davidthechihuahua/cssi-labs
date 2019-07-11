num1 = int(raw_input("Give me a number: "))
num2 = int(raw_input("Give me a second Number: "))

def additionFunction(add1,add2):
    sum = add1 + add2
    return sum
print("here is the sum: " + str(additionFunction(num1, num2)))


def subtractionFunction(sub1,sub2):
    dif = sub1 - sub2
    return dif
print("here is the difference: " + str(subtractionFunction(num1, num2)))


def multFunction(mult1,mult2):
    prod = mult1 * mult2
    return prod
print("here is the product: " + str(multFunction(num1, num2)))
