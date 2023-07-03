#!/usr/bin/python3
"""
Module 101-lazy_matrix_mul
Contains method to multiply matrix using numpy module (pip3 install numpy)
https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.matmul.html
"""

"""Defines a matrix multiplication function using NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return the multiplication of two matrices.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    """
    return (np.matmul(m_a, m_b))
