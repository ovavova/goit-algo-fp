""" Необхідно написати програму на Python, яка використовує два підходи — жадібний алгоритм та алгоритм динамічного програмування для розв’язання задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.

Кожен вид їжі має вказану вартість і калорійність. Дані про їжу представлені у вигляді словника, де ключ — назва страви, а значення — це словник з вартістю та калорійністю.

Розробіть функцію greedy_algorithm жадібного алгоритму, яка вибирає страви, максимізуючи співвідношення калорій до вартості, не перевищуючи заданий бюджет.

Для реалізації алгоритму динамічного програмування створіть функцію dynamic_programming, яка обчислює оптимальний набір страв для максимізації калорійності при заданому бюджеті.

 """


import timeit
import matplotlib.pyplot as plt

# Дані про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items: dict, budget: int) -> dict:
    """
    Жадібний алгоритм:
    вибирає страви за максимальним співвідношенням calories/cost,
    не перевищуючи бюджет. Кожну страву можна взяти максимум 1 раз.
    """
    result = {}
    total_cost = 0
    total_calories = 0

    # Сортуємо страви за "вигодою": калорії / вартість (від більшого до меншого)
    sorted_items = sorted(
        items.items(),
        key=lambda x: x[1]["calories"] / x[1]["cost"],
        reverse=True
    )

    for name, info in sorted_items:
        if total_cost + info["cost"] <= budget:
            result[name] = 1
            total_cost += info["cost"]
            total_calories += info["calories"]

    return {
        "selected": result,
        "total_cost": total_cost,
        "total_calories": total_calories
    }

def dynamic_programming(items: dict, budget: int) -> dict:
    """
    Динамічне програмування (knapsack):
    знаходить оптимальний набір страв для максимуму калорій при бюджеті.
    """
    names = list(items.keys())
    n = len(names)

    # dp[i][b] = максимум калорій, якщо розглядаємо перші i страв і бюджет b
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Заповнюємо таблицю
    for i in range(1, n + 1):
        name = names[i - 1]
        cost = items[name]["cost"]
        calories = items[name]["calories"]

        for b in range(0, budget + 1):
            # варіант: не беремо страву i
            dp[i][b] = dp[i - 1][b]

            # варіант: беремо страву i, якщо влазить
            if b >= cost:
                dp[i][b] = max(dp[i][b], dp[i - 1][b - cost] + calories)

    # 
    selected = {}
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            name = names[i - 1]
            selected[name] = 1
            b -= items[name]["cost"]

    total_cost = sum(items[name]["cost"] for name in selected)
    total_calories = dp[n][budget]

    return {
        "selected": selected,
        "total_cost": total_cost,
        "total_calories": total_calories
    }

def compare_algorithms():
    # Бюджети для тестування
    test_budgets = range(10, 500, 20)

    greedy_times = []
    dp_times = []

    print(f"{'Budget':<10} | {'Greedy Time (s)':<20} | {'DP Time (s)':<20}")
    print("-" * 60)

    for budget in test_budgets:
        # запускаємо кілька разів і беремо сумарний час
        t_greedy = timeit.timeit(lambda: greedy_algorithm(items, budget), number=2000)
        t_dp = timeit.timeit(lambda: dynamic_programming(items, budget), number=2000)

        greedy_times.append(t_greedy)
        dp_times.append(t_dp)

        print(f"{budget:<10} | {t_greedy:.6f}             | {t_dp:.6f}")

    # Графіки
    plt.figure(figsize=(10, 6))
    plt.plot(test_budgets, greedy_times, label='Жадібний Алгоритм', marker='o')
    plt.plot(test_budgets, dp_times, label='Динамічне програмування', linestyle='--')

    plt.title('Тест швидкості: Жадібний vs Динамічне програмування (Food Selection)')
    plt.xlabel('Бюджет')
    plt.ylabel('Час виконання, секунди (сума з 2000 запусків)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Демонстрація на одному бюджеті (щоб побачити різницю в рішенні)
    budget = 150

    g = greedy_algorithm(items, budget)
    d = dynamic_programming(items, budget)

    print("\n=== DEMO (budget = 100) ===")
    print("Greedy:", g)
    print("DP    :", d)

    # Порівняння швидкості + графік
    compare_algorithms()