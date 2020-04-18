import os
import csv

#Set path file
csvpath=os.path.join('.','Resources','election_data.csv')

#Open and read the file
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csvheader=next(csvfile)
   
   #Set variables for voter_id and candidates
    voter_id=[]
    candidates=[]
   
   #Count total votes
    for rows in csvreader:
        voter_id.append(rows[0])
        total_votes=len(voter_id)
        
        #Append candidates
        candidates.append (rows[2])
    
    #Count total number of votes and percentage for candidate Khan
    khan_count=int(candidates.count("Khan"))
    khan_percentage=round((khan_count/total_votes) * 100, 3)

    #Count total number of votes and percentage for candidate Correy
    correy_count=int(candidates.count("Correy"))
    correy_percentage=round((correy_count/total_votes)* 100, 3)

    #Count total number of votes and percentage for candidate Li
    li_count=int(candidates.count("Li"))
    li_percentage=round((li_count/total_votes)* 100, 3)

    #Count total number of votes and percentage for candidate O'Tooley
    otooley_count=int(candidates.count("O'Tooley"))
    otooley_percentage=round((otooley_count/total_votes)* 100, 3)
    
    if khan_count > correy_count > li_count > otooley_count:
        winner= "Khan"
    elif correy_count > li_count > otooley_count> khan_count:
        winner="Correy"
    elif li_count > otooley_count > khan_count > correy_count:
        winner="O'Tooley"
    elif otooley_count > khan_count > correy_count > li_count:
        winner= "Li"

#Create printout
print("Election Results")
print("----------------------")
print(f"Total Votes: {total_votes}")
print("----------------------")
print(f"Khan: {khan_percentage}% {khan_count}")
print(f"Correy: {correy_percentage}% {correy_count}")
print(f"Li: {li_percentage}% {li_count}")
print(f"O'Tolley: {otooley_percentage}% {otooley_count}")
print("----------------------")
print(f"Winner: {winner}")
print("----------------------")

#Create outbound file/extract
budget_extract=os.path.join(".", "Analysis", "PyPoll_main.txt")

with open(budget_extract, 'w') as outfile:
    outfile.write("Election Results\n")
    outfile.write("----------------------\n")
    outfile.write(f"Total Votes: {total_votes}\n")
    outfile.write("----------------------\n")
    outfile.write(f"Khan: {khan_percentage}% {khan_count}\n")
    outfile.write(f"Correy: {correy_percentage}% {correy_count}\n")
    outfile.write(f"Li: {li_percentage}% {li_count}\n")
    outfile.write(f"O'Tolley: {otooley_percentage}% {otooley_count}\n")
    outfile.write("----------------------\n")
    outfile.write(f"Winner: {winner}\n")
    outfile.write("----------------------\n")
