n = 5

for i in range(1, n + 1):

    # Right alignment spaces
    print("  " * (n - i), end="")

    for j in range(1, i + 1):

        # Border conditions
        if j == 1 or j == i or i == n:
            print("* ", end="")

        else:
            print("  ", end="")

    print()