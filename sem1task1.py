print("Введите длины сторон треугольника через пробел и нажмите Enter")
a = int(input())
b = int(input())
c = int(input())

if a+b<=c or a+c<=b or b+c<=a:
    print("Не существует")
elif a==b and a==c:
    print("Равносторонний")
elif a==b or a==c or b==c:
    print("Равнобедренный")
else: print("Разносторонний")