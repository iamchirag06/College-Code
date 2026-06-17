from scipy import stats

data = [2, 3, 5, 3, 7, 3, 8]
mode = stats.mode(data, keepdims=True)
print(f"Mode: {mode.mode[0]}")  # Output: 3