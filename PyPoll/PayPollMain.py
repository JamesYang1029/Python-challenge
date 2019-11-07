# Import dependencies
import os
import csv

# assign csv directory
election_csv = os.path.join('Resources', 'election_data.csv')

# define Variables 
Total_votes = 0 
Khan_num = 0
Correy_num = 0
Li_num = 0
Otooley_num = 0

# open csv and read
with open(election_csv,newline="", encoding="utf-8") as votes:    
    csvreader = csv.reader(votes,delimiter=",")     
    header = next(csvreader)     

    #for loop to calculate total votes and each candidates' votes
    for row in csvreader:     
        Total_votes +=1

        if row[2] == "Khan": 
            Khan_num +=1
        elif row[2] == "Correy":
            Correy_num +=1
        elif row[2] == "Li": 
            Li_num +=1
        elif row[2] == "O'Tooley":
            Otooley_num +=1

 # zip names and number of votes and use max function of dictionary to return winner
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [Khan_num, Correy_num,Li_num,Otooley_num]
 
votes_chart = dict(zip(candidates,votes))
winner = max(votes_chart, key=votes_chart.get)

# calculate each candidates' vote percentages
Khan_percent = (Khan_num/Total_votes) *100
Correy_percent = (Correy_num/Total_votes) * 100
Li_percent = (Li_num/Total_votes)* 100
Otooley_percent = (Otooley_num/Total_votes) * 100

# Print the summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {Total_votes}")
print(f"----------------------------")
print(f"Khan: {Khan_percent:.3f}% ({Khan_num})")
print(f"Correy: {Correy_percent:.3f}% ({Correy_num})")
print(f"Li: {Li_percent:.3f}% ({Li_num})")
print(f"O'Tooley: {Otooley_percent:.3f}% ({Otooley_num})")
print(f"----------------------------")
print(f"Winner: {winner}")
print(f"----------------------------")

# Output files

file = open("output.txt","w") 
file.write(f"Election Results"+ "\n")
file.write(f"----------------------------"+ "\n")
file.write(f"Total Votes: {Total_votes}"+ "\n")
file.write(f"----------------------------"+ "\n")
file.write(f"Khan: {Khan_percent:.3f}% ({Khan_num})"+ "\n")
file.write(f"Correy: {Correy_percent:.3f}% ({Correy_num})"+ "\n")
file.write(f"Li: {Li_percent:.3f}% ({Li_num})"+ "\n")
file.write(f"O'Tooley: {Otooley_percent:.3f}% ({Otooley_num})"+ "\n")
file.write(f"----------------------------"+ "\n")
file.write(f"Winner: {winner}"+ "\n")
file.write(f"----------------------------")