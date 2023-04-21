# Dependencies
import csv
import os

# Files to load and output
file_to_path = r'/Users/mariaalsayed/Desktop/repo-hub/Python-Challenge2/PyBank/Resources/budget_data.csv'
file_to_load = os.path.join(file_to_path)
file_to_outpath = r'/Users/mariaalsayed/Desktop/repo-hub/Python-Challenge2/PyBank/Resources/budget_data.csv'
file_to_output = os.path.join(file_to_outpath)


#Track Various Parameters
total_months = 0
prev_profit = 0
month_of_change = []
profit_change_list = []
greatest_increase = ['',0]
greatest_decrese = ['',99999999999]
total_profit = 0

# Read the csv and convert it into list of dictionaries
with open(file_to_load) as budget_data:
    reader = csv.reader(budget_data)
    cvs_header = next(reader)
    print(f'cvs header: {cvs_header}')
    for row in reader:



         #Track The Totals
        total_months = total_months + 1
        total_profit = total_profit + int(row[1])

        #Track Profit Change
        profit_change = int(row[1]) - prev_profit
        prev_profit = int(row[1])
        profit_change_list = profit_change_list + [profit_change]
        month_of_change = month_of_change = [row[0]]


    # Calculate the greatest increase
    if (profit_change > greatest_increase[1]):
        greatest_increase[0] = row[0]
        greatest_increase[1] = profit_change

    # Calculate the greatest decrease
    if (profit_change < greatest_decrese[1]):
        greatest_decrese[0] = row[0]
        greatest_decrese[1] = profit_change

    # Calculate the Average Profit Change
    profit_avg = sum(profit_change_list) / len(profit_change_list)


    #Generate Output Summary
    output = (
        f'\nfinancial Analysis\n'
        f'----------------------\n'
        f'Total Months: {total_months}n'
        f'Average Profit Change:{profit_avg}\n'
        f'Greatest Increase in Profit:{greatest_increase[0]} (${greatest_increase[1]})\n'
        f'Grearest Decrease in Profit: {greatest_decrese[0]} (${greatest_decrese[1]})\n'
    )

    #Print the Output
    print(output)

    #Export the results to text file
    with open(file_to_output,'w')as txt_file:
        txt_file.write(output)