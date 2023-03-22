import  os
import csv

# input
file_path = r'C:\Users\mpena\Documents\git\challenges\mod3_python-challenge\python-challenge\PyBank\Resources\budget_data.csv'

with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csvheader = next(csvreader)
    #print(f'csv header: {csvheader}')

    print("Financial Analysis")
    print('----------------------------------------------------------')

    total_months = 0                                              # Variable assignment 
    total_profit_loss = 0
    
    current = 0 
    previous = 0
    
    net_chg = 0
    total_chg = 0
    avg_chg = 0
    
    largest_net_inc = 0
    largest_net_inc_mo = ''
    
    largest_net_dec= 9999999999999999999
    largest_net_dec_mo = ''

                                                                
    first_row = next(csvreader)                                  # Process header row  
    total_months = total_months + 1                              # Process second row of data; row 2; so that we have a place to start
    total_profit_loss = total_profit_loss + int(first_row[1])
    previous = int(first_row[1])

                                                                # Begins processing rest of data set
    for row in csvreader:
        total_months = total_months + 1                             # The total number of months included in the dataset
        total_profit_loss = total_profit_loss + int(row[1])         # The net total amount of "Profit/Losses" over the entire period
        current = int(row[1])                                     
        net_chg = current - previous
        
                                                                
        total_chg =  total_chg + net_chg                            # The change in "Profit/Losses" over the entire period
        avg_chg = (total_chg) / (total_months -1)                   # The average change in "Profit/Losses" over the entire period
        previous = current
        
                                                               
        if net_chg > largest_net_inc:                               # Where greatest increase in profits along with its associated month   
            largest_net_inc = net_chg
            largest_net_inc_mo = row[0]


        if  net_chg < largest_net_dec:                              # Where greatest decrease in profits along with its associated month                            
            largest_net_dec = net_chg
            largest_net_dec_mo = row[0]

# output = (
#     f"Financial Analysis\n"
#     f"----------------------------\n"
#     f"Total Months: {total_months}\n"
#     f"Total: ${total_profit_loss}\n"
#     f"Average Change: ${avg_chg:.2f}\n"
#     f"Greatest Increase in Profits: {largest_net_inc_mo[0]} (${largest_net_inc[1]})\n"
#     f"Greatest Decrease in Profits: {largest_net_dec_mo[0]} (${largest_net_dec[1]})\n")
# print(output)

    
    # print(f'Total Months: {total_months}')                          # Begins outputs
    # print(f'Total: {total_profit_loss}')
    # print(f'Average change: {avg_chg}')


    # print(f'Greatest Increase in Profits: {largest_net_inc_mo};  (${largest_net_inc})')
    # print(f'Greatest Decrease in Profits: {largest_net_dec_mo};  (${largest_net_dec})')

output = (
    f'Total Months: {total_months}\n'                          # Begins outputs
    f'Total: {total_profit_loss}\n'
    f'Average change: {avg_chg}\n'
    f'Greatest Increase in Profits: {largest_net_inc_mo};  ${largest_net_inc}\n'
    f'Greatest Decrease in Profits: {largest_net_dec_mo};  ${largest_net_dec}\n')
        

print(output)
# #output
# output_path = r'\Analysis\Results_PyBank.txt'
output_path = r'C:\Users\mpena\Documents\git\challenges\mod3_python-challenge\python-challenge\PyBank\Analysis\Results_PyBank.txt'
# output_path = os.path.join("Analysis","Results_PyBank.txt")
with open(output_path, "w") as txt_file:
    txt_file.write(output)


# #output
# output_path = r'\Analysis\Results_PyBank.txt'
# output_path = os.path.join("Analysis","Results_PyBank.txt")
# with open(output_path, "w") as txt_file:
#     txt_file.write(output)