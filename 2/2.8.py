import math
import random
import timeit
pi_accurate = math.pi

def leibniz_method():
    n = 1000000
    pi_approx = 0
    for k in range(n):
        pi_approx += ((-1) ** k) / (2 * k + 1)
    pi_approx *= 4
    return pi_approx

def archimedes_method():
    sides = 6
    length = 1
    for k in range(10):
        sides *= 2
        length = math.sqrt(2 - 2 * math.sqrt(1 - (length / 2) ** 2))
    pi_approx = (length * sides) / 2
    return pi_approx

def monte_carlo_method():
    num_points = 1000000
    inside_circle = 0
    for k in range(num_points):
        x, y = random.random(), random.random()
        if x ** 2 + y ** 2 <= 1:
            inside_circle += 1
    pi_approx = (inside_circle / num_points) * 4
    return pi_approx

def test_methods():
    methods = [leibniz_method, archimedes_method, monte_carlo_method]
    for method in methods:
        result = method()
        error = abs(result - pi_accurate)
        print(f"Method: {method.__name__}, π = {result:.10f}, Error = {error:.10f}")

if __name__ == '__main__':
    test_methods()
    leibniz_time = timeit.timeit("leibniz_method()", globals=globals(), number=100)
    archimedes_time = timeit.timeit("archimedes_method()", globals=globals(), number=100)
    monte_carlo_time = timeit.timeit("monte_carlo_method()", globals=globals(), number=100)
    print(f"Time taken for 100 iterations:")
    print(f"Leibniz Method: {leibniz_time:.5f} seconds")
    print(f"Archimedes Method: {archimedes_time:.5f} seconds")
    print(f"Monte Carlo Method: {monte_carlo_time:.5f} seconds")
