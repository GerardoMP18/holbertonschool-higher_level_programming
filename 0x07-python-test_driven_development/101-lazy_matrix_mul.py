#!/usr/bin/python3
import numpy as np
"""
Lazy matrix multiplication

Write a function that multiplies 2 matrices by using the module NumPy
"""


def lazy_matrix_mul(m_a, m_b):
    """Function for multiplie 2 matrices with numpy"""
    return (np.matmul(m_a, m_b))
