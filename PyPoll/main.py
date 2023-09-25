import os
import csv

total_votes = 0
candidate_names = []
individuals = []
vote_count = []
vote_percent = []

#find the file location
csvpath = os.path.join("PyPoll","election_data.csv")
#open the file in read mode
with open(csvpath) as csvfile:
#specify delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
#read the header row
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    for row in csvreader:
# The total number of votes cast
        total_votes = total_votes + 1
# A complete list of candidates who received votes
        candidate_names.append(row[2])
    for names in set(candidate_names):
        individuals.append(names)
# The total number of votes each candidate won
        number_of_votes = candidate_names.count(names)
        vote_count.append(number_of_votes)
# The percentage of votes each candidate won
        percent_of_votes = (number_of_votes/total_votes)*100
        vote_percent.append(percent_of_votes)

# The winner of the election based on popular vote
    wins = max(vote_count)
    winner = individuals[vote_count.index(wins)]

print("Election Results")
print("------------------")
print("Total Votes: " + (str(total_votes)))
print("------------------")
# print(individuals)
# print(number_of_votes)
# print(percent_of_votes)
for results in range(len(individuals)):
    print(individuals[results] + ": " + str(vote_percent[results]) +"% " + str(vote_count[results]))
print("------------------")
print("Winner: " + str(winner))
print("------------------")

outputpath = os.path.join("Pypoll","Analysis", "vote.txt")
with open(outputpath, "w") as file:
    file.write("Election Results\n")
    file.write("------------------\n")
    file.write("Total Votes: " + (str(total_votes)) + "\n")
    file.write("------------------\n")
    for results in range(len(individuals)):
        file.write(individuals[results] + ": " + str(vote_percent[results]) +"% " + str(vote_count[results]) + "\n")
    file.write("------------------\n")
    file.write("Winner: " + str(winner) + "\n")
    file.write("------------------\n")
