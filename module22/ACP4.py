#disarium number
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** len(str(num))
    temp //= 10
    print("Sum of digits raised to the power of their positions:", sum)
if num == sum:
    print(num, "is a Disarium number")
else:
    print(num, "is not a Disarium number")