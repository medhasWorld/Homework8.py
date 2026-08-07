base = int(input("Enter a base number: "))
exponent = int(input("Enter a expotential value: "))
result = 1
for x in range(exponent):
    result = result * base
print("result= ", result)