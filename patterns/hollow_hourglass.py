n = 5

# Upper half
for i in range(n, 0, -1):

    # Left spaces
    print(" " * (n - i), end="")

    for j in range(1, 2 * i):

        # Border condition
        if j == 1 or j == (2 * i - 1) or i == n:
            print("*", end="")
        else:
            print(" ", end="")

    print()

# Lower half
for i in range(2, n + 1):

    # Left spaces
    print(" " * (n - i), end="")

    for j in range(1, 2 * i):

        # Border condition
        if j == 1 or j == (2 * i - 1) or i == n:
            print("*", end="")
        else:
            print(" ", end="")

    print()