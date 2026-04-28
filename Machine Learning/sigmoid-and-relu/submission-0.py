import numpy as np
from numpy.typing import NDArray


class Solution: # lesson learned, use numpy funcs
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        return 1 / (1 + np.exp(-z))

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        return np.maximum(0, z)
