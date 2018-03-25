
import csv
with open("election_data_1.csv",newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)
    voters = list(csvreader)

    total_votes=0
    list_of_candidates=[]
    vote_of_candidates=[]
    current_candidate=""
    number_of_candidates=0
    winner_votes=0
    winner=""

    

    for row in voters:
        total_votes+=1
        if row[2] not in list_of_candidates:
            list_of_candidates.append(row[2])
            vote_of_candidates.append(0)
            
    number_of_candidates = len(list_of_candidates)
    #print("number of candidates is: "+str(number_of_candidates) )
   
    i=0
    for i in range(number_of_candidates):
        for row in voters:
                #print(f'{row}')
                if row[2] == list_of_candidates[i]:
                    #print(f'candidate is: {row[2]}')
                    vote_of_candidates[i]+=1




    print("Election Results")
    print("---------------------------------------")
    print(f'Total Votes: {total_votes}')
    print("---------------------------------------")    
    #print(f'List of candidates: {list_of_candidates}')

    for i in range(number_of_candidates):
        if vote_of_candidates[i] > winner_votes:
            winner=list_of_candidates[i]
            winner_votes=vote_of_candidates[i]

        print(f'{list_of_candidates[i]} got {round((vote_of_candidates[i]/total_votes)*100)}% ({vote_of_candidates[i]})')

    print("---------------------------------------")
    print(f"And the grammy goes to: {winner}")
    print("---------------------------------------")


bankfile = open("PyPoll1.out", 'w')
bankfile.write("Election Results\n")
bankfile.write("---------------------------------------\n")
bankfile.write('Total Votes: '+ str(total_votes)+"\n")
bankfile.write("---------------------------------------\n")

for i in range(number_of_candidates):
    if vote_of_candidates[i] > winner_votes:
        winner=list_of_candidates[i]
        winner_votes=vote_of_candidates[i]

    bankfile.write(str(list_of_candidates[i])+ " got " + str(round((vote_of_candidates[i]/total_votes)*100)) +"% "+ "("+str(vote_of_candidates[i])+")"+"\n")

bankfile.write("---------------------------------------\n")
bankfile.write("And the grammy goes to: "+str(winner)+"\n")
bankfile.write("---------------------------------------\n")
