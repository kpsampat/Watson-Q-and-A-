from __future__ import print_function
from flask import Flask, request
import ibm_nlu_user_data as nlp
import TFvec as TF
import sim as similarity
import cosine
import counter_list 
import json
from watson_developer_cloud import DiscoveryV1
from bs4 import BeautifulSoup
from flask import jsonify

app = Flask(__name__)

@app.route('/getresult', methods=['GET'])
def my_form():

    nlp.nlu_data()
    count_percentile = counter_list.csv_file()
    print("keywords matched ===>>> " , count_percentile , "%")
    if count_percentile >= 25:
        print('ok')
        x = similarity.main()    
        print("similarity score ===>>> " , x,"%")
        v = cosine.main()
        val_v = v*100
        print("cosine similarity value  ===>> " , val_v,"%")
        T = TF.main()
        print("Vector Model ===>>> " , T , "%")
        total_Score_calc = str((count_percentile*0.50+(x*0.16+val_v*0.17+T*0.16)))  
        print("Total Score ==> " , total_Score_calc,"%") 
        json_format_keywords = json.dumps(count_percentile)
        json_format_tf = json.dumps(T)
        json_format_cosine = json.dumps(val_v)
        json_format_similarity = json.dumps(x)
        json_format_Total = json.dumps(total_Score_calc)
        
    else:
        return str("fail")

    return jsonify(json_format_keywords,json_format_similarity,json_format_cosine,json_format_tf,json_format_Total)

@app.route('/discover_input', methods=['POST'])

def discovery_input():
    
    discovery = DiscoveryV1(
    version='2018-03-05',
    username='a44582db-274d-4997-99ac-3492c0698da2',
    password='IDBSItjGztOC'
    )
    Query = request.form['text']
    my_query = discovery.query(environment_id='a6795f2b-bbde-4eb4-b80c-4d5d7f294ca8', collection_id='b4390ea5-d465-49c0-a439-a3a9a85cc2d6', query=Query , passages = 'true',count = '10')
    #print(json.dumps(my_query, indent=2))
    
    with open('C:\\Users\\kishan.sampat\\Desktop\\test.txt' , 'w', newline='') as outfile:
        for each in my_query['passages']:
                data = (each['passage_text'])
                soup = BeautifulSoup(data,"lxml")
                clean_data = soup.get_text()
                outfile.write(clean_data)
                
                return clean_data
            
@app.route('/user_input_test', methods=['POST'])

def user_post():
    
    text = request.form['text']
    processed_text = text.upper()
    f = open('user_input_test.txt','a')
    f.write(processed_text + "\n")
    f.close()
    
    return processed_text

@app.route('/fact_input_test', methods=['POST'])

def fact_post():
    
    text = request.form['text']
    processed_text = text.upper()
    f = open('fact_test.txt','a')
    f.write(processed_text + "\n")
    f.close()
    
    return processed_text
   
app.run(host='127.0.0.1', port=5000)