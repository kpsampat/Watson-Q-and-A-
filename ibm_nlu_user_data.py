
# USER DATA WHO IS GIVING THE INTERVIEW USED TO COMPARE WITH IBM_NLU_FACT
from __future__ import print_function
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions
from nltk.stem.porter import PorterStemmer
import csv
porter_stemmer = PorterStemmer()
def nlu_data():
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2017-02-27',
        username='f7aef59a-55c0-4999-a510-9174026922ea',
        password='SUcyG6MXKWiY')
    r = open("C:\\Users\\kishan.sampat\\Desktop\\user_input.txt","r")
    extracted = r.read().splitlines()
    #print(extracted)
    mainArray = []
    
    for elements in extracted:
        array = []
        if len(elements)>0:
            #print(elements)
            response = natural_language_understanding.analyze(

            text= elements,
   
            features=Features(entities=EntitiesOptions(sentiment=True,limit=3), keywords=KeywordsOptions()))
            
            
            with open('C:\\Users\\kishan.sampat\\Desktop\\user_input.csv' , 'w', newline='') as outfile:
   
                for each in response['keywords']:
                    tex = each['text']
                    lemet = porter_stemmer.stem(tex)
                    array.append(lemet)   
                mainArray.append(array)
                csv.writer(outfile).writerows(mainArray)
                                        
        else:
            break
