import numpy as np
from tabulate import tabulate

def Walds_criterion(mat):
    MIN = []
    for i in range(0, len(mat)):
        MIN.append(min(mat[i]))
    return MIN, [max(MIN), MIN.index(max(MIN))+1]

def Maximum_criterion(mat):
    MAX = []
    for i in range(0, len(mat)):
        MAX.append(max(mat[i]))
    return MAX, [max(MAX), MAX.index(max(MAX))+1]

def Laplace_criterion(mat):
    SUM = []
    for i in range(0, len(mat)):
        SUM.append(np.sum(mat[i]) / 3)
    return SUM, [np.around(max(SUM), 2), SUM.index(max(SUM))+1]

def Hurwitz_criterion(mat):
    y = 0.75
    MIN = []
    MAX = []
    for i in range(0, len(mat)):
        MIN.append(min(mat[i]))
        MAX.append(max(mat[i]))
    S = []
    for i in range(0, len(mat)):
        count = y * MIN[i] + (1 - y) * MAX[i]
        S.append(count)
    return S, [np.around(max(S), 2), S.index(max(S))+1]

def Bayes_Laplace_criterion(mat):
    p = [0.5, 0.35, 0.15]
    S = []
    for i in range(0, len(mat)):
        count = 0
        for j in range(0, len(mat[i])):
            count += p[j] * mat[i][j]
        S.append(count)
    return S, [np.around(max(S), 2), S.index(max(S))+1]
    
mat = np.loadtxt("laboratorna 1.txt", dtype=int)

Walds_all, Walds = Walds_criterion(mat)
Walds_all.insert(0, "Максимальні значення для критерію Вальда")
Walds.insert(0, "Критерій Вальда")

Maximum_all, Maximum = Maximum_criterion(mat)
Maximum_all.insert(0, "Максимальні значення для критерію Максимуму")
Maximum.insert(0, "Критерій Максимуму")

Laplace_all, Laplace = Laplace_criterion(mat)
Laplace_all.insert(0, "Максимальні значення для критерію Лапласа")
Laplace.insert(0, "Критерій Лапласа")

Hurwitz_all, Hurwitz = Hurwitz_criterion(mat)
Hurwitz_all.insert(0, "Максимальні значення для критерію Гурвіца")
Hurwitz.insert(0, "Критерій Гурвіца")

Bayes_Laplace_all, Bayes_Laplace = Bayes_Laplace_criterion(mat)
Bayes_Laplace_all.insert(0, "Максимальні значення для критерію Байєса-Лапласа")
Bayes_Laplace.insert(0, "Критерій Байєса-Лапласа")

show_mat = tabulate(mat, tablefmt='fancy_grid')
print("Зчитана матриця:")
print(show_mat)

header_all = ['Максимальні значення', 'Для першого\nрядка матриці', 'Для другого\nрядка матриці', 'Для третього\nрядка матриці']
table_all = [header_all, Walds_all, Maximum_all, Laplace_all, Hurwitz_all, Bayes_Laplace_all]
show_all = tabulate(table_all, headers='firstrow', tablefmt='fancy_grid', showindex=range(1, len(table_all)), colalign=("center", "center"))
print("Розрахункова таблиця:")
print(show_all)

header = ["Критерії", "Максимальні\nзначення", "Номер вибраної\nстратегії"]
table = [header, Walds, Maximum, Laplace, Hurwitz, Bayes_Laplace]
show = tabulate(table, headers='firstrow', tablefmt='fancy_grid', showindex=range(1, len(table)), colalign=("center", "center"))
print("Таблиця результатів: ")
print(show)

strategy = []
for i in range(1, len(table)):
    strategy.append(table[i][2])
strategy_best = max(set(strategy), key = strategy.count)
print("Найкраща стратегія в результаті усіх критеріїв:", strategy_best)
