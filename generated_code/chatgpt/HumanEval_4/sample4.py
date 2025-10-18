import numpy as np
    if not numbers:
        return 0.0
    arr = np.array(numbers)
    mean = np.mean(arr)
    mad = np.mean(np.abs(arr - mean))
    return float(mad)