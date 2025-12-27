""" Завдання 7. Використання методу Монте-Карло
Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на кубиках, і визначає ймовірність кожної можливої суми.

Створіть симуляцію, де два кубики кидаються велику кількість разів. Для кожного кидка визначте суму чисел, які випали на обох кубиках. Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції. Використовуючи ці дані, обчисліть імовірність кожної суми.

На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.

Таблиця ймовірностей сум при киданні двох кубиків виглядає наступним чином.

Порівняйте отримані за допомогою методу Монте-Карло результати з аналітичними розрахунками, наведеними в таблиці вище.

 """

import numpy as np
import matplotlib.pyplot as plt

# ---- Monte Carlo для двох кубиків  ----
def monte_carlo_dice(num_rolls=100000):

    np.random.seed(42)

    # 1 Генеруємо кидки двох кубиків (1-6)
    d1 = np.random.randint(1, 7, size=num_rolls)
    d2 = np.random.randint(1, 7, size=num_rolls)

    # 2 Рахуємо суми
    sums = d1 + d2  # 2 до 12

    # 3 Підрахунок частот кожної суми (2-12)
    counts_full = np.bincount(sums, minlength=13)  # індекси 0-12
    counts = counts_full[2:13]  # беремо тільки 2-12
    probs = counts / num_rolls

    return sums, counts, probs


def analytic_probs_two_dice():
    # Кількість комбінацій для сум 2..12: 1,2,3,4,5,6,5,4,3,2,1 (всього 36) - з наведоної таблиці в завданні 
    comb_counts = np.array([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1], dtype=float)
    return comb_counts / 36.0

if __name__ == "__main__":
    N = 20000  # кількість симуляцій
    sums, mc_counts, mc_probs = monte_carlo_dice(num_rolls=N)

    # Аналітика
    th_probs = analytic_probs_two_dice()

    # ---- Таблиця порівняння ----
    print(f"Monte Carlo simulation for two dice: N = {N}\n")
    header = f"{'Sum':>3} | {'MC count':>8} | {'MC prob':>9} | {'Theory':>9} | {'Abs err':>9} | {'Rel err %':>9}"
    print(header)
    print("-" * len(header))

    sums_values = np.arange(2, 13)
    abs_err = np.abs(mc_probs - th_probs)
    rel_err = np.where(th_probs > 0, abs_err / th_probs * 100, 0)

    for i, s in enumerate(sums_values):
        print(f"{s:>3} | {int(mc_counts[i]):>8} | {mc_probs[i]:>9.5f} | {th_probs[i]:>9.5f} | {abs_err[i]:>9.5f} | {rel_err[i]:>9.2f}")

    # ---- Графік ----
    fig, ax = plt.subplots(figsize=(10, 6))

    x = sums_values
    width = 0.38

    ax.bar(x - width/2, mc_probs, width=width, label="Monte Carlo")
    ax.bar(x + width/2, th_probs, width=width, label="Теоретичні - розраховані значення")

    ax.set_xticks(x)
    ax.set_xlabel("Сума з двох кубиків")
    ax.set_ylabel("Probability-Вирогідність")
    ax.set_title(f"Вирогідність значень киждання двох кубиків: Monte Carlo та Аналітичні (N={N})")
    ax.grid(True, axis="y", alpha=0.3)
    ax.legend()

    plt.show()
