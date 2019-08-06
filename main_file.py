import ibm_nlu_user_data as nlp
import TFvec as TF
import sim as similarity
import cosine
import counter_list 
#import speech_to_text as speechtext
#sp = speechtext.speech()
#print(sp)
nlp.nlu_data()
count_percentile = counter_list.csv_file()
print("keywords matched ===>>> " , count_percentile , "%")

if count_percentile >= 20:
    print('ok')
    x_sim = similarity.main()    
    print("similarity score ===>>> " , x_sim ,"%")
    v = cosine.main()
    val_v = v*100
    print("cosine similarity value  ===>> " , val_v,"%")
    Term = TF.main()
    print("Vector Model ===>>> " , Term , "%")
    total_Score_calc = (count_percentile*0.50+(x_sim*0.16+val_v*0.18+Term*0.16))  
    #its score multiply be weights
    print("Total Score ==> " , total_Score_calc,"%")  
    
else:
    print('fail')




