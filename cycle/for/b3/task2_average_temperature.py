countries_temperature = [
    ['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Germany', [57.2, 55.4, 59, 59, 53.6]],
    ['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]

for country in countries_temperature:
    temp_count = 0
    time_count = 0
    for temp in country[1]:
        temp_count += temp
        time_count += 1
    print(f"Средняя температура в {country[0]} — {(temp_count/time_count) :.2f} F")


# or
print('#############################')
for country in countries_temperature:
    avr_temp = round(sum(country[1])/len(country[1]), 2)
    print(f"Средняя температура в {country[0]} — {avr_temp} F")