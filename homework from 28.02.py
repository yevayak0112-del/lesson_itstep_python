'''
def suma(*numbers):
    print(sum(numbers))
print(suma(1, 2, 3, 4))

def maximum(*number):
    print(max(number))
print(maximum(5, 8, 2, 10, 3))

def ser_grade(name, *grades):
    ser = sum(grades) / len(grades)
    print(f"Середній бал студента {name}: {ser:.2f}")
print(ser_grade("Yeva", 10, 12, 9, 11))

def merge_lists(*lists):
    result = []
    for lst in lists:
        result.extend(lst)
    print(result)
print(merge_lists([1, 2], [3, 4], [5, 6]))
'''
from webbrowser import open_new

text = input("Введіть рядок: ")
print(text[::-1] + "\n")

for numbers in range(1, 11):
    print(f"{numbers}\n")

price = 123.45
print(f"{price:.2f} грн")

a = "груша"
b = "огірок"
c = "полуниця"
print(f"{a}\t{b}\t{c}")