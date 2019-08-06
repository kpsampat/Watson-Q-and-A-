

# FACT DATA USED TO EVALUATE THE USER DATA IN IBM_NLU_DATA

from __future__ import print_function
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
def nlu_fact():
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2017-02-27',
        username='f7aef59a-55c0-4999-a510-9174026922ea',
        password='SUcyG6MXKWiY')
    r = open("C:\\Users\\kishan.sampat\\Desktop\\fact.txt","r")
    extracted = r.read()    

    response = natural_language_understanding.analyze(

        text= extracted,
   
        features=Features(entities=EntitiesOptions(sentiment=True,limit=3), keywords=KeywordsOptions())) 
    #print(response)
   # print(json.dumps(response, indent=5))
    #json_parsed = json.dumps(response)
    #print(json_parsed)
    with open('C:\\Users\\kishan.sampat\\Desktop\\fact_data.csv', 'w') as outfile:
        #json.dump(response , outfile)
        for each in response['keywords']:
            tex = each['text']
            lemet = porter_stemmer.stem(tex)
            #print(lemet)
            json.dump(lemet , outfile)
            outfile.write('\n')
        for ent in response['entities']:
            ents = ent['text']
            lemet_ent = porter_stemmer.stem(ents)
            #print(lemet_ent)
            json.dump(lemet_ent , outfile)
            outfile.write('\n')

nlu_fact()