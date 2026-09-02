n = int(input("The third pull req Enter numper of terms: "))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
    print("This is main branch")
    print("This is q1 branch")
    print("This is q2 branch")
