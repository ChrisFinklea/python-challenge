import os
import csv

#path to csv file
poll_csv = os.path.join("C:/Users/cmfjr/Desktop/class/Week3/python_challenge/PyPoll/", "Resources", "election_data.csv")

#Variables
candidates_votes={}
total_votes = 0
winner = ""
results = ""
candidate_percentage_vote = ""
candidate_total_vote = ""
candidates_name = ""

#open bank_csv as csv_file
with open(poll_csv) as csv_file:
    
    #read in the file.  Commas are the delimiter
    csv_reader = csv.reader(csv_file,delimiter=',')
    
    #Storing the headers as csv_header
    csv_header=next(csv_reader)
    
    #Loop through each row of the csv
    for row in csv_reader:
        
        #If the candidate is not in the dictionary then add them with an intial value (vote count) of 0
        if row[2] not in candidates_votes:
            candidates_votes[row[2]] = 0
        
        #If the candidate is in the dictionary then add +1 to their vote count
        if row[2] in candidates_votes:
            candidates_votes[row[2]] = candidates_votes[row[2]] + 1

    #Sum all votes
    total_votes = sum(candidates_votes.values())
    
    #Max returns the key with the greatest value.  The candidate with the most votes.
    winner = max(candidates_votes, key=candidates_votes.get)
    
    #for each candidate in candidates_votes
    for candidate in candidates_votes:
        
        #write the candidates name
        candidates_name = str(candidate)
        
        #calculate their percentage of the vote
        candidate_percentage_vote = str(round((candidates_votes[candidate]/total_votes)*100,3))
        
        #write their total number of votes
        candidate_total_vote = str(candidates_votes[candidate])
        
        #append it to results variable
        results += candidates_name + ": " + candidate_percentage_vote + "% " + "(" + candidate_total_vote + ")\n"

    #All prints
    print("Election Results")
    print("----------------------------")
    print("Total Votes: "+str(total_votes))
    print("----------------------------")
    print(results.rstrip())
    print("----------------------------")
    print("Winner: " + winner)
    print("----------------------------")

#Open text file
with open("C:/Users/cmfjr/Desktop/class/Week3/python_challenge/PyPoll/Analysis/Election Results.txt", "w") as er:
    # Write each line to the file
    er.write("Election Analysis\n")
    er.write("----------------------------\n")
    er.write("Total Votes: " + str(total_votes) + "\n")
    er.write("----------------------------\n")
    er.write(results.rstrip() + "\n")
    er.write("----------------------------\n")
    er.write("Winner: " + winner + "\n")
    er.write("----------------------------")