#Module. Importing csv file
import os
import csv

#Set file path
csvpath=os.path.join('.', 'Resources', 'election_data.csv')

#Open and read the file
with open (csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    #Skip the header
    csvheader=next(csvfile)
     #Create Variables
    voter_id=[]
    vote=[]
    candidates=[]
    votes=[]
    #Calculate the total number of votes
    for rows in csvreader:
        voter_id.append(rows[0])
        total_votes=len(voter_id)

    #Create list for candidates and votes
    candidates=["Khan", "Correy", "Li", "O'Tooley"]
    votes=[2218231, 704200, 492940, 105630]

    results_strings=[]

    #Calculate vote and percentage for all candidates with constructed string
    for candidate in candidates:
        candidate_index=candidates.index(candidate)
        vote=votes[candidate_index]
        vote_percent=round(vote/(total_votes)*100, 3)
        result=f"{candidate}: {vote_percent}% {vote}"
        results_strings.append(result)

#Identify the winner with the maximum votes
winner_max=max(votes)
winner_index=votes.index(winner_max)
winner=candidates[winner_index]

#Print total votes, and candidatets with their votes count and vote percentage
print("Election Results")
print("----------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------------")
for r in results_strings:
    print(r)
print("-------------------------------")
print(f"Winner: {winner}")
print("-------------------------------")

#Create outbound file/extract
budget_extract=os.path.join(".", "Analysis", "Main_Pypoll.txt")

with open(budget_extract, 'w') as outfile:
    outfile.write("Election Results\n")
    outfile.write("----------------------\n")
    outfile.write(f"Total Votes: {total_votes}\n")
    outfile.write("----------------------\n")
    for r in results_strings:
        outfile.write(r + "\n")
    outfile.write("----------------------\n")
    outfile.write(f"Winner: {winner}\n")
    outfile.write("----------------------\n")




