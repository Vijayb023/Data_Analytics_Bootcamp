import os 
import csv 

BudgetDatacsv = os.path.join("Resources","budget_data.csv")

total_months = 0

total_profits = 0

starting_profit = 0
change_profit = 0

profit=[]
changes=[]
date=[]

with open(BudgetDatacsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        
        date.append(row[0])

        profit.append(row[1])
        total_profits = total_profits + int(row[1])

        total_months = total_months +1

        final_profit = int(row[1])
        Monthly_profit = final_profit - starting_profit

        changes.append(Monthly_profit)

        change_profit = change_profit + Monthly_profit
        starting_profit = final_profit
        average_profit = (change_profit/total_months)

        greatest_increase = max(changes)
        Date_increase = date[changes.index(greatest_increase)]


        greatest_decrease = min(changes)
        Date_decrease = date[changes.index(greatest_decrease)]

        
       


    print("----------------------------------------------------------")
    print("Financial Analysis")
    print("----------------------------------------------------------")
    print("Total Months: " + str(total_months))
    print("Total Profits: " + "$" + str(total_profits))
    print("Average Change: " + "$" + str(int(average_profit)))
    print("Greatest Increase in Profits: "+str(Date_increase)+ " ($" + str(greatest_increase) + ")")
    print("Greatest Decrease in Profits: "+str(Date_decrease)+ " ($" + str(greatest_decrease) + ")")
    print("----------------------------------------------------------")

with open('Vijay_fin_analysis.text','w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(total_months) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profits) +"\n")
    text.write("    Average Change: " + "$" + str(int(average_profit)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(Date_increase) + " ($" + str(greatest_increase) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(Date_decrease) + " ($" + str(greatest_decrease) + ")\n")
    text.write("----------------------------------------------------------\n")

    

