# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
average_change = 0
increase_profit = 0
increase_date = ""
decrease_profit = 0
decrease_date = ""
net_change_list = []
prev_profit = 0

with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)

    # Track the total and net change
    total_months += 1
    total_net += int(first_row[1])
    prev_profit = int(first_row[1])
    # Process each row of data
    for row in reader:
        row_net = int(row[1])
        # Track the total
        total_months += 1
        total_net += row_net
        # Track the net change
        change = row_net - prev_profit
        net_change_list.append(change)
        prev_profit = row_net

        # Calculate the greatest increase in profits (month and amount)
        if change > increase_profit:
            increase_date = row[0]
            increase_profit = change
        # Calculate the greatest decrease in losses (month and amount)
        if change < decrease_profit:
            decrease_date = row[0]
            decrease_profit = change

# Calculate the average net change across the months
average_change = sum(net_change_list)/ len(net_change_list)

# Generate the output summary
# Print the output
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_net}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {increase_date} (${increase_profit})")
print(f"Greatest Decrease in Profits: {decrease_date} (${decrease_profit})")

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("----------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${total_net}\n")
    txt_file.write(f"Average Change: ${average_change}\n")
    txt_file.write(f"Greatest Increase in Profits: {increase_date} (${increase_profit})\n")
    txt_file.write(f"Greatest Decrease in Profits: {decrease_date} (${decrease_profit})")