import random
from math import sin

def function(x):
    return x**2 + 4*x * sin(x)

def montecarlo_integration(a, b, num_samples):
    integral = 0
    for k in range(num_samples):
        x = random.uniform(a, b)  
        integral += function(x)
    
    integral *= (b - a) / num_samples  
    return integral

a = 2  
b = 3 
num_samples = 1000000  
    
result = montecarlo_integration(a, b, num_samples)
print(result)
