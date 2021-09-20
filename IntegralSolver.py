import scipy.integrate as integrate
import numpy as np

def f(x):
    return(1 / (np.sqrt(x)))

def calc_error(true_value, measured_value):
    return (abs(measured_value - true_value) / true_value) * 100

def calc_integral(function, lower_bound, upper_bound, step_count):
    percent = "%"
    steps = np.linspace(lower_bound, upper_bound, step_count + 1)
    dx = (upper_bound - lower_bound) / step_count
    mram = []
    for i in range(len(steps) - 1):
        mram.append((steps[i] + steps[i + 1]) / 2)
    integral = integrate.quad(function, lower_bound, upper_bound)[0]
    integral_trapezoidal = integrate.trapezoid([function(x) for x in steps], dx = dx)
    integral_simpsons = integrate.simpson([function(x) for x in steps], dx = dx)
    integral_lram = np.sum([function(x) * dx for x in steps[:step_count]])
    integral_rram = np.sum([function(x) * dx for x in steps[1:]])
    integral_mram = np.sum([function(x) * dx for x in mram])
    print("Integral of f(x): {0}".format(integral))
    print("Integral of f(x) using trapezoidal rule: {0} with {1}{2} error".format(integral_trapezoidal, calc_error(integral, integral_trapezoidal), percent))
    print("Integral of f(x) using Simpson's rule: {0} with {1}{2} error".format(integral_simpsons, calc_error(integral, integral_simpsons), percent))
    print("Integral of f(x) using LRAM: {0} with {1}{2} error".format(integral_lram, calc_error(integral, integral_lram), percent))
    print("Integral of f(x) using RRAM: {0} with {1}{2} error".format(integral_rram, calc_error(integral, integral_rram), percent))
    print("Integral of f(x) using MRAM: {0} with {1}{2} error".format(integral_mram, calc_error(integral, integral_mram), percent))

lower_bound = int(input("Lower bound: "))
upper_bound = int(input("Upper bound: "))
steps = int(input("Steps: "))
calc_integral(f, lower_bound, upper_bound, steps)