import csv
def csv_file():
    f1 = open('C:\\Users\\kishan.sampat\\Desktop\\fact_data.csv', 'r')
    f2 = open('C:\\Users\\kishan.sampat\\Desktop\\user_input.csv', 'r')
    c1 = csv.reader(f1)
    c2 = csv.reader(f2)
    file1 = list(c1)
    file2 = list(c2)    

    count =[]
    row = 0
    for file1_row in file1:
        print('cycle:', row)
        print("fact_data column",file1_row)
        
        for column in file1_row:  
            print('check row in file user_input=',file2[row])
            print("column======",column)
            if(column in file2[row]):
                if (row >= len(count)):
                    print('we found-adding 1',column)
                    count.append(1)
                    print("count",count)
                else:
                    print('we found-sum',column)
                    count[row]= count[row]+ 1
                    print("count[row]==>>> ", count[row])
            
        if(row>=len(count)):
            count.append(0)   
        row += 1
    row = 0
    print(count)
    
    percentage=[]
    for count1 in count:
        print("file1[row]====>>.",file1[row])
        print("match ratio",count1,len(file1[row]),row)
        print(file1[row])
        percentage.append(count1/len(file1[row])*100)
        row+=1 
    percent = (sum(percentage)/len(percentage))
    return percent

    f1.close()
    f2.close()
csv_file()