# Задаємо значення чисел
a = float(input("Введіть (a): "))
b = float(input("Введіть (b): "))

# Виводимо результати обчислень
print("\nresults:\n")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} ** {b} = {a ** b}")

# Перевірка, щоб b не дорівнювало 0
if b != 0:
    print(f"{a} / {b} = {a / b}")
    print(f"{a} // {b} = {a // b}")
    print(f"{a} % {b} = {a % b}")
else:
    print(f"{a} / {b} = Помилка: на 0 ділити не можна")
    print(f"{a} // {b} = = Помилка: на 0 ділити не можна")
    print(f"{a} % {b} = = Помилка: на 0 ділити не можна")
