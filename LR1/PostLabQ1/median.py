def compute_median(numbers):
    n = []
    for i in numbers:
        n.append(i)
    n.sort()
    midpoint = len(n) // 2
    if len(n) % 2 == 1:
        return n[midpoint]
    else:
        return (n[midpoint] + n[midpoint - 1]) / 2