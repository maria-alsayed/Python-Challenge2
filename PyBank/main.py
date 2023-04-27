# Dependencies
import csv
import os

# Files to load and output
#file_to_path = r'/Resources/budget_data.csv'
file_to_load = os.path.join("Resources","budget_data.csv")
#file_to_outpath = r'/Resources/budget_data.txt'
file_to_output = os.path.join("Analysis","budget_analysis.txt")


#Track Various Parameters
total_months = 0
prev_profit = 0
month_of_change = []
profit_change_list = []
greatest_increase = ['',0]
greatest_decrease = ['',99999999999]
total_profit = 0

# Read the csv and convert it into list of dictionaries
with open(file_to_load) as budget_data:
    reader = csv.reader(budget_data)
    csv_header = next(reader)
    print(f'csv header: {csv_header}')


    for row in reader:
        # Track the totals
        total_months = total_months + 1
        total_profit += int(row[1])

        #Track Profit Change
        profit_change = int(row[1]) - prev_profit
        prev_profit = int(row[1])
        profit_change_list = profit_change_list + [profit_change]
        month_of_change = month_of_change + [row[0]]


    # Calculate the greatest increase
        if (profit_change > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = profit_change

    # Calculate the greatest decrease
        if (profit_change < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = profit_change

    # Calculate the Average Profit Change
            profit_avg = sum(profit_change_list) / len(profit_change_list)


    #Generate Output Summary
    output = (
        f'\nFinancial Analysis\n'
        f'--------------------------\n'
        f'Total Months: {total_months}\n'
        f'Total: ${total_profit}\n'
        f'Average Change: ${profit_avg}\n'
        f'Greatest Increase in Profit:{greatest_increase[0]} (${greatest_increase[1]})\n'
        f'Greatest Decrease in Profit: {greatest_decrease[0]} (${greatest_decrease[1]})\n'
    )

    #Print the Output
    print(output)

    #Export the results to text file
    with open(file_to_output,'w')as txt_file:
        txt_file.write(output)
