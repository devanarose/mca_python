# Print the pyramid of numbers using for loops.
i = 0
n = int(input("Enter the limit: "))
# n = 8
for i in range(1, n + 1):
    for j in range(n - i + 1):
        print(" ", end="")

    for k in range(1, i+1):
        print(i, end=" ")
    print()
    

