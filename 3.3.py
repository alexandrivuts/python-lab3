with open("subjects.txt", "r") as file:
    lines = file.readlines()

s_dict = {}

for line in lines:
    parts = line.strip().split(": ")

    if len(parts) == 2 and parts[0]:
        subject = parts[0]
        info = parts[1]

        parts_info = info.split()

        total = 0

        for part in parts_info:
            if part.isdigit():
                total += int(part)

        s_dict[subject] = total

print(s_dict)
