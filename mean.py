X = np.array([[1, 2, 3],
              [4, 5, 6]])

mean = X.mean(axis=1, keepdims=True)
std = X.std(axis=1, keepdims=True)

normalized = (X - mean) / std
print(normalized)
