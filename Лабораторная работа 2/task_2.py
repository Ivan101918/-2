salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0  # фин подушка

for month in range(months):
    if month == 0:
        cur_spend = spend
    cur_spend = spend * (1 + increase) ** month  # с инфляцией
    money_capital += abs(salary - cur_spend)  # суммируем к подушке безопасности разницу между зп и тратами

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))
