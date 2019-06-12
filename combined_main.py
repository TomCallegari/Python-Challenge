
import pandas as pd 

print('''


''')

print(
'''Please choose a dataset for analysis:
--------------------------------------------------

[1] for PyBank 'budget_data.csv'

                or

[2] for PyPoll 'election_data.csv'
'''
)

print('-'*50)
print('''


''')
first_input = int(input('Selection: '))

if first_input == 1:

    data = pd.read_csv('budget_data.csv')
    month = data['Date,Profit/Losses'].str.split('-', n=1, expand=True)
    data['month'] = month[0]
    year = month[1].str.split(',', n=1, expand=True)
    data['year'] = year[0]
    data['P/L'] = year[1]
    months = data['month'].count() 
    convert = {'P/L': int}
    data = data.astype(convert) 
    total = data['P/L'].sum()
    avg = round(data['P/L'].mean(), 3)
    max = data.max(axis=0)
    min = data.min(axis=0)

    print(''' 
    

    ''')
    print('Financial Analysis')
    print('-'*50)
    print(f' Total Months: {months}')
    print(f' Total: ${total}')
    print(f' Average Change: ${avg}')
    print(f' Greatest Increase in Profits: {max[1]}' + f' {max[2]}' + f' (${max[3]})')
    print(f' Greatest Decrease in Profits: {min[1]}' + f' {min[2]}' + f' (${min[3]})')

    with open('PyBank.txt', 'w') as f:
        print(' ', file=f)
        print('Financial Analysis', file=f)
        print('-'*50, file=f)
        print(f' Total Months: {months}', file=f)
        print(f' Total: ${total}', file=f)
        print(f' Average Change: ${avg}', file=f)
        print(f' Greatest Increase in Profits: {max[1]}' + f' {max[2]}' + f' (${max[3]})', file=f)
        print(f' Greatest Decrease in Profits: {min[1]}' + f' {min[2]}' + f' (${min[3]})', file=f)
    
    print('''
    
    ''')
    print('-'*50)
    print("A 'PyBank.txt' file has been saved to your local directory.")
    print(' ')

elif first_input == 2:

    data = pd.read_csv('election_data.csv')
    voters = int(data['Voter ID'].nunique())
    data['Votes'] = 1 
    vote_count = data.groupby('Candidate').agg({'Votes': 'sum'})
    vote_count['Percent'] = round((vote_count['Votes'] / voters) * 100, 2)
    vote_count = vote_count.sort_values(by='Percent', ascending=False)
    khan = vote_count.loc['Khan']
    correy = vote_count.loc['Correy']
    li = vote_count.loc['Li']
    otooley = vote_count.loc["O'Tooley"]

    print(''' 
    
    
    ''')
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

    print('''
    
    ''')
    print('-'*50)
    print("A 'PyPoll.txt' file has been saved to your local directory.")
    print(' ')

else:

    print('''
    











    ''')
    print('''
It seems you have not followed the instructions ... 
        
buh bye now.
        ''')
    print('''
    



    ''')    

print(' ')
print(' ')

second_input = input('Would you like the other analysis just because? (Y/N)').lower()

if second_input == 'y' and first_input == 1:

    data = pd.read_csv('election_data.csv')
    voters = int(data['Voter ID'].nunique())
    data['Votes'] = 1 
    vote_count = data.groupby('Candidate').agg({'Votes': 'sum'})
    vote_count['Percent'] = round((vote_count['Votes'] / voters) * 100, 2)
    vote_count = vote_count.sort_values(by='Percent', ascending=False)
    khan = vote_count.loc['Khan']
    correy = vote_count.loc['Correy']
    li = vote_count.loc['Li']
    otooley = vote_count.loc["O'Tooley"]

    print(''' 
    
    
    ''')
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

    print('''
    
    ''')
    print('-'*50)
    print("A 'PyPoll.txt' file has been saved to your local directory.")
    print(' ')

elif second_input == 'y' and first_input == 2:

    data = pd.read_csv('budget_data.csv')
    month = data['Date,Profit/Losses'].str.split('-', n=1, expand=True)
    data['month'] = month[0]
    year = month[1].str.split(',', n=1, expand=True)
    data['year'] = year[0]
    data['P/L'] = year[1]
    months = data['month'].count() 
    convert = {'P/L': int}
    data = data.astype(convert) 
    total = data['P/L'].sum()
    avg = round(data['P/L'].mean(), 3)
    max = data.max(axis=0)
    min = data.min(axis=0)

    print(''' 
    
    
    ''')
    print('Financial Analysis')
    print('-'*50)
    print(f' Total Months: {months}')
    print(f' Total: ${total}')
    print(f' Average Change: ${avg}')
    print(f' Greatest Increase in Profits: {max[1]}' + f' {max[2]}' + f' (${max[3]})')
    print(f' Greatest Decrease in Profits: {min[1]}' + f' {min[2]}' + f' (${min[3]})')

    with open('PyBank.txt', 'w') as f:
        print(' ', file=f)
        print('Financial Analysis', file=f)
        print('-'*50, file=f)
        print(f' Total Months: {months}', file=f)
        print(f' Total: ${total}', file=f)
        print(f' Average Change: ${avg}', file=f)
        print(f' Greatest Increase in Profits: {max[1]}' + f' {max[2]}' + f' (${max[3]})', file=f)
        print(f' Greatest Decrease in Profits: {min[1]}' + f' {min[2]}' + f' (${min[3]})', file=f)
    
    print('''
    
    ''')
    print('-'*50)
    print("A 'PyBank.txt' file has been saved to your local directory.")
    print(' ')

elif second_input == 'n':

    print('''
    











    ''')
    print('Ok then, buh bye now.')
    print('''





     ''')


elif second_input != 'y' or second_input != 'n':

    print('''
    











    ''')
    print('''
It seems you have not followed the instructions ... 
        
buh bye now.
        ''')
    print('''
    



    ''')