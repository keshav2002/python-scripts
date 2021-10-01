import math
import numpy
import matplotlib.pyplot as plt

def F(f):
    return (0.04 - (f/(1-f))*(math.sqrt(7/(2+f))))

def dF(f):
    return -1 * ((1.32288 * (f ** 2) + 1.32288 * f + 5.2915)/(((f-1) ** 2) * ((f+2) ** 1.5)))

def newtonRaphson(x0, e, N):
    print('\n\n*** NEWTON RAPHSON METHOD IMPLEMENTATION ***')
    step = 1
    flag = 1
    condition = True
    while condition:
        if dF(x0) == 0.0:
            print('Divide by zero error!')
            break

        prev_x0 = x0
        x1 = x0 - F(x0)/dF(x0)
        print('Iteration-%d, f = %0.7f and F(f) = %0.7f' % (step, x1, F(x1)))
        epochs.append(step)
        x1_val.append(x1)
        fx_val.append(F(x1))

        x0 = x1
        step = step + 1

        if step > N:
            flag = 0
            break

        # uncomment this if you want function value to be within error
        # condition = abs(f(x1)) > e
        print(f'Error: {abs(x1 - prev_x0)}')

        error_val.append(abs(x1 - prev_x0))

        # here, root value is considered for error
        condition = abs(x1 - prev_x0) > e and F(x1) != 0 and abs(F(x1)) > e

    if flag == 1:
        print('\nRequired root is: %0.8f' % x1)
    else:
        print('\nNot Convergent.')


# Initial guess
x0 = 0.1
# Error
e = 1e-6
# Max iterations
N = 10

# fill the lists
epochs = []
x1_val = []
fx_val = []
error_val = []

x1_val.append(x0)
fx_val.append(F(x0))
error_val.append(x0)
epochs.append(0)

# Starting Newton Raphson Method
newtonRaphson(x0, e, N)

plt.scatter(x1_val, fx_val, s=20, marker='x')
plt.plot(x1_val, fx_val)

# naming the x axis
plt.xlabel('f')
# naming the y axis
plt.ylabel('F(f)')
# giving a title to my graph
plt.title(f'Newton method f0 = {x0}')

plt.figure()
plt.plot(epochs, error_val)
plt.title(f'Newton method f0 = {x0}')
plt.xlabel('Epochs')
plt.ylabel('Error')

plt.show()