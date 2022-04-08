from collections import Counter
import csv
import os

# Define our variables
vote_cand = []
votes_per_cand = []

# Create path for csv
poll_csv = os.path.join("..", "Resources", "election_data.csv")

# Open and read csv file
with open(poll_csv) as file:
    csv_reader = csv.reader(file, delimiter=",")
    #Read the header
    csv_header = next(file)

    for row in csv_reader:
        vote_cand.append(row[2])

    # Sort list by ascending order
    sort_list = sorted(vote_cand)

    # Arrange sorted list by most common outcome
    arrange_list = sort_list

    # Count votes per candidate  in most commmon outcome and append to list
    count_cand = Counter (arrange_list)
    votes_per_cand.append(count_cand.most_common())

    # Calculate percentage of votes per candidate
    for item in votes_per_cand:

        first = format((item[0][1])*100/(sum(count_cand.values())),'.3f')
        second = format((item[1][1])*100/(sum(count_cand.values())),'.3f')
        third = format((item[2][1])*100/(sum(count_cand.values())),'.3f')

# Print Analysys to terminal
print("Election Results")
print("-----------------------")
print(f"Total Votes: {sum(count_cand.values())}")
print("-----------------------")
print(f"{votes_per_cand[0][0][0]}: {first}% ({votes_per_cand[0][0][1]})")
print(f"{votes_per_cand[0][1][0]}: {second}% ({votes_per_cand[0][1][1]})")
print(f"{votes_per_cand[0][2][0]}: {third}% ({votes_per_cand[0][2][1]})")
print("-----------------------")
print(f"Winner:  {votes_per_cand[0][0][0]}")
print("------------------------")

