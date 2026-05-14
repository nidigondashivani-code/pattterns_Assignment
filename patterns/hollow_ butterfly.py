n = 5

# Upper half
for i in range(1, n + 1):

    # Left wing
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    # Middle spaces
    print("  " * (2 * (n - i)), end="")

    # Right wing
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

# Lower half
for i in range(n - 1, 0, -1):

    # Left wing
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    # Middle spaces
    print("  " * (2 * (n - i)), end="")

    # Right wing
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()