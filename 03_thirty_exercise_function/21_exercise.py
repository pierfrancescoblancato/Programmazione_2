def sum_ric(n):
    return n + sum_ric(n - 1) if n > 0 else 0

print(sum_ric(5))