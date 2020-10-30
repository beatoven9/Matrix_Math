#!/usr/bin/env python

def dot_product(vect_a, vect_b):
    if len(vect_a) != len(vect_b):
        print("error: vectors must be of equal length to find dot product")
        return 0
    dot_product = 0
    for i in range(len(vect_a)):
        dot_product += (vect_a[i] * vect_b[i])
    return dot_product

def add_vectors(vect_a, vect_b):
    if len(vect_a) != len(vect_b):
        print("error: vectors must be of equal length to find sum")
        return 0
    sum_vector = [0] * len(vect_a)

    for i in range(len(vect_a)):
        sum_vector[i] = vect_a[i] + vect_b[i]
    return sum_vector

def subtract_vectors(vect_a, vect_b):
    if len(vect_a) != len(vect_b):
        print("error: vectors must be of equal length to find sum")
        return 0
    sum_vector = [0] * len(vect_a)

    for i in range(len(vect_a)):
        sum_vector[i] = vect_a[i] - vect_b[i]
    return sum_vector

if __name__ == "__main__":
    vect_a = [2, 3, 3]
    vect_b = [4, 5, 4]

    product = dot_product(vect_a, vect_b)

    sum = add_vectors(vect_a, vect_b)

    print(product)
    print()
    print(sum)
