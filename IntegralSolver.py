import scipy.integrate as integrate
import numpy as np

def f(x):
    return(1 / (np.sqrt(x)))

def calc_error(true_value, measured_value):
    return (abs(measured_value - true_value) / true_value) * 100

def calc_integral(function, lower_bound, upper_bound, step_count):
    percent = "%"
    steps = np.linspace(lower_bound, upper_bound, step_count + 1)
    integral = integrate.quad(function, lower_bound, upper_bound)[0]
    integral_trapezoidal = integrate.trapezoid([function(x) for x in steps], dx = (upper_bound - lower_bound) / step_count)
    integral_simpsons = integrate.simpson([function(x) for x in steps], dx = (upper_bound - lower_bound) / step_count)
    print("Integral of f(x): {0}".format(integral))
    print("Integral of f(x) using trapezoidal rule: {0} with {1}{2} error".format(integral_trapezoidal, calc_error(integral, integral_trapezoidal), percent))
    print("Integral of f(x) using Simpson's rule: {0} with {1}{2} error".format(integral_simpsons, calc_error(integral, integral_simpsons), percent))

lower_bound = int(input("Lower bound: "))
upper_bound = int(input("Upper bound: "))
steps = int(input("Steps: "))
calc_integral(f, lower_bound, upper_bound, steps)