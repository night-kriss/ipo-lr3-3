# Ввод данных от пользователя
day = int(input("Введите день: "))
month = int(input("Введите месяц: "))
# Функция для определения сезона
def determine_season(day, month):
    if (month == 3 and day >= 1) or (month == 4) or (month == 5) or (month == 6 and day <= 20):
        return "Весна"
    elif (month == 6 and day >= 21) or (month == 7) or (month == 8) or (month == 9 and day <= 22):
        return "Лето"
    elif (month == 9 and day >= 23) or (month == 10) or (month == 11) or (month == 12 and day <= 20):
        return "Осень"
    else:
        return "Зима"

# Ввод данных от пользователя
day = int(input("Введите день: "))
month = int(input("Введите месяц: "))

# Определение и вывод сезона
season = determine_season(day, month)
print(f"Время года: {season}")