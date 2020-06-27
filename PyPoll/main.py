# Import the modules
import os
import csv

# Set path for file
csv_path = os.path.join(".", "Resources", "election_data.csv")

# Open the csv
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")  
    csv_header = next(csvreader)

    # Total number of voters
    lines = len(list(csvreader))
    
    # Print results to screen
    print("Election Results")
    print("-------------------------")
    print("Total Votes: "+str(lines))
    print("-------------------------")
    
    # Print results to output file
    output_path = os.path.join(".", "Analysis", "Output.txt")
    with open(output_path, "w") as textfile:

        print("Election Results", file=textfile)
        print("-------------------------", file=textfile)
        print("Total Votes: "+str(lines), file=textfile)
        print("-------------------------", file=textfile)

    # Return to the top of the csv
    csvfile.seek(0)
    csv_header = next(csvreader)

    # Create list to store all values in Candidates column
    all_candidates = []

    for row in csvreader:
        all_candidates.append(str(row[2]))

    # Create list to store only unique values in Candidates column
    unique_candidates = list(dict.fromkeys(all_candidates))
    
    # Return to the top of the csv
    csvfile.seek(0)
    csv_header = next(csvreader)

    # Create dictionary for candidate votes
    votes = {}
    
    # Count votes for each candidate and store values in dictionary
    for i in unique_candidates:
        votes.update({i:all_candidates.count(i)})

    # Determine the winner
    winner = max(votes, key=votes.get)
        
    # Create dictionary for percentages of votes
    percentage = {}   

    # Calculate percentage for each candidate and store values in dictionary
    for i in unique_candidates:
        percentage.update({i:(round(votes[i]/lines*100, 0))})
            
        # Print results to screen
        print(i+": "+str("%.3f%%" % percentage[i])+" ("+str(votes[i])+")")

        # Print results to output file
        output_path = os.path.join(".", "Analysis", "Output.txt")
        with open(output_path, "a") as textfile:
            print(i+": "+str("%.3f%%" % percentage[i])+" ("+str(votes[i])+")", file=textfile)
    
    # Print remaining results to screen
    print("-------------------------")
    print("Winner: "+str(winner))
    print("-------------------------")

    # Print remaining results to output file
    output_path = os.path.join(".", "Analysis", "Output.txt")
    with open(output_path, "a") as textfile:
        print("-------------------------", file=textfile)
        print("Winner: "+str(winner), file=textfile)
        print("-------------------------", file=textfile)