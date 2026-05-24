numbers = []

for i in range(3):
    number1 = int(input("enter the number:"))

    if number1 % 2 == 1:
        numbers.append(number1)
total = 0
for i in range(len(numbers)):
    total = total + numbers[i]
    print(total)
