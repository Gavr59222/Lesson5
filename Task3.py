summa = 0
count = 0
persons = []
with open("sal.txt", "r") as file_obj:
    for line in file_obj:
        tokens = line.split(' ')
        if int(tokens[1]) <= 20000:
            persons.append(tokens[0])
        summa += int(tokens[1])
        count += 1
result = summa / count
print(f"сотрудники с низким окладом: {persons}")
print(f"средний доход сотрудников: {result}")