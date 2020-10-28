#!/usr/bin/env python

import vector_math as Vector

class Matrix:

    def __init__(self, dimensions=[1, 1], elements=None, identity=False, zero=False):
        
        if dimensions == [1, 1] and elements == None and identity==False and zero==False:
            self.query_elements()
            self.refresh_matrix()
        elif identity == True:
            print('creating identity matrix')
            self.create_identity_matrix()
        elif zero == True:
            self.dimensions = dimensions
            self.create_zero_matrix()
        else:
            print('what kind of matrix are you making?')
        
        

    def query_elements(self):
        rows, columns = [int(dimension) for dimension in input('Input the dimensions of the matrix in "rows, columns" format: ').split(', ')]  
        matrix = []
        self.dimensions = [rows, columns]
        self.set_default_vals()

        for i in range(rows):
            matrix.append([])
            for j in range(columns):
                matrix[i].append(int(input("input elem (%d, %d):" % (i, j))))

        self.set_elements(matrix)
        print('Is this matrix correct?:\n')
        self.print_matrix()
        print()
        if input('Y/n: ') == 'n':
            self.query_elements()    

    def set_elements(self, matrix_vals):
        self.elements = matrix_vals
        self.set_rows()
        self.set_columns()

    def set_rows(self):
        self.rows = []
        for row in self.elements:
            self.rows.append(row)

    def set_columns(self):
        self.columns = []
        for i in range(0, len(self.rows[0])):
            self.columns.append([])
            for j in range(0,self.dimensions[0]):
                self.columns[i].append(self.elements[j][i])
#        self.columns = []
#        for i in range(self.dimensions[1]):
#            if len(self.columns) <= i:
#                self.columns.append([])
#            for j in range(self.dimensions[0]):
#                if len(self.columns[i]) <= j:
#                    self.columns[i].append(self.elements[j][i])
#                else:
#                    self.columns[i][j] = self.elements[j][i]

    def set_default_vals(self):
        #this creates a zero matrix of dimensions 'dimensions'
        matrix = []
        for i in range(0, self.dimensions[0]):
            matrix.append([])
            for j in range(0, self.dimensions[1]):
                matrix[i].append(0)
        self.set_elements(matrix)
        #this is causing a bug because each row is occupying the same space in memory
        #self.elements = [[0] * self.dimensions[0]] * self.dimensions[1] 

    def create_identity_matrix(self):
        # create zero matrix of dimensions 'dimensions' then set every dimension+1th value to 1
        self.create_zero_matrix()

        if self.dimensions[0] != self.dimensions[1]:
            print("Error: an identity matrix must be a square matrix.")
            self.create_zero_matrix()
        
        counter = 0

        for i in range(len(self.elements)):
            for j in range(len(self.elements[i])):
                if counter > 0:
                    self.elements[i][j] = 0
                    self.refresh_matrix()
                elif counter == 0:
                    self.elements[i][j] = 1
                    self.refresh_matrix()
                    counter = self.dimensions[0] + 1
                counter -= 1
        
    def refresh_matrix(self):
        self.set_rows()
        self.set_columns()

    def query_dimensions(self):
        rows, columns = [int(dimension) for dimension in input('Input the dimensions of the matrix in "row, column" format: ').split(', ')]
        self.dimensions = [rows, columns]

    def create_zero_matrix(self):
        if self.dimensions == [1,1]:
            self.query_dimensions() 
        self.set_default_vals()
        self.set_rows()
        self.set_columns()

    def print_matrix(self):
        for row in self.elements:
            print(row)
#        print()
#        for column in self.columns:
#            print(column)

def define_matrix(elements):
    pass

def multiply_matrices(matrix_a, matrix_b):
    if matrix_a.dimensions[1] != matrix_b.dimensions[0]:
        print("ERROR: these matrices are not compatible for multiplication.\n")
        return
    product_matrix = Matrix(dimensions=[matrix_a.dimensions[1], matrix_b.dimensions[0]], zero=True)
    
    for i in range(len(product_matrix.rows)):
        for j in range(len(product_matrix.columns)):
            product_matrix.elements[i] = Vector.dot_product(matrix_a.rows[i], matrix_b.columns[j])

    return product_matrix

if __name__ == '__main__':
    new_matrix = Matrix()

    second_matrix = Matrix()
    print()
    second_matrix.print_matrix()
    print()
    new_matrix.print_matrix()
    print()
    second_matrix.refresh_matrix()
    new_matrix.refresh_matrix()
    product_matrix = multiply_matrices(new_matrix, second_matrix)
    product_matrix.print_matrix()