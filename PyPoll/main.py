# import the os module
import os

# navigate folder from python-challenge to budget_data
csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')

# module for reading csv files
import csv

# total number of votes cast
# add up all rows minus the header row
total_votes = 0

# complete list of candidates who received votes
# list of unique names of all rows
candidates = []

# total number of votes each candidate won
# Add up all rows with name of candidate in
votes_per_candidate = 0

# percentage of votes each candidate won
# Add up all rows with name of candidate / by (total rows minus header row))
win_percentage = 0

# winner of the election based on popular vote
# print name of candidate with most votes. 
election_winner = 0
winner_name = ""


# Reading using csv 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
# Read each row of data after the header
    next(csvreader)
    votes_count = 0
    candidates = []
    for row in csvreader:
        votes_count+=1
        candidates.append(row[2])
        
        # votes = int(row[0])
        # total_votes+=votes
    # print('Total Votes', votes_count)
# Skip the header row
        
from collections import Counter
import numpy as np

# Export the analysis to a text file
output = "Election_Results.txt"
# open file and the information into the output file
with open(output, 'w') as file:

# print(csvreader)
# print(row)
# to count total votes
# list of candidates
# # count votes per candidate
# print(total_votes)
# print(voted_candidates)
# print(votes_won)
# print(win_percentage)
# print(election_winner)

    candidates_votes_frequency = Counter(candidates)


    print ("Election Results") 

    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes:{votes_count}\n")
    file.write("-------------------------\n")
    print('Total Votes :', votes_count)
    
    greatest_votes = 0
    for candidate, votes in candidates_votes_frequency.items():
        perc = (votes/votes_count)*100
        print(candidate, perc,votes)
        
        # print the financial analysis report
        
        file.write(f"{candidate}: {round(perc,3)}% ({votes})\n")
        if votes > greatest_votes : 
            greatest_votes = votes 
            winner = candidate

    file.write("-------------------------\n")
    file.write(f"winner:{winner}\n")
    file.write("-------------------------")

# end of writing and saving file
file.close() 
