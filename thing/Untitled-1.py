def is_self_describing(number):
    # Convert the number to a string to easily access individual digits
    str_number = str(number)
    
    # Count the occurrences of each digit
    digit_counts = [0] * len(str_number)
    
    for digit in str_number:
        digit = int(digit)
        if digit < 0 or digit >= len(str_number):
            # Invalid digit for self-describing number
            return False
        digit_counts[digit] += 1
    
    # Check if the counts match the description
    for i, count in enumerate(digit_counts):
        if count != int(str_number[i]):
            return False
    
    # If all checks pass, it's a self-describing number
    return True

# Example usage:
number = 200
if is_self_describing(number):
    print(f"{number} is a self-describing number.")
else:
    print(f"{number} is not a self-describing number.")
