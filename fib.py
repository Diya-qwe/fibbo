n = int(input("The third pull req Enter number of terms: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
    print("f1 new added")
