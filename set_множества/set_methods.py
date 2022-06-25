"""
set.union(other)                Объединение.           Возвращает множество, состоящее из элементов set и other.
set.intersection(other)	        Пересечение.           Возвращает множество, состоящее из элементов, которые встречаются и в set, и в other.
set.difference(other)	        Разность.	           Возвращает множество элементов set, которые не встречаются в other.
set.symmetric_difference(other) Симметричная разность. Возвращает множество элементов, встречающиеся в одном из множеств, но не в обоих одновременно.
"""

abons = {"Иванов", "Петров", "Васильев", "Антонов"}

debtors = {"Петров", "Антонов"}

non_debtors = abons.difference(debtors)
print(non_debtors)


#################

a = input("Введите первую строку: ")
b = input("Введите вторую строку: ")

a_set, b_set = set(a), set(b) # используем множественное присваивание

a_and_b = a_set.intersection(b_set)

print(a_and_b)
