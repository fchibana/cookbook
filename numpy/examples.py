import numpy as np

def min_max_scaling(arr: np.ndarray) -> np.ndarray:
    
    assert arr.shape[0] != 0, "Empty array"
    assert arr.max(axis=0) != arr.min(axis=0), "Constant array"
    
    return (arr - arr.min(axis=0)) / (arr.max(axis=0) - arr.min(axis=0))