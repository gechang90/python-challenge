import os
import csv

pybank_path = os.path.join('Resources','budget_data.csv')
with open(pybank_path,newline='') as csv_file:

    csv_reader = csv.reader(csv_file,delimiter = ",")
    header = next(csv_reader)
    months_total = 0
    profits_lose_sum = 0
    profits_lose_list = []
    each_month_list = []

    for row in csv_reader:
        months_total +=1
        profits_lose_sum +=int(row[1])
        profits_lose_list.append(int(row[1]))
        each_month_list.append(row[0])
    Average_change = (profits_lose_list[months_total-1] - profits_lose_list[0])/months_total
    max_index = profits_lose_list.index(max(profits_lose_list))
    min_index = profits_lose_list.index(min(profits_lose_list))
    
    print("Financail Analysis\n-------------------------")    
    print(f'Total Months: {months_total}')
    print(f'Total: {profits_lose_sum}')
    print(f'Average Change: {Average_change}')
    print(f'Greatest Increase in Profits: {each_month_list[max_index]} (${profits_lose_list[max_index]}) \nGreatest Decrease in Profits: {each_month_list[min_index]} (${profits_lose_list[min_index]})')
    
    
    


