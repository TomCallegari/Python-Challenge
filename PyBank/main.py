
# PyBank script

# Import the pandas package and store as pd per standard practice
import pandas as pd

# Read in budget_data.csv as a pandas dataframe named data
data = pd.read_csv('budget_data.csv')

# Use string split to separate the column by '-' and pull out the left or 0 indexed item
# then add the split column month as a new column to data
month = data['Date,Profit/Losses'].str.split('-', n=1, expand=True)
data['month'] = month[0]

# Use string split to separate the right or 1 indexed item by ','
# and pull the year (0 item) and Profit/Loss (1 item) columns
year = month[1].str.split(',', n=1, expand=True)

# Add year and Profit/Loss (P/L) columns to data
data['year'] = year[0]
data['P/L'] = year[1]

# Summarize key info and store as individual variables
months = data['month'].count() 

convert = {'P/L': int}
data = data.astype(convert) # Convert P/L to int datatype

total = data['P/L'].sum()
avg = round(data['P/L'].mean(), 3)

# Filter data to get specific Max and Min rows and store as variables
max = data.max(axis=0)
min = data.min(axis=0)

# Print summary information
print(' ')
print(' Financial Analysis')
print('-'*50)
print(f' Total Months: {months}')
print(f' Total: ${total}')
print(f' Average Change: ${avg}')
print(f' Greatest Increase in Profits: {max[1]}' + f' {max[2]}' + f' (${max[3]})')
print(f' Greatest Decrease in Profits: {min[1]}' + f' {min[2]}' + f' (${min[3]})')

# Save summary information as a .txt file
with open('PyBank.txt', 'w') as f:
    print(' ', file=f)
    print(' Financial Analysis', file=f)
    print('-'*50, file=f)
    print(f' Total Months: {months}', file=f)
    print(f' Total: ${total}', file=f)
    print(f' Average Change: ${avg}', file=f)
    print(f' Greatest Increase in Profits: {max[1]}' + f' {max[2]}' + f' (${max[3]})', file=f)
    print(f' Greatest Decrease in Profits: {min[1]}' + f' {min[2]}' + f' (${min[3]})', file=f)