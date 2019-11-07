# Import dependencies
import os
import csv

# assign csv directory
budget_csv = os.path.join('Resources', 'budget_data.csv')

# define Variables 
Total_Months= []
Total = []
Monthly_change = []

# open csv and read
with open(budget_csv,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",") 
    header = next(csvreader) 
    
    #for loop to calculate monthly change
    for row in csvreader: 
        Total_Months.append(row[0])
        Total.append(int(row[1]))
    for i in range(len(Total)-1):
        Monthly_change.append(Total[i+1]-Total[i])

# calculate average change and also return greatest increase decrease 
Average_Change = round(sum(Monthly_change)/len(Monthly_change),2)
Greatest_increase = max(Monthly_change)
Greatest_decrease = min(Monthly_change)
Greatest_increase_Month = Monthly_change.index(max(Monthly_change))+1
Greatest_decrease_Month = Monthly_change.index(min(Monthly_change))+1

# Print the summary table
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(Total_Months)}")
print(f"Total: ${sum(Total)}")
print(f"Average Change: {Average_Change}")
print(f"Greatest Increase in Profits: {Total_Months[Greatest_increase_Month]} (${(str(Greatest_increase))})")
print(f"Greatest Decrease in Profits: {Total_Months[Greatest_decrease_Month]} (${(str(Greatest_decrease))})")

# Output files
file = open("output.txt","w")    
file.write("Financial Analysis"+ "\n")    
file.write("----------------------------"+ "\n")    
file.write(f"Total Months: {len(Total_Months)}"+ "\n")    
file.write(f"Total: ${sum(Total)}"+ "\n")    
file.write(f"Average Change: {Average_Change}"+ "\n")    
file.write(f"Greatest Increase in Profits: {Total_Months[Greatest_increase_Month]} (${(str(Greatest_increase))})"+ "\n")    
file.write(f"Greatest Decrease in Profits: {Total_Months[Greatest_decrease_Month]} (${(str(Greatest_decrease))})"+ "\n")