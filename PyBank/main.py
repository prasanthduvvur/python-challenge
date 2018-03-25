
import csv
with open("budget_data_2.csv",newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    total_months=0
    total_revenue=0
    curr_revenue=0
    next_revenue=0
    sum_monthly_diff=0
    average_monthly_diff=0
    row_index=0
    local_diff=0
    max_diff=0
    min_diff=0

    next(csvreader,None)

    for row in csvreader:
        total_months+=1
        total_revenue+=int(row[1])
        if row_index == 0:
            curr_revenue=int(row[1])
            #print(f'current revenue is: {curr_revenue}')
        elif row_index >=1:
            next_revenue = int(row[1])
            sum_monthly_diff += next_revenue-curr_revenue
            local_diff=next_revenue-curr_revenue
            if local_diff > max_diff:
                max_diff=local_diff
                max_month=row[0]
            if local_diff < min_diff:
                min_diff=local_diff
                min_month=row[0]
            #print(f'{local_diff}')
            curr_revenue = next_revenue
        row_index+=1
        
    
    average_monthly_diff = sum_monthly_diff/(total_months-1)
    


    print("Financial Analysis")
    print("------------------")
    print(f'Total Months: {total_months}')
    print(f'Total Revenue: {total_revenue}')
    print(f'Average Monthly Revenue Change: {average_monthly_diff}')
    print(f'Greatest Increase in Revenue: {max_month} : {max_diff}')
    print(f'Greatest Decrease in Revenue: {min_month} : {min_diff}')




bankfile = open("PyBank2.out", 'w')
bankfile.write("Financial Analysis\n")
bankfile.write("------------------\n")
bankfile.write('Total Months: '+ str(total_months)+"\n")
bankfile.write('Total Revenue: '+ str(total_revenue)+"\n")
bankfile.write('Average Monthly Revenue Change: '+ str(average_monthly_diff)+"\n")
bankfile.write('Greatest Decrease in Revenue: '+ str(min_month)+ ':'+ str(min_diff)+"\n")
