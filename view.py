import web
from flask import Flask, jsonify
from dao import get_doc,get_all_docs,put_doc,create_db,get_db_details,get_all_dbs
from controller import controller_get_doc,controller_get_all_docs,controller_put_doc,controller_create_db,controller_get_db_details,controller_get_all_dbs
import requests
import json

app = Flask(__name__)

#GET all databases
@app.route('/', methods=['GET'])
def view_get_all_dbs():
    output = controller_get_all_dbs()
    return output

#CREATE database
@app.route('/<string:db_name>', methods=['POST'])
def view_create_db():
    output = controller_create_db(db_name)
    return output

#GET document   
@app.route('/<string:db_name>/<string:doc_name>', methods=['GET'])
def view_get_doc():
    output = controller_get_doc(db_name,doc_name)
    return output

#GET all documents in the database  
@app.route('/<string:db_name>', methods=['GET'])
def view_get_all_docs():
    output = controller_get_all_docs(db_name)
    return output

#POST document    
@app.route('/<string:db_name>/<string:doc_name>', methods=['POST'])
def view_put_doc():
    output = controller_put_doc(db_name,doc_name,request.json)
    return output


#GET details of a database
@app.route('/<string:db_name>/<string:doc_name>', methods=['GET'])
def view_get_db_details(db_name)
    output = controller_get_db_details(db_name):
    return output

   
if __name__ == '__main__':
    app.run(debug=True)
