def print_triangle(char, rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print(char, end=' ')
        print()

        
def print_reverse_triangle(char, rows):
    for i in range(rows, 0, -1):
        for j in range(i):
            print(char, end=' ')
        print()
        
def print_pyramid(char, rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + (char + ' ') * i)

        
def print_diamond(char, rows):
    for i in range(1, rows + 1):
        print(' ' * (rows - i) + (char + ' ') * i)
    
    for i in range(rows - 1, 0, -1):
        print(' ' * (rows - i) + (char + ' ') * i)

def print_square(char, rows):
    for i in range(rows):
        for j in range(rows):
            print(char, end=' ')
        print()

def print_pattern(pattern, char, rows):
    if pattern == 1:
        print_triangle(char, rows)
    elif pattern == 2:
        print_reverse_triangle(char, rows)
    elif pattern == 3:
        print_pyramid(char, rows)
    elif pattern == 4:
        print_diamond(char, rows)
    elif pattern == 5:
        print_square(char, rows)
    else:
        print("Invalid pattern choice")
print("Choose a pattern:")
print("1. Triangle")
print("2. Reverse Triangle")
print("3. Pyramid")
print("4. Diamond")
print("5. Square")

while True:
    try:
        pattern_choice = int(input("Enter the pattern number (1-5): "))
        if pattern_choice < 1 or pattern_choice > 5:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 5.")

character = input("Enter a character to use in the pattern: ")[0]

while True:
    try:
        num_rows = int(input("Enter the number of rows for the pattern: "))
        if num_rows <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

print_pattern(pattern_choice, character, num_rows)
