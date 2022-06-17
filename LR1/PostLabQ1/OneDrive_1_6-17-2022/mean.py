def compute_mean(numbers):
    j = 0
    computed_mean = 0
    for i in numbers:
        computed_mean += i
        j += 1
    computed_mean = computed_mean / j
    return computed_mean