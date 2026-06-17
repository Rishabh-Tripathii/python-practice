# Basic Pascal_Triangle solution
def pascal_triangle(rows):
    for i in range(rows):
        num = 1
        print(" "*(rows-i-1),end=" ")
        for j in range(i + 1):
            print(num, end=" ")
            num = num * (i - j) // (j + 1)
        print()

n = int(input("Enter rows: "))
pascal_triangle(n)
