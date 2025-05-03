print("Input first leg length: ", end="")
# Casting to float. Input without prompt.
leg_a = float(input())

# Casting to float. Input with prompt.
leg_b = float(input("Input second leg length: "))

hypo = (leg_a**2 + leg_b**2) ** .5
print("Hypotenuse length is", hypo)

# Casting to integer.
# In here, if you enter a number not integer format, it will throw an error.
integer = int(input("Input a integer: "))

print("The ineteger value multiplicated by 2 is", integer * 2)