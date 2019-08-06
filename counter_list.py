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
        while '' in file1_row:
            file1_row.remove('')
        
        for column in file1_row:  
                
            if(column in file2[row]):

                if (row >= len(count)):
                    count.append(1)

                else:
                    count[row]= count[row]+ 1
                    #print("count[row]==>>> ", count[row])
            
        if(row>=len(count)):
            count.append(0)   
        row += 1
    row = 0
    
    percentage=[]
    for count1 in count:
        
        #print("match ratio","count1:",count1,"len(file1[row]):",len(file1[row]),"row:",row)
        percentage.append(count1/len(file1[row])*100)
        #print(percentage)
        row+=1 
        
    percent = (sum(percentage)/len(percentage))
    #print(percent)
    return percent

    f1.close()
    f2.close()
