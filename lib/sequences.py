#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_sequence = []
    if length == 0:
        print(fibonacci_sequence)
        return

    a, b = 0, 1
    
    fibonacci_sequence.append(a)
    for _ in range(length - 1):
        a, b = b, a + b  
        fibonacci_sequence.append(a)
    
    print(fibonacci_sequence)
    
    
