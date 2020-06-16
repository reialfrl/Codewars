import numpy as np

def generate_integers(m, n):
    if m <= n: return np.arange(m, n+1).tolist()
    else: return 'The first value must be less than the second'

