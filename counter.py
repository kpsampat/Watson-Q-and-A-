import csv
def csv_file():
    f1 = open('C:\\Users\\kishan.sampat\\Desktop\\fact_data.csv', 'r')
    f2 = open('C:\\Users\\kishan.sampat\\Desktop\\user_input.csv', 'r')
    f3 = open('C:\\Users\\kishan.sampat\\Desktop\\results.csv', 'w')
    c1 = csv.reader(f1)
    c2 = csv.reader(f2)
    c3 = csv.writer(f3)
    file1 = list(c1)
    list_count =len(file1)
    #print("target_file_count" , list_count)
    file2 = list(c2)    
    #list_count_ans =len(file2)
    #print("answer_file_count" , list_count_ans)

    count = 0
    for file1_row in file1:
        row = 1
        found = False
        results_row = file1_row  
        for file2_row in file2:
            #x = file2_row[0]
            if file1_row[0].lower() == file2_row[0].lower():
                results_row.append(" Found ")
                found = True
                count = count + 1
                break        
        row += 1 
        if not found:
            results_row.append('Not found')     
        c3.writerow(results_row)
    percentage = (count/list_count*100)
    #print("total percentage " , percentage)
    return percentage
    #print("total number of words matched" , count)
    f1.close()
    f2.close()
    f3.close()
 