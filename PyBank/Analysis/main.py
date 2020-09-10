import os
import csv
from statistics import mean


filepath = os.path.join("..","Resources","budget_data.csv")

with open(filepath, newline= '') as csvfile:
    budgetData = csv.reader(csvfile, delimiter = ',')
    header = next(budgetData)

    totalMonths = 0
    netTotal = 0
    profitLoss = []
    dates = []
    for row in budgetData:
        # number of months
        totalMonths += 1
        #net total
        netTotal += int(row[1])
        
        #extract dates
        dates.append(row[0])
        
        #extract profit/loss values and store in sepate list
        profitLoss.append(row[1])
    
    differences = []
    greatestIncrease = 0
    greatestDecrease = 0
    increaseIndex = 0
    decreaseIndex = 0 
    
    for i in range(1, len(profitLoss)):
        delta = int(profitLoss[i]) - int(profitLoss[i-1])
        differences.append(delta)

        if delta > greatestIncrease:
            greatestIncrease = delta
            increaseIndex = i
        
        if delta < greatestDecrease:
            greatestDecrease = delta
            decreaseIndex = i

    meanDifferences = round(mean(differences),3)
    greatestIncreaseDate = dates[increaseIndex]
    greatestDecreaseDate = dates[decreaseIndex]

#create text file 
f = open("FinancialAnalysis.txt", 'w')
f.write("Financial Analysis\n")
f.write("----------------------------\n")
f.write(f"Total Months: {totalMonths}\n")
f.write(f"Total: {netTotal}\n")
f.write(f"Average  Change: {meanDifferences}\n")
f.write(f"Greatest Increase in Profits: {greatestIncreaseDate} (${greatestIncrease})\n")
f.write(f"Greatest Decrease in Profits: {greatestDecreaseDate} (${greatestDecrease})\n")
f.close()


