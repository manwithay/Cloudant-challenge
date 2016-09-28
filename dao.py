import json
import requests

#GET document
def get_doc(db_name,doc_name):
    out = requests.get("https://manwitha.cloudant.com/db_name/doc_name",
             auth=("manwitha", "Reddy@24"))
    return out.json()

#GET all documents in the database
def get_all_docs(db_name):
    out = requests.get("https://manwitha.cloudant.com/db_name/_all_docs",
             auth=("manwitha", "Reddy@24"))
    return out.json()   #(or) out.text can be used 

#POST document
def put_doc(db_name,doc_name,jsondata):
    out = requests.put("https://manwitha.cloudant.com/db_name/doc_name",
             auth=("manwitha", "Reddy@24"),
             headers={"content-type":"application/json"},
             data=json.dumps(jsondata))
    return out.json()
    
#CREATE database
def create_db(db_name):
    out = requests.put("https://manwitha.cloudant.com/db_name",
             auth=("manwitha", "Reddy@24"))
    return out.json()

#GET details of a database
def get_db_details(db_name):
    out = requests.get("https://manwitha.cloudant.com/db_name",
             auth=("manwitha", "Reddy@24"))
    return out.json()

#GET all databases
def get_all_dbs():
    out = requests.get("https://manwitha.cloudant.com/_all_dbs",
             auth=("manwitha", "Reddy@24"))
    return out.json()

             

