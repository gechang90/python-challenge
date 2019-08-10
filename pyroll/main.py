import os
import csv

pyroll_path = os.path.join('Resources','election_data.csv')
with open(pyroll_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter = ',')
    header = next(csv_reader)
    
    total_votes = 0
    Khan_count = 0
    Correy_count = 0
    Li_count = 0
    OTooley_count = 0

    for row in csv_reader:
        total_votes +=1
        if row[2] == 'Khan':
            Khan_count+=1
        elif row[2] == 'Correy':
            Correy_count+=1
        elif row[2] == 'Li':
            Li_count +=1
        else:
            OTooley_count +=1

    print(f'Election Results\n-------------------------\nTotal Votes: {total_votes}\n-------------------------')
    print(f'Khan: {round(Khan_count/total_votes*100,5)}% ({Khan_count})')
    print(f'Correy: {round(Correy_count/total_votes*100,5)}% ({Correy_count})')
    print(f'li: {round(Li_count/total_votes*100,5)}% ({Li_count})')
    print(f"O'Tooley: {round(OTooley_count/total_votes*100,5)}% ({OTooley_count})\n-------------------------\nWinner: Khan\n-------------------------")





