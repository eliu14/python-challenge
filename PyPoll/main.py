# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidates = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        cur_candidate = row[2]

        # If the candidate is not already in the candidate list, add them
        if cur_candidate not in candidates:
            candidates[cur_candidate] = 1
        # Add a vote to the candidate's count
        else:
            candidates[cur_candidate] += 1
    print()

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    output1 = f"Election results\n-------------------------\nTotal Votes: {total_votes}\n-------------------------"
    print(output1)
    # Write the total vote count to the text file
    txt_file.write(output1+"\n")

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidates:

        # Get the vote count and calculate the percentage
        vote_count = candidates[candidate]
        vote_percentage = (float(vote_count)/total_votes) * 100
        # Update the winning candidate if this one has more votes
        if vote_count > winning_count:
            winning_count = vote_count
            winning_candidate = candidate
        # Print and save each candidate's vote count and percentage
        output2 = f"{candidate}: {vote_percentage:.3f}% ({vote_count})"
        print(output2)
        txt_file.write(output2 + "\n")
    # Generate and print the winning candidate summary
    output3 = f"-------------------------\nWinner: {winning_candidate}\n-------------------------"
    print(output3)
    # Save the winning candidate summary to the text file
    txt_file.write(output3)