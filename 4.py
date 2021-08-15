n= int(input("Enter a number: "))
m = 0
temp = n
while temp > 0:
    digit = temp % 10
    m += digit ** 3
    temp //= 10
if n == m:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")