import  os
import csv

file_path = r'C:\Users\mpena\Documents\git\challenges\mod3_python-challenge\python-challenge\PyBank\Resources\budget_data.csv'

with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csvheader = next(csvreader)
    #print(f'csv header: {csvheader}')

    print("Financial Analysis")
    print('----------------------------------------------------------')

    total_months = 0
    total_profit_loss = 0
    
    current = 0 
    change_a = 0
    previous = 0
    biggest_inc = 0
    biggest_dec= 9999999999999999999

    
    for row in csvreader:
        total_months = total_months + 1                         # The total number of months included in the dataset
        total_profit_loss = total_profit_loss + int(row[1])     # The net total amount of "Profit/Losses" over the entire period
        
        current = int(row[1])                                   # The change in "Profit/Losses" over the entire period, and then the average of those changes
        
        change_a = ((current) - (previous))
        
        if total_months > 1:
            change_a = (change_a) + (current - previous)
            avg_chg = (change_a) / (total_months -1) 
            change_a = (current) - (previous)
            previous = current
        
        
        if change_a > biggest_inc:
            biggest_inc = change_a
        if  change_a < biggest_dec:
            biggest_dec = change_a

    

    print(f'Total Months: {total_months}')
    print(f'Total: {total_profit_loss}')
    print(f'Average change: {avg_chg}')
    
    
    print(f'Greatest Increase in Profits: {biggest_inc}')
    print(f'Greatest Decrease in Profits: {biggest_dec}')
    
    # for i in range(list(change_b)):
    #     current = range(row[1])    
    #     change_b = (current) - (previous)        
    #     change_b = max
    #     change_b = min
    # print(change_b)

    # for i in range(list(change_b)):
    # value_from_list1 = list1[change_b]
    # value_from_list2 = list2[change_b]
    
    # #                                                             # print(f'Greatest Increase in Profits: {max}')
    #   for i in range(len(list1)):
    # value_from_list1 = list1[i]
    # value_from_list2 = list2[i]                                                          # print(f'Greatest Decrease in Profits: {min}')
       
        
        # rev_net = int(row[1])
        # net_change = int(row[1]) - prev_net
        # change += [net_change]
        
        # if prev_net > net_change:
        #     prev_net = prev_net
        #     prev_net = net_change

        # current = int(row[1])
        # if total_months > 1:      
        #     stored_value = (current) - (previous)
        #     # stored_value = max(stored_value)
   


        # if stored_value > current:
        #    stored_value = stored_value
        # else: stored_value = current   

        # net_change = int(row[1]) - prev_net
        # prev_net = int(row[1])
        # change += [net_change]
        
        

          # The greatest increase in profits (date and amount) over the entire period
        # if change > current_value:
        #     current_value = change
        

        # # The greatest decrease in profits (date and amount) over the entire period
        # if change < current_value_2:
        #     current_value_2 = change

        # stored_value2 = change  #The greatest decrease in profits (date and amount) over the entire period
        # if stored_value2 < current_value:
        #     stored_value2 = stored_value2
        # else: stored_value2 = current_value
    
    
   



   

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

     # current = int(row[1])                                    # The change in "Profit/Losses" over the entire period, and then the average of those changes
        # if total_months > 1:  
        #     change = (change + ((current) - (previous)))       
        # previous = current