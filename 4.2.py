import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_integration(x, num_points):
    y_random = np.random.uniform(0, 1, num_points)
    
    x_random = np.random.uniform(0, x, num_points)
    
    # Обчислення значень функції f(u) = e^(-u^2/2)
    f_x = np.exp(-x_random**2 / 2)
    
    # Підрахунок кількості точок під графіком
    points_under_curve = np.sum(y_random < f_x)
    
    # Наближене значення інтегралу
    integral_estimate = (points_under_curve / num_points) * x
    
    return integral_estimate


x_values = [.1, .2, .4, .6, .8]
num_points = 10000000

# Обчислення значень функції f(x) у заданих точках
f_values = []
for x in x_values:
    integral_value = monte_carlo_integration(x, num_points) * 1/(np.sqrt(2 * np.pi))
    f_values.append(integral_value)

# Виведення результатів
for x, f in zip(x_values, f_values):
    print(f"f({x}) = {f:.6f}")

# Побудова графіка
x_plot = np.linspace(min(x_values), max(x_values), 500)


plt.plot(x_values, f_values, label='Approximation of f(x) using the Monte Carlo method', color='blue', marker='o')
plt.scatter(x_values, f_values, color='red', zorder=5, label='Calculated values')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Calculating the integral using the Monte Carlo method')
plt.xlim(min(x_values), max(x_values))
plt.legend()
plt.grid()
plt.show()
