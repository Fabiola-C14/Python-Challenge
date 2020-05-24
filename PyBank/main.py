#Module. Importing csv file
import os
import csv

#Set file path 
csvpath=os.path.join('.','Resources','budget_data.csv')

#Open and read the file
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    #Skip the header
    csv_header=next(csvfile)

    #Create Variables
    Date_Month=[]
    Profit=[]
    Gains_Change=[]

    #Loop through rows in csv file
    for rows in csvreader:

        #Calculate Total Months
        Date_Month.append(rows[0])
        Total_Months=len(Date_Month)

        #Calculate Profit/Loss
        Profit.append(int(rows[1]))
        Total=sum(Profit)

    #Calculate the difference in month to month Profit/Loss.
    for n in range(len(Profit)-1): 
        Gains_Change.append((Profit[n+1])- (Profit[n]))

        #Calculate the average of the Profit/Loss changes.
        Average_Change=round(sum(Gains_Change)/len(Gains_Change),2)  
        
        #Calculate greatest increase in Profit 
        Profit_Increase=max(Gains_Change)

        #Calculate greatest decrease in Profit
        Profit_Decrease=min(Gains_Change)

        #Create index for greatest profit increase and decrease
        Month_Increase=Gains_Change.index(Profit_Increase)
        Month_Decrease=Gains_Change.index(Profit_Decrease)

        #Assign date to greatest profit increase and decrease
        Greatest_Month=Date_Month[Month_Increase + 1]
        Decrease_Month=Date_Month[Month_Decrease + 1]

#Create printout
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {Total_Months}")
print(f"Total: ${Total}")
print(f"Average Change: ${Average_Change}")
print(f"Greatest Increase in Profit: {Greatest_Month} (${Profit_Increase})")
print(f"Greatest Decrease in Profit: {Decrease_Month} (${Profit_Decrease})")

#Create outbound file/extract
budget_extract=os.path.join(".", "Analysis", "PyBank.txt")

with open(budget_extract, 'w') as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("-----------------------------\n")
    outfile.write(f"Total: ${Total}\n")
    outfile.write(f"Average Change: ${Average_Change}\n")
    outfile.write(f"Greatest Increase in Profit: {Greatest_Month} (${Profit_Increase})\n")
    outfile.write(f"Greatest Decrease in Profit: {Decrease_Month} (${Profit_Decrease})\n")
