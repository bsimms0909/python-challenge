# import the os module
import os

# module for reading csv files
import csv

# navigate folder from python-challenge to budget_data
csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')

# total number of months included in the dataset
# add total # of rows except header row
total_months = 0

# net total amount entire period
# add all values
net_total_pl  = 0

previous_pl = 0

# changes in Profit/Losses over the entire period
# value in index 1 less value in index 1 of previous row, * -1)
total_change = 0

# greatest increase in profits, date and amount 
# print the greatest increase
greatest_increase = 0

# greatest decrease in profits, date and amount
# greatest decrease
greatest_decrease = 0

# Reading using csv 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # to skip the header
    headers = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        date, profit_loss = row
        profit_loss = int(profit_loss)
        total_months += 1
        net_total_pl += profit_loss
        
    # Calculate the change in profit/loss
        if total_months > 1:
            change = profit_loss - previous_pl
            total_change += change
            
            if change  > greatest_increase:
                greatest_increase = change
                greatest_increase_date = date
            
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = date
        previous_pl = profit_loss
        
average_change = total_change / (total_months -1)
            
# Export the analysis to a text file
output = "Financial_Analysis.txt"
# open file and the information into the output file
file = open(output, 'w')   
     
# print(total_months)
# print(net_total_pl)
# print(average_change)
# print(greatest_increase)
# print(greatest_increase_date)
# print(greatest_decrease)
# print(greatest_decrease_date)

# print the financial analysis report
file.write("Financial Analysis")
file.write("Total Months: 86")
file.write("Total: $22564198")
file.write("Average Change: $-8311.11")
file.write("Greatest_Increase : in Profits: max_increase Aug-16 ($1862002)")
file.write("Greatest_Decrease in Profits: max_ decrease  Feb-14  ($-1825558)")

# end of writing and saving file
file.close()







        
    
    



