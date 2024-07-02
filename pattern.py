#1 Function to print a half pyramid pattern
def half_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("* ", end="")
        print("")

# Example: Print a half pyramid with 5 rows
n = 10
half_pyramid(n)


print("\n")

##2 Function to print inverted half pyramid pattern
def inverted_half_pyramid(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print("* ", end="")
        print("\r")

## Example: Inverted Half Pyramid with n = 5
n = 10
inverted_half_pyramid(n)


print("\n")


#3Function to print inverted full pyramid pattern
def inverted_full_pyramid(n):
    for i in range(n, 0, -1):
        for j in range(n - i):
            print(" ", end="")
        for k in range(2*i - 1):
            print("*", end="")
        print("")
 ## Example: Inverted Half Pyramid with n = 5       
n = 10
inverted_full_pyramid(n)

print("\n")
##
## 4 function to print inverted full pyramid pattern
def print_space(space):
    if space > 0:
        print(" ", end="")
        print_space(space - 1)

def print_star(star):
    if star > 0:
        print("*", end="")
        print_star(star - 1)

def print_pyramid(n, current_row=1):
    if current_row > n:
        return

    spaces = n - current_row
    stars = 2 * current_row - 1
    print_space(spaces)
    print_star(stars)

    print()
    print_pyramid(n, current_row + 1)

 #Set the number of rows for the pyramid
n = 10
print_pyramid(n)
