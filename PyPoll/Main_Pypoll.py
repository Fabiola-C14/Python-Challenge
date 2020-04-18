import os
import csv

csvpath=os.path.join('.', 'Resources', 'election_data.csv')

with open (csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csvheader=next(csvfile)
    voter_id=[]
    vote=[]
    candidates=[]
    votes=[]

    for rows in csvreader:
        voter_id.append(rows[0])
        total_votes=len(voter_id)

    candidates=["Khan", "Correy", "Li", "O'Tooley"]
    votes=[2218231, 704200, 492940, 105630]

    results_strings=[]

    for candidate in candidates:
        candidate_index=candidates.index(candidate)
        vote=votes[candidate_index]
        vote_percent=round(vote/(total_votes)*100, 3)
        result=f"{candidate}: {vote_percent}% {vote}"
        results_strings.append(result)

winner_max=max(votes)
winner_index=votes.index(winner_max)
winner=candidates[winner_index]

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




