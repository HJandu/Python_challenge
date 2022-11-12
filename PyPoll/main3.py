import csv
import os

#path to collect data from my folder (check if this works) 
election_data_csv_path=os.path.join("Resources","election_data.csv")

votes = []
candidates = []
#open and read file
with open(election_data_csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

#Read headers
    csv_header = next(csv_reader)

    #print(f"Header: {csv_header}") 
    # shows Header: ['Ballot ID', 'County', 'Candidate']
    
    for column in csv_reader:
        votes.append(column[0])
        candidates.append(column[2])

    total_votes = (len(votes))
    # print(f"Total Votes: {total_votes}")
    
    Charles = int(candidates.count("Charles Casper Stockham"))
    Diana = int(candidates.count("Diana DeGette"))
    Raymon = int(candidates.count("Raymon Anthony Doane"))

    #Get percentage for each candidate
    Charles_percent = (Charles/total_votes)*100
    Diana_percent = (Diana/total_votes)*100
    Raymon_percent = (Raymon/total_votes)*100

    # Round percentage to 3 decimal places
    Charlesround = round(Charles_percent, 3)
    Dianaround = round(Diana_percent, 3)
    Raymonround = round(Raymon_percent, 3)


    #Print results
    print("Election Results")
    print("------------------------")
    print(f"Total Votes: {total_votes}")
    print("------------------------")
    print(f"Charles Casper Stockham:  {Charlesround}%  ({Charles})")
    print(f"Diana DeGette:   {Dianaround}%   ({Diana})")
    print(f"Raymon Anthony Doane:   {Raymonround}% .  ({Raymon})")
    print("------------------------")

    # compare candidates to output winner
    if Charles > Diana > Raymon:
        Winner = "Charles Casper Stockham"
    elif Diana > Charles > Raymon:
        Winner = "Diana DeGette"
    elif Raymon > Charles > Diana :
         Winner = "Raymon Anthony Doane"
    print(f"Winner:  {Winner}")

# Export the file as a textfile
election_file = os.path.join("Output", "election_data.txt")
with open(election_file, "w") as outfile:

    outfile.write("Election Results\n")
    outfile.write("-----------------------\n")
    outfile.write(f"Total Votes:  {total_votes}\n")
    outfile.write("------------------------\n")
    outfile.write(f"Charles Casper Stockham:  {Charlesround}%  ({Charles})\n")
    outfile.write(f"Diana DeGette:   {Dianaround}%   ({Diana})\n")
    outfile.write(f"Raymon Anthony Doane:   {Raymonround}% .  ({Raymon})\n")
    outfile.write("------------------------\n")
    outfile.write(f"Winner:  {Winner}\n")


