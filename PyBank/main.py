import  os
import csv

file_path = r'C:\Users\mpena\Documents\git\challenges\mod3_python-challenge\python-challenge\PyBank\Resources\budget_data.csv'

with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csvheader = next(csvreader)
    #print(f'csv header: {csvheader}')

# The total number of months included in the dataset
    #csv reader file: count number of rows
    #rows need to have contents
    # need row count

    print("Financial Analysis")
    print('----------------------------------------------------------')


    total_months = 0
    total_profit_loss = 0
    
    current = 0
    previous = 0 
    current_change = 0
    previous_change = 0

    for row in csvreader:
        total_months = total_months + 1                         # The total number of months included in the dataset
        total_profit_loss = total_profit_loss + int(row[1])     # The net total amount of "Profit/Losses" over the entire period
        
        current = int(row[1])                                    # The change in "Profit/Losses" over the entire period, and then the average of those changes
        if total_months > 1:
            current_change = (current_change + ((current) - (previous)))
            # previous_change = (current_change + ((current) - (previous))) - (current_change - ((current) + (previous)))
            avg_chg = current_change / (total_months - 1)          
        previous = current

        # current = int(row[1])                                    # The change in "Profit/Losses" over the entire period, and then the average of those changes
        # if total_months > 1:  
        #     change = (change + ((current) - (previous)))       
        # previous = current


    print(f'Total Months: {total_months}')
    print(f'Total: {total_profit_loss}')
    print(f'Average Change: {avg_chg}')
    print(f'Previous Change: {previous_change}')



   

# The greatest increase in profits (date and amount) over the entire period
    # get the highest positive number
    # get the associated date

# The greatest decrease in profits (date and amount) over the entire period
    # get the lowest negative number
    # get the associated date

    # profit_loss = row
    # for row in csvreader:
    #     profit_loss + int(sum(row[1]))
    # print(f'Total: {profit_loss}')