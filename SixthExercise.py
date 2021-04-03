import numpy
import math


def simpson():
    def func(x):
        return math.sin(x)

    def simpsonMethod(x0, xn, n):
        h = (xn - x0) / n

        integration = func(x0) + func(xn)
        # N sub-intervals means N+1 points
        points = numpy.linspace(x0, xn, n+1)
        for i in range(1, n):
            if i % 2 == 0:
                integration = integration + 2 * func(points[i])
            else:
                integration = integration + 4 * func(points[i])

        integration = integration * h / 3
        return integration

    res = simpsonMethod(0, math.pi / 2, 10)
    print("Simpsons method result: ")
    print(res)


def trapezoidal():
    def func(x):
        return math.sin(x)

    def trapezoidalMethod(x0, xn, n):
        h = (xn - x0) / n
        integration = func(x0) + func(xn)
        # N sub-intervals means N+1 points
        points = numpy.linspace(x0, xn, n+1)
        for i in range(1, n):
            integration = integration + 2*func(points[i])

        res = h * integration * 0.5

        return res

    res = trapezoidalMethod(0, math.pi / 2, 10)
    print("Trapezoidal method result: ")
    print(res)


if __name__ == '__main__':
    simpson()
    trapezoidal()
