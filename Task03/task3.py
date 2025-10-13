# todo: Данные две переменные:
# age = 36.6
# temperature = 25
# Нужно обменять значения переменных местами. В итого age
# должен равнятся 25 а temperature – 36.6:

age = 36.6
temperature = 25

# с исп. временной переменной switch
# switch = age
# age = temperature
# temperature = switch

#print("age =", age)
#print("temperature =", temperature)

# без исп. временной переменной switch, используя "кортежи" ( (python) может распознавать "кортежи" )
# кортеж - это упорядоченная, неизменяемая коллекция объектов. Если простыми словами, когда объёкты идут через запятую.
age, temperature = temperature, age
print("Возраст =", age)
print("Температура =", temperature)
