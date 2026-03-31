def generate_series(N):
    series = []
    
    # First 5 terms are powers of 2
    for i in range(min(N, 5)):
        series.append(2**i)
        
    # Remaining terms follow custom increments
    increments = [7, 5, 10, 11]  # can extend if needed
    idx = 0
    while len(series) < N:
        next_val = series[-1] + increments[idx % len(increments)]
        series.append(next_val)
        idx += 1
    
    return series

# Example usage:
N = 10
print(generate_series(N))