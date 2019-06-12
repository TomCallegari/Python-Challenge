
# PyPoll script

# Import the pandas package and store as pd per standard practice
import pandas as pd
 
# Read in election_data.csv as a pandas dataframe named data
data = pd.read_csv('election_data.csv')

# Count the number of unique voter ids and store as an integer variable named voters
voters = int(data['Voter ID'].nunique())

# Create a new column named Votes with a value of 1 for each voter
data['Votes'] = 1 

# Group by the candidate variable and sum the number of votes for each
vote_count = data.groupby('Candidate').agg({'Votes': 'sum'})

# Add a new column to the dataframe vote_count that contains the percentage of votes cast
# for each candidate in the proper numerical format
vote_count['Percent'] = round((vote_count['Votes'] / voters) * 100, 2)

# Sort the vote_count dataframe from highest percentage to lowest
vote_count = vote_count.sort_values(by='Percent', ascending=False)

# Separate each candidate row for indexing in the print statements
khan = vote_count.loc['Khan']
correy = vote_count.loc['Correy']
li = vote_count.loc['Li']
otooley = vote_count.loc["O'Tooley"]

# Print summary information
print(' ')
print(' Election Results')
print('-'*25)
print(f' Total Votes: {voters}')
print('-'*25)
print(f' Khan: {khan[1]}% ({khan[0]})')
print(f' Correy: {correy[1]}% ({correy[0]})')
print(f' Li: {li[1]}% ({li[0]})')
print(f" O'Tooley: {otooley[1]}% ({otooley[0]})")
print('-'*25)
print(' Winner: Khan')
print('-'*25)

# Save summary information as a .txt file
with open('PyPoll.txt', 'w') as f:
    print(' ', file=f)
    print(' Election Results', file=f)
    print('-'*25, file=f)
    print(f' Total Votes: {voters}', file=f)
    print('-'*25, file=f)
    print(f' Khan: {khan[1]}% ({khan[0]})', file=f)
    print(f' Correy: {correy[1]}% ({correy[0]})', file=f)
    print(f' Li: {li[1]}% ({li[0]})', file=f)
    print(f" O'Tooley: {otooley[1]}% ({otooley[0]})", file=f)
    print('-'*25, file=f)
    print(' Winner: Khan', file=f)
    print('-'*25, file=f)