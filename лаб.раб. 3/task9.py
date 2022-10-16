salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
# money = 0 # расходы второго месяца
summ = spend
for i in range (2, months + 1):
spend = spend * 1.03
summ = summ + spend
(summ - salary * months) // 1 + 1
print(round(need_money))