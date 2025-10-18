import numpy as np
    arr = np.array(numbers)
    if arr.size < 2:
        return False
    diff_matrix = np.abs(arr[:, None] - arr)
    np.fill_diagonal(diff_matrix, np.inf)
    return np.any(diff_matrix < threshold)