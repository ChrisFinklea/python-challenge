import os
import csv

#path to csv file
bank_csv = os.path.join("C:/Users/cmfjr/Desktop/class/Week3/python_challenge/PyBank/", "Resources", "budget_data.csv")

#Analysis Variables
num_of_months = 0
total_net_profit = 0
avg_net_profit = 0
greatest_increase = 0
greatest_decrease = 0
current_row_profit = 0
#previous_row_profit needs to be none to cover a scenario where the first months profit is zero
previous_row_profit = None
current_profit_difference = 0
total_profit_difference = 0
greatest_increase_date = ""
greatest_decrease_date = ""

#open bank_csv as csv_file
with open(bank_csv) as csv_file:
    
    #read in the file.  Commas are the delimiter
    csv_reader = csv.reader(csv_file,delimiter=',')
    
    #Storing the headers as csv_header
    csv_header=next(csv_reader)
    
    #Loop through each row of the csv
    for row in csv_reader:
        
        #Find profit of the current row
        current_row_profit = int(row[1])
        
        #Each row is a month so increasing the num_of_months by 1 for each row in the loop
        num_of_months = num_of_months + 1
        
        #Sums all profits/losses
        total_net_profit = total_net_profit + current_row_profit
        
        #Compares current profit and last months profit as long as it is not the first profit value
        if previous_row_profit is not None:
            #Calculates profit diffence between last and current profit value
            current_profit_difference = current_row_profit - previous_row_profit
            
            #If statement to set greatest increase and decrease change variable
            #Also gets date of change
            if current_profit_difference > greatest_increase:
                greatest_increase = current_profit_difference
                greatest_increase_date = row[0]
            elif current_profit_difference < greatest_decrease:
                greatest_decrease = current_profit_difference
                greatest_decrease_date = row[0]
            
            #Sums all profit diffences
            total_profit_difference = total_profit_difference + current_profit_difference
        
        #Updates previous profit with current
        previous_row_profit = current_row_profit

#Calculates average change
#Number of months is reduced by one because there is no change in profit calculated for the first month
avg_net_profit = total_profit_difference/(num_of_months-1)

#All prints
print("Financial Analysis")
print("----------------------------")
print("Total Months: "+str(num_of_months))
print("Total: $"+str(total_net_profit))
print("Average Change: $"+str(round(avg_net_profit,2)))
print("Greatest Increase in Profits: "+greatest_increase_date+" ($"+str(greatest_increase)+")")
print("Greatest Decrease in Profits: "+greatest_decrease_date+" ($"+str(greatest_decrease)+")")

#Open text file
with open("C:/Users/cmfjr/Desktop/class/Week3/python_challenge/PyBank/Analysis/Financial Analysis.txt", "w") as fa:
    # Write each line to the file
    fa.write("Financial Analysis\n")
    fa.write("----------------------------\n")
    fa.write("Total Months: " + str(num_of_months) + "\n")
    fa.write("Total: $" + str(total_net_profit) + "\n")
    fa.write("Average Change: $" + str(round(avg_net_profit, 2)) + "\n")
    fa.write("Greatest Increase in Profits: " + greatest_increase_date + " ($" + str(greatest_increase) + ")\n")
    fa.write("Greatest Decrease in Profits: " + greatest_decrease_date + " ($" + str(greatest_decrease) + ")\n")