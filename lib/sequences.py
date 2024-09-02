#!/usr/bin/env python3

def print_fibonacci(length):
    if not isinstance(length, int) or length < 0:
        print("Please provide a non-negative integer.")
        return
    
    
    fib_sequence = []
    a, b = 0, 1
    while len(fib_sequence) < length:
        fib_sequence.append(a)
        a, b = b, a + b

    # Print the sequence
    print(fib_sequence)

# Example usage
print_fibonacci(0)  # Should print []
print_fibonacci(5)  # Should print [0, 1, 1, 2, 3]
print_fibonacci(-1) # Should print error message
