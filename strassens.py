import numpy as np

def strassen(A, B):
    if A.shape[0] <= 2:
        return np.dot(A, B)

    a, b, c, d = split(A)
    e, f, g, h = split(B)
    
    p1 = strassen(a + d, e + h)  # p1 = (a + d)(e + h)
    p2 = strassen(d, g - e)       # p2 = d(g - e)
    p3 = strassen(a + b, h)       # p3 = (a + b)h
    p4 = strassen(b - d, g + h)   # p4 = (b - d)(g + h)
    p5 = strassen(a, f - h)       # p5 = a(f - h)
    p6 = strassen(c + d, e)       # p6 = (c + d)e
    p7 = strassen(a - c, e + f)   # p7 = (a - c)(e + f)
    
    C11 = p1 + p2 - p3 + p4
    C12 = p5 + p3
    C21 = p6 + p2
    C22 = p5 + p1 - p6 - p7
    
    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
    return C

def split(mat):
    n = mat.shape[0]
    mid = n // 2
    return mat[:mid, :mid], mat[:mid, mid:], mat[mid:, :mid], mat[mid:, mid:]

if __name__ == "__main__":
    A = np.array([[1, 2, 3, 4], 
                  [5, 6, 7, 8], 
                  [9, 10, 11, 12], 
                  [13, 14, 15, 16]])
    B = np.array([[17, 18, 19, 20], 
                  [21, 22, 23, 24], 
                  [25, 26, 27, 28], 
                  [29, 30, 31, 32]])
    
    C = strassen(A, B)
    print("Result of Strassen's algorithm:")
    print(C)