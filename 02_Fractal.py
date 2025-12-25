""" Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії



Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала “дерево Піфагора”. Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен мати можливість вказати рівень рекурсії. """



import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


def draw_square(ax, A, B, linewidth=0.6):
    """
    Малює квадрат, побудований на відрізку A->B (A,B — complex).
    Квадрат будується "вліво" від напрямку A->B (вгору, якщо A->B вздовж +X).
    Повертає вершини (A,B,C,D).
    """
    v = B - A
    # Поворот на +90°: множимо на 1j
    C = B + v * 1j
    D = A + v * 1j

    poly = Polygon(
        [(A.real, A.imag), (B.real, B.imag), (C.real, C.imag), (D.real, D.imag)],
        closed=True, fill=False, linewidth=linewidth
    )
    ax.add_patch(poly)
    return A, B, C, D


def pythagoras_tree(ax, A, B, level, theta=np.pi / 4):
    """
    Рекурсивно будує дерево Піфагора.
    A->B — нижня сторона квадрата.
    level — глибина рекурсії.
    theta — кут "розгалуження" (класичний варіант: 45°).
    """
    A, B, C, D = draw_square(ax, A, B)

    if level == 0:
        return

    # Верхня сторона квадрата: D -> C (це "гіпотенуза" для трикутника)
    h = C - D

    # Точка E — вершина прямокутного трикутника на гіпотенузі D->C
    # DE має довжину |h|*cos(theta) і напрямок h, повернутий на theta
    E = D + h * np.cos(theta) * np.exp(1j * theta)

    # Два нових квадрати будуються на "катетах" D->E та E->C
    pythagoras_tree(ax, D, E, level - 1, theta)
    pythagoras_tree(ax, E, C, level - 1, theta)


def main():
    while True:
        try:
            level = int(input("Введіть рівень рекурсії (0-12): "))
            if not (0 <= level <= 12):
                raise ValueError("Рівень має бути від 0 до 12.")
            break
        except ValueError as e:
            print("Помилка:", e)

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect("equal")
    ax.axis("off")

    # Базовий квадрат (старт)
    A = 0 + 0j
    B = 1 + 0j

    pythagoras_tree(ax, A, B, level=level, theta=np.pi / 4)

    # Трохи “поля”, щоб нічого не обрізалось
    ax.relim()
    ax.autoscale_view()
    plt.show()


if __name__ == "__main__":
    main()