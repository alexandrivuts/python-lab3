import json

with open("firm_data.txt","w") as file:
    file.write("firm1 OOO 10000 5000\n")
    file.write("firm2 OAO 8000 9000\n")
    file.write("firm3 IP 5000 2000\n")

firm_profits = {}
total_profit = 0
num_profitable_firms = 0

with open("firm_data.txt","r") as file:
    for line in file:
        data = line.strip().split()
        if len(data)==4:
            name,ownership,revenue,expenses = data
            revenue = int(revenue)
            expenses = int(expenses)

            profit = revenue - expenses

            if profit>0:
                firm_profits[name] = profit
                total_profit +=profit
                num_profitable_firms+=1
average_profit = total_profit/num_profitable_firms if num_profitable_firms >0 else 0
result_list = [firm_profits,{"average_profit": average_profit}]

with open("firm_profits.json","w") as json_file:
    json.dump(result_list,json_file)

print("Данные сохранены.")
