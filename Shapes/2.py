#Equilateral triangle
input_lines = int(input("Enter number of lines: "))
for i in range(1, input_lines + 1):
    print(" " * (input_lines - i) + "*" * (2 * i - 1))