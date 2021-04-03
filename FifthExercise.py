import numpy
import matplotlib.pyplot as plt
from numpy.linalg import inv
from sklearn.metrics import mean_squared_error


def polynomialApproach(input):
    inputAltered = input
    m = 10
    x = [-3, -2, -0.4, -0.1, 0.8, 1, 1.6, 2, 3, 3.14]
    y = numpy.sin(x)

    def poly(x, y, n):
        sum = y[0]
        temp = numpy.zeros((m, m))

        for i in range(0, m):
            temp[i, 0] = y[i]
        temp_sum = 1.0

        # Calculate the sum for each point.
        for i in range(1, m):
            temp_sum = temp_sum * (n - x[i - 1])
            for j in range(i, m):
                temp[j, i] = (temp[j, i - 1] - temp[j - 1, i - 1]) / (x[j] - x[j - i])
            sum += temp_sum * temp[i, i]

        return sum

    # Convert x to [-pi, pi]
    if (input >= numpy.pi or input <= -numpy.pi):
        inputAltered = input % numpy.pi

    xnew = numpy.zeros(1)
    xnew[0] = inputAltered
    ynew = []
    for i in xnew:
        ynew.append(poly(x, y, i))

    print("The approximation of sin(%f)" % input + " with Newtons method is:")
    print(ynew[0])



def splines(input):
    inputAltered = input
    n = 10
    a = numpy.zeros(n - 1)
    delta = numpy.zeros(n - 1)
    Delta = numpy.zeros(n - 1)
    d = numpy.zeros(n - 1)
    b = numpy.zeros(n - 1)
    A = numpy.zeros((n, n))
    B = numpy.zeros(n)
    A[0][0] = 1
    A[n - 1][n - 1] = 1

    x = [-3, -2, -0.4, -0.1, 0.8, 1, 1.6, 2, 3, 3.14]
    y = numpy.sin(x)

    for i in range(n - 1):
        a[i] = y[i]
        delta[i] = x[i + 1] - x[i]
        Delta[i] = y[i + 1] - y[i]

    for i in range(1, n - 1):
        A[i, i] = 2 * (delta[i - 1] + delta[i])
        A[i, i - 1] = delta[i - 1]
        A[i, i + 1] = delta[i]
        B[i] = 3 * ((Delta[i] / delta[i]) - (Delta[i - 1] / delta[i - 1]))

    # Inbuilt numpy function to get the solution of a linear system
    c = numpy.linalg.solve(A, B)

    for i in range(n - 1):
        d[i] = (c[i + 1] - c[i]) / (3 * delta[i])
        b[i] = (Delta[i] / delta[i]) - (delta[i] * (2 * c[i] + c[i + 1]) / 3)

    # Convert x to [-pi, pi]
    if (input >= numpy.pi or input <= -numpy.pi):
        inputAltered = input % numpy.pi

    xnew = numpy.linspace(-numpy.pi, numpy.pi, 200)
    xnew[0] = inputAltered

    ynew = numpy.zeros(1)
    m = 0
    for i in range(1):
        for j in range(n - 1):
            if (xnew[i] >= x[j] and xnew[i] < x[j + 1]):
                m = j
                break
            elif (xnew[i] == x[n - 1]):
                m = n - 1
        ynew[i] = a[m] + b[m] * (xnew[i] - x[m]) + c[m] * ((xnew[i] - x[m]) ** 2) + d[m] * ((xnew[i] - x[m]) ** 3)

    print("The approximation of sin(%f)" % input + " with Splines method is:")
    print(ynew[0])



def leastSquares(input):
    inputAltered = input
    x = [-3, -2, -0.4, -0.1, 0.8, 1, 1.6, 2, 3, 3.14]
    y = numpy.sin(x)
    A = numpy.zeros((len(x), 5))
    b = numpy.zeros(len(x))

    # Filling the two arrays accordingly
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

    # Calculating transpose and inverse matrices
    transposeA = A.transpose()
    A_Atranspose = numpy.dot(transposeA, A)
    inverseA_Atranspose = inv(A_Atranspose)

    Atranspose_b = numpy.dot(transposeA, b)

    # Inbuilt numpy func for matrix multiplication
    c = numpy.dot(inverseA_Atranspose, Atranspose_b)

    # Convert x to [-pi, pi]
    if (input >= numpy.pi or input <= -numpy.pi):
        inputAltered = input % numpy.pi

    xnew = numpy.zeros(1)
    xnew[0] = inputAltered
    ynew = numpy.zeros(1)
    j = 0
    for i in range(1):
        ynew[i] = c[j] + c[j+1]*xnew[i] + c[j+2]*xnew[i]**2 + c[j+3]*xnew[i]**3 + c[j+4]*xnew[i]**4

    print("The approximation of sin(%f)" % input + " with least squares method is:")
    print(ynew[0])

if __name__ == '__main__':
    # Enter the desired x to calculate its sin.
    polynomialApproach(14)
    splines(14)
    leastSquares(14)
