# Import the modules
import os
import csv

# Set path for file
csv_path = os.path.join(".", "Resources", "budget_data.csv")

# Open the csv
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")  
    csv_header = next(csvreader)

    # Total number of months - Mehtod 1
    lines = len(list(csvreader))
    
    # Return to the top of the csv
    csvfile.seek(0)
    csv_header = next(csvreader)

    # Net total amoutn of "Profit/Losses"
    net_total = 0
    for row in csvreader:           
        net_total += int(row[1]) 
    
    # Return to the top of the csv AGAIN
    csvfile.seek(0)
    csv_header = next(csvreader)

    # Average of monthly changes in "Profit/Losses"
    # Create list to store values
    net_profit = []
    mth_change = []
    max_increase = []
    max_decrease = []
    date = []

    # Store values in the list
    for row in csvreader:
        net_profit.append(int(row[1]))
        date.append(str(row[0]))

    # Loop through all relevant rows to retrieve values and calculate
    for i in range (1, lines):
        
        mth_change.append(net_profit[i] - net_profit[i-1])
        avg_mth_change = sum(mth_change) / (lines - 1)
          
    
    # Print the result on screen & output file
    output_path = os.path.join(".", "Analysis", "Output.txt")
    with open(output_path, "w") as textfile:
    
        print("Financial Analysis", file=textfile)
        print("----------------------------", file=textfile)
        print("Total Months:", lines, file=textfile)
        print("Total: $"+str(net_total), file=textfile)
        print("Average Change: $"+str(round(avg_mth_change, 2)), file=textfile)   
    
        max_increase = max(mth_change)
        max_decrease = min(mth_change)

        print("Greatest Increase in Profits:", (date[mth_change.index(max_increase) + 1]), "($"+str(max_increase)+")", file=textfile)
        print("Greatest Decrease in Profits:", (date[mth_change.index(max_decrease) + 1]), "($"+str(max_decrease)+")", file=textfile)

    
   
    
    
    




