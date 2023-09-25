import os
import csv

months = []
profit_loss = []
profitloss_change = []
total_profitloss = 0
previous_value = 0
pl_change = 0
pl_change_average = 0
decrease = ["", 0]
increase = ["", 0]

#find the file location
csvpath = os.path.join("PyBank","budget_data.csv")
#open the file in read mode
with open(csvpath) as csvfile:
#specify delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
#read the header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        months.append(row[0])
        total_profitloss = total_profitloss + int(row[1])

        pl_change = int(row[1])-previous_value
        previous_value =int(row[1])
        profitloss_change = profitloss_change + [pl_change]

        pl_change_average = sum(profitloss_change)/len(profitloss_change)

        if pl_change>increase[1]:
            increase[1] = pl_change
            increase[0] = row[0]

        #The greatest decrease in revenue (date and amount) over the entire period
        if pl_change<decrease[1]:
            decrease[1] = pl_change
            decrease[0] = row[0]

print("Financial Analysis")
print("--------------------")
print("Total Months: " + str(len(months)))   
print("Total: " + (str(total_profitloss)))
# print(int(sum(profitloss_change)))
print("Average Change: " + str(pl_change_average))
print("Greatest Increase in Profits: " + str((increase[0],increase[1])))
print("Greatest Decrease in Profits: " + str((decrease[0],decrease[1])))

outputpath = os.path.join("PyBank","Analysis", "profitloss.txt")
with open(outputpath, "w") as file:
    file.write("Financial Analysis\n")
    file.write("--------------------\n")
    file.write("Total Months: " + str(len(months))+ "\n")   
    file.write("Total: " + (str(total_profitloss))+ "\n")
    file.write("Average Change: " + str(pl_change_average)+ "\n")
    file.write("Greatest Increase in Profits: " + str((increase[0],increase[1]))+ "\n")
    file.write("Greatest Decrease in Profits: " + str((decrease[0],decrease[1]))+ "\n")
    