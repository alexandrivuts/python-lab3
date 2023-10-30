with open("F1.txt","w") as f1:
    while True:
        data = input("Введите строку: ")
        if data == "":
            break
        f1.write(data + "\n")

N1 = int(input("введите номер строки номер 1: "))
N2 = int(input("введите номер строки номер 2: "))

with open("F1.txt","r") as f1, open("F2.txt", "w") as f2:
    lines = f1.readlines()
    for i in range(N1 - 1, N2):
        line = lines[i]
        if line.startswith("a"):
            f2.write(line)

with open("F2.txt","r") as f2:
    first_line = f2.readline()
    words = first_line.split()
    count = len(words)
    print(f"Кол-во слов в 1 строке в файле F2: {count}")
