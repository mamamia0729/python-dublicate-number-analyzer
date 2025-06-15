# Duplicate Number Analyzer
# A tool to input numbers, check for duplicates, and identify palindromes

print("Welcome to the Duplicate Number Analyzer!")
print("Enter numbers to check for duplicates and palindromes.")

# Get the number of inputs
num_count = int(input("How many numbers do you want to enter? "))

# List to store tuples of (number, is_palindrome)
number_list = []

# Collect numbers and check if they are palindromes
for i in range(num_count):
    num = int(input("Enter number " + str(i + 1) + ": "))
    
    # Check if number is negative (for palindrome purposes)
    if num < 0:
        print("Warning: Negative number entered. Using absolute value for palindrome check.")
        num = abs(num)
    
    # Check if number is a palindrome
    original = num
    reversed_num = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        reversed_num = reversed_num * 10 + digit
        temp = temp // 10
    is_palindrome = original == reversed_num
    
    # Store number and palindrome status as a tuple
    number_list.append((original, is_palindrome))

# Check for duplicates
has_duplicates = False
seen_numbers = []
for index, num_tuple in enumerate(number_list):
    num = num_tuple[0]
    if num in seen_numbers:
        has_duplicates = True
    else:
        seen_numbers.append(num)

# Display results
print("\n=== Number Analysis ===")
print("All Numbers:")
for index, num_tuple in enumerate(number_list):
    palindrome_status = "Palindrome" if num_tuple[1] else "Not a Palindrome"
    print(str(index + 1) + ". " + str(num_tuple[0]) + " (" + palindrome_status + ")")

# Display duplicate status
if has_duplicates:
    print("\nDuplicate Status: Duplicates found in the list.")
else:
    print("\nDuplicate Status: No duplicates found.")
