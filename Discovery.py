from watson_developer_cloud import DiscoveryV1
import json
from bs4 import BeautifulSoup

#reference link https://watson-api-explorer.ng.bluemix.net/apis/discovery-v1#!/Documents/addDocument
#developer tools link https://www.ibm.com/watson/developercloud/discovery/api/v1/python.html?python#query

def retrive():
    
    discovery = DiscoveryV1(
            version='2018-03-05',
            username='a44582db-274d-4997-99ac-3492c0698da2',
            password='IDBSItjGztOC'
            )
    environments = discovery.list_environments()
    print(json.dumps(environments, indent=2))

    configs = discovery.list_configurations('a6795f2b-bbde-4eb4-b80c-4d5d7f294ca8')
    print(json.dumps(configs, indent=2))
    
    #if collection does not exist create with code below
    #new_collection = discovery.create_collection(environment_id='a6795f2b-bbde-4eb4-b80c-4d5d7f294ca8', configuration_id='f4f12ffc-721d-41bb-bdb7-5613a735ce7f', name='ANS', description='trail' ,  language='en')
    #print(json.dumps(new_collection, indent=2))

    collections = discovery.list_collections('a6795f2b-bbde-4eb4-b80c-4d5d7f294ca8')
    print(json.dumps(collections, indent=2))

    Query = input("enter a query : ")
    my_query = discovery.query(environment_id='a6795f2b-bbde-4eb4-b80c-4d5d7f294ca8', collection_id='b4390ea5-d465-49c0-a439-a3a9a85cc2d6', query=Query , passages = 'true',count = '10')
    
    #print(json.dumps(my_query, indent=2))
    with open('C:\\Users\\kishan.sampat\\Desktop\\test.txt' , 'w', newline='') as outfile:
        for each in my_query['passages']:
                data = (each['passage_text'])
                soup = BeautifulSoup(data,"lxml")
                clean_data = soup.get_text()
                print(clean_data)
                outfile.write(clean_data)
            
            
retrive()



          