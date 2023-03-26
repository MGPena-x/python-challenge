import  os
import csv

# input
file_path = os.path.join("PyPoll", "Resources", "election_data.csv")

with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csvheader = next(csvreader)
    #print(f'csv header: {csvheader}')

    # variable assignment
    total_votes = 0
    

    first_row = next(csvreader)                                         # Process the header row                             
    total_votes = total_votes + 1                                       # Process second row of data; row 2; so that we have a place to start
    #previous = int(first_row[1])

   

     # Total number of votes cast                                       # Begins processing rest of data set
    for row in csvreader:
        total_votes = total_votes + 1                                   # The total number of votes based on count of voter ballots
    total_votes = total_votes


# A complete list of candidates that recieved vote

# % of votes each candidate won

# The total number of votes each candidate won

#The winner of the election based on popular vote


# Begin outputs for print
output = (                                                          
     f'Eelection Results:\n'
     f'----------------------------------------------------------\n'
     f'Total Votes: {total_votes}\n')
#     f'----------------------------------------------------------\n'
#     f'Charles Casper Stockman: {}\n'
#     f'Diana DeFette: {}; {}\n'
#     f'Raymon Anthony Doane: {};  ${}\n'
#     f'----------------------------------------------------------\n'
#     f'Winner: Diana DeGette: {};  ${}\n'
#     f'----------------------------------------------------------\n')

print(output)


output_path = os.path.join("Pypoll", "Analysis", "Results_pyPoll.txt")
with open(output_path, "w") as txt_file:
    txt_file.write(output)






