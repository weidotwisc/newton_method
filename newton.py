import math
# f is f(x)
# d is f'(x)
# x1 is init x value
# n is the desired precision
# x_(n+1) = x_(n)- f(x_n)/f'(x_n)
# return iteration number, and final solution, or print diverging
def newton(f, d, x1,n):
    x_old = x1
    x_new = x1
    calc_iter = 0
    while True:
        x_new = x_old - f(x_old)/d(x_old)
        if abs(x_new - x_old) < (10 ** ((-1)*n)):
            return calc_iter+1,x_new
        x_old = x_new
        calc_iter = calc_iter + 1
        print("i:", calc_iter, " val:", x_old)
        if(calc_iter > 100):
            return calc_iter, math.inf 

# Stewart 3.8.11
f = lambda x: x**4-75
d = lambda x: 4* (x**3)
x1 = 3
n = 8

# Stewart 3.8.13
f = lambda x: 3*x**4 - 8*x**3 + 2
d = lambda x: 12*x**3 - 24*x**2
x1 = 3 # note when x1=2 there is a divison by zero error
n = 6

# Stewart 3.8.15
f = lambda x: x**2 - math.sin(x)
d = lambda x: 2*x - math.cos(x)
x1 = 1 
n = 6

# Stewart 3.8.17
f = lambda x: x+1-3*math.cos(x)
d = lambda x: 1 + 3*math.sin(x)
x1 = 1.57
x1 = -2
x1 = -4
n = 6

# Stewart 3.8.19
f = lambda x: x ** (1/3) - 1 - 1/x
d = lambda x: (1/3)*x**(-2/3) + x ** (-2)
x1 = 3
n = 6


# Stewart 3.8.21
f = lambda x: math.cos(x) - x ** 3 
d = lambda x: -1*math.sin(x) - 3 * (x**2)
x1 = 1.57
n = 6

# Stewart 3.8.23
f = lambda x: -2*(x**7)-5*(x**4)+9*(x**3)+5
d = lambda x: -14*(x**6)-20*(x**3)+27*(x**2)
x1 = 1
x1 = -1
x1 = -2
n = 8

# Stewart 3.8.25
f = lambda x: x/(x**2+1)-math.sqrt(1-x)
d = lambda x: (1-x**2)/((1+x**2)**2) + 0.5/(math.sqrt(1-x))
x1 = 0.5
n = 8

# Stewart 3.8.27
f = lambda x: x**2-1000
d = lambda x: 2*x
x1 = 30
n = 6

# Stewart 3.8.30
f = lambda x: x**3-x-1
d = lambda x: 3*(x**2)-1
x1 = 1
x1 = 0.6
x1 = 0.57
n = 6

# Stewart 3.8.31
f = lambda x: x**(1/3)
d = lambda x: (1/3)*(x**(-2/3))
x1 = 1
n = 6

# Stewart 3.8.33
f = lambda x: 6*(x**5)-4*(x**3)+9*(x**2)-2
d = lambda x: 30*(x**4)-12*(x**2)+18*x
x1 = -1.3
x1 = -0.5
x1 = 0.5
n = 6

# Stewart 3.8.35
f = lambda x: 2*math.sin(x)+4*x*math.cos(x)-x**2*math.sin(x)
d = lambda x: 6*math.cos(x) - 6*x*math.sin(x)-x**2*math.cos(x)
x1 = 0
x1 = 1.5
n = 6

# Stewart 3.8.35
f = lambda x: 2*x+4*((x-1)**3)
d = lambda x: 2+12*((x-1)**2)
x1 = 0.5
n = 6

# Stewart 3.8.39
f = lambda x: 48*x*(1+x)**60-(1+x)**60+1
d = lambda x: 48*(1+x)**60+60*((1+x)**59)*(48*x-1)
x1 = 0.1
n = 6


iter_num, sol = newton(f, d, x1, n)
print("i:", iter_num, " val:", sol)
if iter_num <= 100:
    print("Solution:", round(sol, n))
else:
    print("Diverged w/ ", x1)
