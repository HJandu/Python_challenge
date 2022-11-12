import os
import csv

#define the variables
months=[]
profit_loss_changes=[]
Total_months=0
n_profit_loss=0
p_month_profit_loss=0
c_month_profit_loss=0
profit_loss_change=0 

#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The changes in "Profit/Losses" over the entire period, and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period

#path to collect data from my folder (check if this works) 
budget_data_csv=os.path.join("Resources","budget_data.csv")

#open and read file
with open(budget_data_csv) as csv_file:
    csv_reader=csv.reader(csv_file, delimiter=",")



    #Read the header row first
    csv_header=next(csv_reader)
    # print(f"Header: {csv_header} ")
    print(csv_header)

    #Read through each row
    for row in csv_reader:
        #Total number of months
        Total_months+=1
        
        #The net total amount of "Profit/Losses" over the entire period
        c_month_profit_loss=int(row[1])
        n_profit_loss+=c_month_profit_loss

        if (Total_months==1):
            #previous month to be equal to current month
            p_month_profit_loss = c_month_profit_loss
            continue

        else:
            #calculate chane in profit loss
            profit_loss_change = c_month_profit_loss - p_month_profit_loss

            #append every month
            months.append(row[0])
            
            profit_loss_changes.append(profit_loss_change)
            p_month_profit_loss = c_month_profit_loss

    #the average of those changes
    Total_profit_loss=sum(profit_loss_changes)
    average_profit_loss=round(Total_profit_loss/(Total_months-1), 2)

    #greatest increase and greatest decrease
    greatest_increase = max(profit_loss_changes)
    greatest_decrease = min(profit_loss_changes)

    greatest_month=profit_loss_changes.index(greatest_increase)
    least_month=profit_loss_changes.index(greatest_decrease)

    b_month=months[greatest_month]
    w_month=months[least_month]


#print the results
print("Financial Analysis")
print("----------------------------------")
print(f"Total Months:   {Total_months}")
print(f"Total:    ${n_profit_loss}")
print(f"Average Change:    ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {b_month}  (${greatest_increase})")
print(f"Greatest Decrease in Losses:  {w_month}  (${greatest_decrease})")

#Export a text file
budget_file = os.path.join("Output", "budget_data.txt")
with open(budget_file, "w") as outfile:
    outfile.write("Finacial Analysis\n")
    outfile.write("------------------------\n")
    outfile.write(f"Total Months:    {Total_months}\n")
    outfile.write(f"Average Change:    ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {b_month}  (${greatest_increase})\n")
    outfile.write(f"Greatest Increase in Profits:  {b_month}  (${greatest_increase})\n")
    outfile.write(f"Greatest Decrease in Losses:  {w_month}  (${greatest_decrease})\n")