import csv

# This function reads data from a CSV file
def read_data():
    # Opens the sales.csv file in read mode
    with open('sales.csv', 'r') as sales_csv:
        # Uses the csv library to read the file as a dictionary
        spreadsheet = csv.DictReader(sales_csv)
        # Goes through each row in the CSV and adds it to a list
        data = [row for row in spreadsheet]
    # Returns the list of data
    return data

# This function writes the summary of calculations to a CSV file
def write_summary(total, average, change_percentages, highest_month, lowest_month):
    # Opens the sales_summary.csv file in write mode
    with open('sales_summary.csv', 'w', newline='') as file:
        # Creates a CSV writer object
        writer = csv.writer(file)
        # Writes the header row to the summary file
        writer.writerow(['Total Sales', 'Average Sales', 'Monthly Change Percentages', 'Highest Month', 'Lowest Month'])
        # Writes the calculated data to the summary file
        writer.writerow([total, average, change_percentages, highest_month, lowest_month])

# The main function that deals with reading, calculating, and writing data
def run():
    # Reads data from the CSV file
    data = read_data()
    # Extracts the 'sales' column from the data
    sales = [int(row['sales']) for row in data]

    # Calculates total sales by summing up the sales column
    total_sales = sum(sales)

    # Calculates average sales by dividing total sales by the number of entries
    average_sales = total_sales / len(sales)

    # Calculates monthly changes as a percentage list
    monthly_changes = []
    # Loops through the sales starting from the second month
    for i in range(1, len(sales)):
        # Calculates the percentage change from the previous month
        change = (sales[i] - sales[i - 1]) / sales[i - 1] * 100
        # Adds the percentage change to the list
        monthly_changes.append(change)

    # Finds the month with the highest and lowest sales
    highest_sales = max(sales)
    lowest_sales = min(sales)
    # Finds the month names for the highest and lowest sales
    highest_month = data[sales.index(highest_sales)]['month']
    lowest_month = data[sales.index(lowest_sales)]['month']

    # Writes the summary of our calculations to a new CSV file
    write_summary(total_sales, average_sales, monthly_changes, highest_month, lowest_month)

    # Prints out the results
    print(f'Total Sales: {total_sales}')
    print(f'Average Sales: {average_sales}')
    print(f'Monthly Change Percentages: {monthly_changes}')
    print(f'Highest Month: {highest_month} with {highest_sales} sales')
    print(f'Lowest Month: {lowest_month} with {lowest_sales} sales')

# Executes the main function
run()