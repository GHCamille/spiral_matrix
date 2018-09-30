# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 14:03:15 2018

@author: Camille
"""

import numpy as np


def spiral_matrix(n):
    """ 
    program that generates a spiral matrix 
    """
    output_matrix = np.zeros((n,n))
    output_matrix[-1][-1]=1
    current_line = n-1
    current_col = n-1
    current_value = 1
    while current_value<n*n:
        while (current_col-1>=0) and (output_matrix[current_line][current_col-1]==0):
                current_col -= 1
                current_value +=1
                output_matrix[current_line][current_col] = current_value
                print(output_matrix)
        while (current_line-1>=0) and (output_matrix[current_line-1][current_col]==0):
                current_line -= 1
                current_value +=1
                output_matrix[current_line][current_col] = current_value
                print(output_matrix)
        while (current_col+1<=n-1) and (output_matrix[current_line][current_col+1]==0):
                current_col += 1
                current_value +=1
                output_matrix[current_line][current_col] = current_value
                print(output_matrix)
        while (current_line+1<=n-1) and (output_matrix[current_line+1][current_col]==0):
            current_line += 1
            current_value +=1
            output_matrix[current_line][current_col] = current_value
    return output_matrix
