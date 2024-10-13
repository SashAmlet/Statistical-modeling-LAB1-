import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare

# Моделюємо підкидання двох кубиків
def simulate_two_dice_rolls(n_rolls):
    dice1 = np.random.randint(1, 7, size=n_rolls)
    dice2 = np.random.randint(1, 7, size=n_rolls)
    return dice1 + dice2

# Теоретичний розподіл суми двох кубиків
def theoretical_distribution():
    # Якими комбінаціями можуть випасти наступні суми:
    # 2 - (1,1) 
    # 3 - (1,2), (2,1) 
    # 4 - (1,3), (3,1), (2,2) 
    # 5 - (1,4), (4,1), (2,3), (3,2) 
    # 6 - (1,5), (5,1), (2,4), (4,2), (3,3)
    # 7 - (1,6), (6,1), (2,5), (5,2), (3,4), (4,3) 
    # 8 - (2,6), (6,2), (3,5), (5,3), (4,4) 
    # 9 - (3,6), (6,3), (4,5), (5,4) 
    # 10 - (4,6), (6,4), (5,5) 
    # 11 - (5,6), (6,5) 
    # 12 - (6,6)
    # Кількість способів отримати кожну суму від 2 до 12
    probabilities = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
    total_ways = 36  # Усього 6 * 6 = 36 способів підкидання двох кубиків
    return np.array(probabilities) / total_ways

# Проводимо обчислювальний експеримент та будуємо розподіл
n_rolls = 1000
rolls = simulate_two_dice_rolls(n_rolls)

# Оцінюємо частоти отриманих сум
observed_frequencies = np.bincount(rolls, minlength=13)[2:]  # суми від 2 до 12
# Реальні ймовірності для кожної суми
observed_probabilities = observed_frequencies / n_rolls

# Теоретичні ймовірності для кожної суми
theoretical_probabilities = theoretical_distribution()

# Перевірка гіпотези chi^2
chi2_stat, p_value = chisquare(f_obs=observed_frequencies, f_exp=theoretical_probabilities * n_rolls)

# Виведення результатів
print(f"Frequencies observed: {observed_frequencies}")
print(f"Theoretical probabilities: {theoretical_probabilities}")
print(f"The value of the chi^2 statistic: {chi2_stat:.2f}, p-value: {p_value:.4f}")


# Побудова гістограми
x = np.arange(2, 13)
plt.bar(x - 0.2, observed_probabilities, width=0.4, label='Experimental frequencies')
plt.bar(x + 0.2, theoretical_probabilities, width=0.4, label='Theoretical probabilities')
plt.xlabel('The sum of two cubes')
plt.ylabel('Frequency')
plt.title('Distribution of the sum of two dice')
plt.legend()
plt.show()
