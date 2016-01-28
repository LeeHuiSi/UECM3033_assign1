import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate(3*(x**2)*sy.sqrt(1-8*(x**3)), (x,-2,0))
    return ans

def my_solution():
    A = np.array( [[10,9,8,7,6,5,4,3,2,1],
                   [8,7,0,2,5,6,7,7,8,9],
                   [3,7,12,35,6,44,23,41,17,10],
                   [5,6,7,1,2,3,5,2,9,0],
                   [3,2,1,0,9,7,8,6,5,4],
                   [3,7,3,5,4,4,6,7,8,2],
                   [0,1,6,4,4,2,5,5,0,3],
                   [3,3,0,5,3,2,3,1,6,7],
                   [9,7,7,9,6,5,6,6,4,5],
                   [4,5,6,4,5,6,4,5,6,4]
                   ] )
    b = np.array([220,358,1229,202,286,280,173,209,316,271])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1003608
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
