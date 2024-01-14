def generate_fibonacci(n):
    fibonacci_series = [0, 1]

    while len(fibonacci_series) < n:
        next_number = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_number)

    return fibonacci_series


# Example: Generate the first 10 Fibonacci numbers
n = 10
fibonacci_result = generate_fibonacci(n)
print(f"Fibonacci Series (first {n} numbers): {fibonacci_result}")
