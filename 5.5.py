import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Визначаємо функцію f(x1, x2)
def f(x1, x2):
    return np.sin(x1) * np.sin(x2**2 / np.pi) + np.sin(x2) * np.sin(2 * x2**2 / np.pi)

# Метод випадкового пошуку для мінімуму та максимуму
def random_search(num_iterations=10000000):
    # Задаємо межі для x1 та x2
    x1_min, x1_max = 0, np.pi
    x2_min, x2_max = 0, np.pi
    
    # Ініціалізація випадкових початкових точок
    best_x1_min = random.uniform(x1_min, x1_max)
    best_x2_min = random.uniform(x2_min, x2_max)
    best_value_min = f(best_x1_min, best_x2_min)
    
    best_x1_max = best_x1_min
    best_x2_max = best_x2_min
    best_value_max = best_value_min
    
    # Цикл випадкового пошуку
    for _ in range(num_iterations):
        # Генерація нової випадкової точки
        x1 = random.uniform(x1_min, x1_max)
        x2 = random.uniform(x2_min, x2_max)
        
        # Обчислення значення функції у новій точці
        current_value = f(x1, x2)
        
        # Оновлення найкращого рішення для мінімуму
        if current_value < best_value_min:
            best_x1_min, best_x2_min = x1, x2
            best_value_min = current_value
        
        # Оновлення кращого рішення для максимуму
        if current_value > best_value_max:
            best_x1_max, best_x2_max = x1, x2
            best_value_max = current_value
    
    return (best_x1_min, best_x2_min, best_value_min), (best_x1_max, best_x2_max, best_value_max)

def plot_function_with_extrema(min_result, max_result):
    x1_vals = np.linspace(0, np.pi, 100)
    x2_vals = np.linspace(0, np.pi, 100)
    x1_grid, x2_grid = np.meshgrid(x1_vals, x2_vals)
    
    f_vals = f(x1_grid, x2_grid)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    ax.plot_surface(x1_grid, x2_grid, f_vals, cmap='viridis', alpha=0.8)

    ax.scatter(min_result[0], min_result[1], min_result[2], color='red', label='Минимум', s=100)
    ax.scatter(max_result[0], max_result[1], max_result[2], color='blue', label='Максимум', s=100)

    # Настройки графика
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_zlabel('f(x1, x2)')
    ax.set_title('Графік функції та точки мінімуму та максимуму')
    ax.legend()

    # Отображение графика
    plt.show()

min_result, max_result = random_search()

print(f"The minimum of the function found: f({min_result[0]:.4f}, {min_result[1]:.4f}) = {min_result[2]:.4f}")
print(f"The maximum of the function found: f({max_result[0]:.4f}, {max_result[1]:.4f}) = {max_result[2]:.4f}")

plot_function_with_extrema(min_result, max_result)