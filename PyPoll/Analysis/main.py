import os
import csv

filepath = os.path.join("..","Resources","election_data.csv")

with open(filepath, 'r') as dataset:
    
    data = csv.reader(dataset, delimiter = ',')
    header = next(data)

    totalVotes = 0
    # Initialising empty dictionary to build a tally type dictionary
    candidateDict = {}
    for row in data:
        totalVotes += 1
        
        candidateName = row[2]
        
        # Building the dictionary
        if candidateName not in candidateDict:
            candidateDict[candidateName] = 1 
        candidateDict[candidateName] += 1 

    # Extracting the names (keys) will make it easier to calculate aggregate values
    candidatesList = [candidate for candidate in candidateDict.keys()]

# Creating export file
export = open("ElectionResults.txt", "a")
export.write("Election Results\n")
export.write("-------------------------\n")
export.write(f"Total Votes: {totalVotes}\n")
export.write("-------------------------\n")

# Empty list to store percentages and calculate maximum value
percentages = []
for name in candidatesList:
    
    candidateVotes = candidateDict[name] 
    percentageWon = round(candidateVotes/totalVotes*100, 2)
    percentages.append((percentageWon,name))

    myString = f"{name}: {percentageWon}% ({candidateVotes})\n"      
    export.write(myString)
export.write("-------------------------\n")

winner = max(percentages)[1]

export.write(f"Winner: {winner}\n")
export.write("-------------------------")
export.close()