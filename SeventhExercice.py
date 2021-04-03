from numpy.linalg import inv
import numpy



def leastSquares4():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [2.1300, 2.1600, 2.1450, 2.0400, 2.0920, 2.1220, 2.2500, 2.2500, 2.2540, 2.2610]
    A = numpy.zeros((len(x), 5))
    b = numpy.zeros(len(x))

    for i in range(len(x)):
        for j in range(5):
            if (j == 0):
                A[i, j] = 1
            elif (j == 1):
                A[i, j] = x[i]
            elif (j == 2):
                A[i, j] = x[i] ** 2
            elif (j == 3):
                A[i, j] = x[i] ** 3
            elif (j == 4):
                A[i, j] = x[i] ** 4
        b[i] = y[i]

    transposeA = A.transpose()
    A_Atranspose = numpy.dot(transposeA, A)
    inverseA_Atranspose = inv(A_Atranspose)

    Atranspose_b = numpy.dot(transposeA, b)

    c = numpy.dot(inverseA_Atranspose, Atranspose_b)

    xnew = numpy.zeros(1)
    xnew[0] = 15
    ynew = numpy.zeros(1)
    j = 0
    for i in range(1):
        ynew[i] = c[j] + c[j+1]*xnew[i] + c[j+2]*xnew[i]**2 + c[j+3]*xnew[i]**3 + c[j+4]*xnew[i]**4

    print("Approximation with fourth grade polynomial:")
    print(ynew[0])



def leastSquares3():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [2.1300, 2.1600, 2.1450, 2.0400, 2.0920, 2.1220, 2.2500, 2.2500, 2.2540, 2.2610]
    A = numpy.zeros((len(x), 4))
    b = numpy.zeros(len(x))

    for i in range(len(x)):
        for j in range(4):
            if (j == 0):
                A[i, j] = 1
            elif (j == 1):
                A[i, j] = x[i]
            elif (j == 2):
                A[i, j] = x[i] ** 2
            elif (j == 3):
                A[i, j] = x[i] ** 3
        b[i] = y[i]

    transposeA = A.transpose()
    A_Atranspose = numpy.dot(transposeA, A)
    inverseA_Atranspose = inv(A_Atranspose)

    Atranspose_b = numpy.dot(transposeA, b)

    c = numpy.dot(inverseA_Atranspose, Atranspose_b)

    xnew = numpy.zeros(1)
    xnew[0] = 15
    ynew = numpy.zeros(1)
    j = 0
    for i in range(1):
        ynew[i] = c[j] + c[j+1]*xnew[i] + c[j+2]*xnew[i]**2 + c[j+3]*xnew[i]**3

    print("Approximation with cubic polynomial:")
    print(ynew[0])


def leastSquares2():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [2.1300, 2.1600, 2.1450, 2.0400, 2.0920, 2.1220, 2.2500, 2.2500, 2.2540, 2.2610]
    A = numpy.zeros((len(x), 3))
    b = numpy.zeros(len(x))

    for i in range(len(x)):
        for j in range(3):
            if (j == 0):
                A[i, j] = 1
            elif (j == 1):
                A[i, j] = x[i]
            elif (j == 2):
                A[i, j] = x[i] ** 2
        b[i] = y[i]

    transposeA = A.transpose()
    A_Atranspose = numpy.dot(transposeA, A)
    inverseA_Atranspose = inv(A_Atranspose)

    Atranspose_b = numpy.dot(transposeA, b)

    c = numpy.dot(inverseA_Atranspose, Atranspose_b)

    xnew = numpy.zeros(1)
    xnew[0] = 15
    ynew = numpy.zeros(1)
    j = 0
    for i in range(1):
        ynew[i] = c[j] + c[j+1]*xnew[i] + c[j+2]*xnew[i]**2

    print("Approximation with square polynomial:")
    print(ynew[0])



if __name__ == '__main__':
    leastSquares4()
    leastSquares3()
    leastSquares2()