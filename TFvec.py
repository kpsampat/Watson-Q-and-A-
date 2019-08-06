from sklearn.feature_extraction.text import TfidfVectorizer
def statement(text1,text2):
        vect = TfidfVectorizer(min_df=1)
        tfidf = vect.fit_transform([text1,text2])
        i = (tfidf * tfidf.T).A
        item_final = i.item(2)
        return item_final
    
def main():
    with open('C:\\Users\\kishan.sampat\\Desktop\\user_input.txt', 'r') as file1:

        with open('C:\\Users\\kishan.sampat\\Desktop\\fact.txt', 'r') as file2:

            value = []
            per = []
            for text1 in file1:
                #print("file1 text " , text1)
                #pass
                
                for text2 in file2:
                    #print("file2 text" , text2)
                    var1 = statement(text1,text2)
                    var = var1*100 
                    value.append(var)
                    #print("append value " , value)
                    value_percent = sum(value)/len(value)
                    per = value_percent
                    #print("total " , per)
                    break
            return per

