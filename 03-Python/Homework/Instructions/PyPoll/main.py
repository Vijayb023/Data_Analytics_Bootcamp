import os
import csv


Election_Data = os.path.join("Resources","election_data.csv")
vote_count = []
vote_percent = []
candidate_list = []
key_candidate = []
total_votes = 0


with open(Election_Data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        total_votes = total_votes + 1
        candidate_list.append(row[2])
    for i in set(candidate_list):
        key_candidate.append(i)
        number_candidate = candidate_list.count(i)
        vote_count.append(number_candidate)
        percent = (number_candidate/total_votes)*100
        vote_percent.append(percent)
        
    
    winner = key_candidate[vote_count.index(max(vote_count))]
    

 
print("-----------------------")
print("Election Results")   
print("-----------------------")
print("Total Votes: " + str(total_votes))    
print("-----------------------")
for i in range(len(key_candidate)):
            print(key_candidate[i] + ": " + str(round(vote_percent[i],3)) +"% (" + str(vote_count[i])+ ")")
print("-----------------------")
print("The winner is: " + winner)
print("-----------------------")


with open('Vijay_Election.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("-------------------------------------\n")
    text.write("Total Vote: " + str(total_votes) + "\n")
    text.write("-------------------------------------\n")
    for i in range(len(set(key_candidate))):
        text.write(key_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("-------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("-------------------------------------\n")

