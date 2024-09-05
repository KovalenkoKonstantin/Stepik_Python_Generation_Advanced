a = 1
b = 25

# Если a больше b, меняем их местами
if a > b:
    a, b = b, a

result = []

for num in range(a, b + 1):
    digits = str(num)
    # Проверяем каждую цифру
    if '0' not in digits and all(num % int(digit) == 0 for digit in digits):
        result.append(num)

# Печатаем подходящие числа через пробел
# print(" ".join(map(str, result)))
print(*result)