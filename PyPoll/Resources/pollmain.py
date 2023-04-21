# Dependencies
import csv
import os


# Files to load and output
file_to_path = r'/Users/mariaalsayed/Desktop/repo-hub/Python-Challenge2/PyPoll/Resources/election_data.csv'
file_to_load = os.path.join(file_to_path)
file_to_outpath = r'/Users/mariaalsayed/Desktop/repo-hub/Python-Challenge2/PyPoll/Resources/election_data.csv'
file_to_output = os.path.join(file_to_outpath)

#Total Vote Counter
total_votes = 0

#Candidate Options and Votes Counters
candidate_options = []
candidate_votes = {}

#Winnning Candidates and Winning Count Tracker
winning_candidate = ''
winning_count = 0

# Read in hte csv and convert it into a list of dictionaries 
with open(file_to_load) as election_data:
        reader = csv.DictReader(election_data)

        #for each row...
        for row in reader:
                
             # Add to the total vote count
            total_votes = total_votes + 1 

            # Extract the candidate name from each row
            candidate_name = row ['Candidate']

            #if the candidate does not match any existing candidate 
            if candidate_name not in candidate_options:
                  
                  # Add it to the list of candidates in the running
                  candidate_options.append(candidate_name)

                  # And begin tracking that candidate's voter count
                  candidate_votes[candidate_name] = 0

            # Then add a vote to that candidate's count
            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1


# Print the results and export the data to out text file
with open(file_to_output, 'w') as txt_file:
      
    # Print the final vote count
    election_results = (
        f'\n\nElections Results\n'
        f'------------------\n'
        f'Total Votes: {total_votes}\n'
        f'--------------------\n'
    )
    print(election_results)
        
    # Save the final vote count to the text file
    txt_file.write(election_results)
      
    # Determine the winner by looping trhough the counts
    for candidate in candidate_votes:
          
        # Retrieve the vote count percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes)* 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
             winning_count = votes
             winning_candidate = candidate

        # Print each candidate's voter count and percentage
        voter_output = f'{candidate}: {vote_percentage:.3f}% ({votes})\n'
        print(voter_output)

        # Save each candidate's voter count and percentage to text file
        txt_file.write(voter_output)


    # Print the winning candidate
    winning_candidate_summary = (
         f'------------------------\n'
         f'winner: {winning_candidate}\n'
         f'--------------------------\n'

    )
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)








           
      



