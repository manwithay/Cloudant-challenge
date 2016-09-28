from dao import get_doc,get_all_docs,put_doc,create_db,get_db_details,get_all_dbs
import json
import requests
import re

#GET document
def controller_get_doc(db_name,doc_name):
    output = get_doc(db_name,doc_name)
    return output

#GET all documents in the database
def controller_get_all_docs(db_name):
    output = get_all_docs(db_name)
    return output

#POST document
def controller_put_doc(db_name,doc_name,jsonstring):
    jsondata = json.loads(jsonstring)
    Keys = jsondata.keys()    
    for index in range(len(Keys)):
        m = list(Keys)[index]
        if m[0]=='_':
            return "Please check for keys, it should not start with an underscore!"
        else:
            j = json.loads(jsondata)
            output = requests.put("https://manwitha.cloudant.com/challenge/grabvgpes",
             auth=("manwitha", "Reddy@24"),
             headers={"content-type":"application/json"},
             data=json.dumps(j))
            return output
    
#CREATE database
def controller_create_db(db_name):
    pattern = re.compile("^[a-z]+[a-z,0-9,!,_, $, (, ), +, -,/]*$")
    matching = pattern.match(db_name)
    if matching is not None:
        out = requests.put("https://manwitha.cloudant.com/db_name",
             auth=("manwitha", "Reddy@24"))
        return out.json()

#GET details of a database
def controller_get_db_details(db_name):
    out = requests.get("https://manwitha.cloudant.com/db_name",
             auth=("manwitha", "Reddy@24"))
    return out.json()

#GET all databases
def controller_get_all_dbs():
    out = requests.get("https://manwitha.cloudant.com/_all_dbs",
             auth=("manwitha", "Reddy@24"))
    return out.json()

             

