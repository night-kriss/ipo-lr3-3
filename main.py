# Ввод данных от пользователя
day = int(input("Введите день: ")) #Ввод дня
month = int(input("Введите месяц: ")) #Ввод месяца
#определение сезона
if (month == 3 and day >= 1 and day <=31) or (month == 4 and day >= 1 and day <=30) or (month == 5 and day >= 1 and day <=31) :
    season = "Весна" 
elif (month == 6 and day >= 1 and day <=30) or (month == 7 and day >= 1 and day <=31) or (month == 8 and day >= 1 and day <=31) :
    season = "Лето"
elif (month == 9 and day >= 1 and day <=30) or (month == 10 and day >= 1 and day <=31 ) or (month == 11 and day >=1 and day <=30 ):
    season = "Осень"
elif (month == 1 and day >= 1 and day <=31) or (month == 2 and day >= 1 and day <=29 ) or (month == 12 and day >=1 and day <=31 ):
    season = "Зима"
else: 
    season=" ERROR: Введены неккоректные данные"
# вывод сезона
print("Время года:", season)
