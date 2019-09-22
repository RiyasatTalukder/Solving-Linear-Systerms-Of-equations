import math
from typing import List
import numpy as np
import pandas as pd
import time

start = time.time()

def findnumber(equations: str, index: int) -> int:
    
    while(equations[index].isdigit()):
        index+=1
        
    return index
    
def extractEquations(equations: str) -> None:
   
    equations = equations.replace(" ", "")
    equations = equations.split(',')
    cat = ''
    counter = 0
    variables = []
    solution_vector = []
    matrix = []
    matrix_column = []
    index = 0
    k = 0
    for i in equations:
        cat = ''
        if(i[0] != '-'):
            i = '+' + i
        while(k < len(i)):
            if(i[k] != '='):
                if(i[k].isdigit() or i[k] == '-' or i[k] == '+'):
                    if(i[k] == '-' or i[k] == '+'):
                        cat = cat + i[k]
                        k+=1
                        if(not i[k].isdigit()):
                            i = i[:k] + '1' + i[k:]
                    index = findnumber(i,k)
                    cat = cat + i[k:index] 
                    matrix_column.append(float(cat))
                    k = index-1
                    cat = '' 
                elif(i[k].isalpha() and counter < 1):
                    variables.append(i[k])
            else:
                cat = ''
                cat = cat + i[k+1:]
                solution_vector.append(float(cat))
                k = 0
                break
            
            k+=1
              
        matrix.append(matrix_column)   
        matrix_column = []
        counter+=1
    
    solve(matrix, solution_vector, variables)

def findNewDet(matrix: List[List[float]], soln_vector: List[float], index: int) -> float:
    
    new_matrix = []
    temp = []
    for i in matrix:
        for j in range(len(i)):
            temp.append(i[j])
        new_matrix.append(temp)
        temp = []
        
    for i in range(len(soln_vector)):
        new_matrix[i][index] = soln_vector[i]
    
    return np.linalg.det(new_matrix)

def solve(matrix: List[List[float]], soln_vector: List[float], variables: List[float]) -> None:
    
    detOriginal = np.linalg.det(matrix)
    result = 0.0
    k = 0.0
    if(detOriginal == 0):
        print("Not solvable")
    else:
        for i in range(len(variables)):
            k = findNewDet(matrix, soln_vector, i)
            result = k/detOriginal
            print('Variable',variables[i],'is: ',round(result,2))
    
s = input("Please enter the set of equations, seperated by commas: \n")
extractEquations(s)
end = time.time()
print(end - start)
  


