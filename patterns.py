##Function to print a half pyramid pattern
##def half_pyramid(n):
##    for i in range(1, n + 1):
##        for j in range(1, i + 1):
##            print("* ", end="")
##        print("")
##n = 5
##half_pyramid(n)


# Function to print inverted half pyramid pattern
def inverted_half_pyramid(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print("* ", end="")
        print("\r")
n = 5
inverted_half_pyramid(n)
