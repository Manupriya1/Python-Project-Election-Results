#test
import csv
import os
# aaassign a variable for the file to load and the path
file_to_load = os.path.join("election_results.csv")
# Assign a varibale to save a file to the path. 
file_to_save = os.path.join("analysis", "election_analysis.txt")
#initialize a total vote counter
total_votes = 0
#declare a new list
candidate_option = []
# declasre th empty dictionary
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# open the election result and read
with open(file_to_load) as election_data:
    #read and analyse data here
    file_reader = csv.reader(election_data)

    # readthe header row
    headers = next(file_reader)

    # print each row in the csv file.
    for row in file_reader:

        #add to the total vote count.
        total_votes +=1

        # pint the candidate name from each row
        candidate_name = row[2]

        if candidate_name not in candidate_option:
            
        #add the candidate name to the candidate list
            candidate_option.append(candidate_name)
        #begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

        # Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    #Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n")
        # save the candidate results t our text file
        txt_file.write(candidate_results)
        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    #  To do: print out the winning candidate, vote count and percentage to
    #   terminal.#  To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

    