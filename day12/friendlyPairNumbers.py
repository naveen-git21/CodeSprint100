def sum_of_proper_divisors(n):
    divisors_sum = 1  # 1 is always a proper divisor
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:  # i and n//i are different
                divisors_sum += n // i
    return divisors_sum

def are_friendly_pairs(a, b):
    sum_a = sum_of_proper_divisors(a)
    sum_b = sum_of_proper_divisors(b)
    
    # Calculate the divisor sum ratios
    ratio_a = sum_a / a
    ratio_b = sum_b / b
    
    return ratio_a == ratio_b

# Example usage:
a, b = 6, 28
if are_friendly_pairs(a, b):
    print(f"{a} and {b} are friendly pairs.")
else:
    print(f"{a} and {b} are not friendly pairs.")
