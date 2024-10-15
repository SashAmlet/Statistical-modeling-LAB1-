import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def monte_carlo_integration(n, num_points=10000000):
    # Генерація випадкових точок з експоненційного розподілу
    x_random = np.random.exponential(1, num_points)
    
    # Обчислення значень функції f(x) = x^(n-1)
    f_values = x_random**(n - 1)
    
    # Середнє значення функції
    integral_estimate = np.mean(f_values)
    
    return integral_estimate


n_values = np.arange(1/2, 25/2 + 0.1, 0.5)  # від 1/2 до 25/2 з кроком 0.5

def integrand(x, n):
    return x**(n-1) * np.exp(-x)

analytical_results = [quad(integrand, 0, np.inf, args=(n))[0] for n in n_values]

monte_carlo_results = [monte_carlo_integration(n) for n in n_values]

# Виведення результатів
for n, integral in zip(n_values, monte_carlo_results):
    print(f"F({n:.1f}) = {integral:.6f}")

# Построение графика
plt.figure(figsize=(10, 6))
plt.bar(n_values - 0.1, monte_carlo_results, width=0.2, label='Monte Carlo', alpha=0.7)
plt.bar(n_values + 0.1, analytical_results, width=0.2, label='Analytical', alpha=0.7)
plt.xlabel('n values')
plt.ylabel('Integral Value')
plt.title('Monte Carlo Integration vs Analytical Solution')
plt.xticks(n_values)
plt.legend()
plt.grid()
plt.show()
