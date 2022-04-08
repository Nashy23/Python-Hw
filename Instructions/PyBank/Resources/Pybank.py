import csv
import os

# Defining our variables
mths = []
profits_losses = []
count_mths = 0
net_prof_loss = 0
prev_mth_prof_loss = 0
curr_mth_prof_loss = 0
prof_loss_chng = 0


# file path
bank_csv = os.path.join("..", "Resources", "budget_data.csv")

# Open and read csv
with open(bank_csv) as file:
    csv_reader = csv.reader(file, delimiter=",")
    csv_header = next(file)

    # Number of months included in dataset
    for row in csv_reader:
        
        # Count of months
         count_mths += 1
        # Net total ammount of profit/losses over entire period
         curr_mth_prof_loss = int(row[1])
         net_prof_loss += curr_mth_prof_loss
         continue
        
    if (count_mths == 1):
        # Make prvious month value equal to current month
        prev_mth_prof_loss = curr_mth_prof_loss
    
    else:
         # compute change in profit loss
         prof_loss_chng = curr_mth_prof_loss - prev_mth_prof_loss

         # Append each month
         mths.append(row[0])

         #Append each profit loss to prof_loss-chngs
         profits_losses.append(prof_loss_chng)

         # Make current month loss to previous month loss for next loop
         prev_mth_prof_loss = curr_mth_prof_loss

# Sum and Average changes in Profits/Losses over entire period
sum_prof_loss = sum(profits_losses)
avg_prof_loss = round(sum_prof_loss/(count_mths -1), 2)

# Highest and Lowest Change in Profits/Losses over entire period
high_chng = max(profits_losses)
low_chng = min(profits_losses)

# Locate index valueof highest and lowest changes over entire period
high_index = profits_losses.index(high_chng)
low_index = profits_losses.index(low_chng)

# Assign highest and lowest months
best = mths[high_index]
worst = mths[low_index]

# Print our analysys on GitBash
print("Financial Analysys")
print("------------------------")
print(f"Total Months: {count_mths}")
print(f"Total: ${net_prof_loss}")
print(f"Average Change: ${avg_prof_loss}")
print(f"Greatest Increase in Profits: {best} (${high_chng})")
print(f"Greatest Decrease in Losses: {worst} (${low_chng})")
    

    
      




