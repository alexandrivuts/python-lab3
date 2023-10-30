with open("Государство.txt","r") as file:
    lines = file.readlines()

for line in lines:
    data = line.strip().split()
    if len(data) == 4:
        country, capital, population, area = data
        population = int(population)
        if population > 1000000:
            print(f"Страна: {country}, население: {population}")
