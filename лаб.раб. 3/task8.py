money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

spend_1 = money_capital + salary - spend # остаток за первый месяц
a = spend * increase # ежемесячный рост цен
spend_2 = spend_1 + salary - (a + spend) # остаток за второй месяц
b = spend_2 * increase # ежемесячный рост цен
spend_3 = spend_2 + salary - (spend_2 + b) # остаток за третий месяц
c = spend_3 * increase # ежемесячный рост цен
spend_4 = spend_3 + salary - (spend_3 + с) # остаток за четвертый месяц
d = spend_4 * increase # ежемесячный прирост цен
spend_5 = spend_4 + salary - (spend_4 + c) # остаток за пятый месяц

print(month)
