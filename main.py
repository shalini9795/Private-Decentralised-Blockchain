import requests
import streamlit as st
from jsonify.convert import jsonify
from pymongo import MongoClient
import pymongo
import json
from pymongo import MongoClient

st.title('Private Decentralised KYC Blockchain')

def get_database():

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    myclient = pymongo.MongoClient("mongodb://localhost:5011/")

    mydb = myclient["KYCDatabase"]
    print("database created")
    # Create the database for our example (we will use the same database throughout the tutorial
    return mydb

def saveDB(name,aadhar,pan,address,phone):
    mydb=get_database()
    mycol = mydb["customers"]
    mydict = {"name":name , "address":address,"phone":phone,"aadhar":aadhar,"pan":pan}
    x = mycol.insert_one(mydict)
    print(x)


add_selectbox = st.sidebar.selectbox(
    "Private KYC Blockchain",
    ("Add Your Bank to Blockchain", "Add KYC Details","Show Detail")
)

def getDetails():
    st.header("Enter KYC Details to be Added")
    name = st.text_input("FullName", "Shalini Singh")
    aadhar = st.text_input("Aadhar", "Aadhar")
    pan = st.text_input("PAN", "PAN card")
    address = st.text_input("Address", "Address")
    phone = st.text_input("Phone", "Phone")
    payload={
        "name":name,
        "aadhar":aadhar,
        "pan":pan,
        "address":address,
        "phone":phone
    }
    if st.button('Add Details'):
        print("payload is",payload)
        try:
            st.write("Details Added for", name)
            r = requests.get("http://127.0.0.1:5011/mine_block", data=json.dumps(payload))
            st.write(r.content)
            try:
                r = requests.post("http://127.0.0.1:5011/add_transaction", data=json.dumps(payload))
                print("r", r)
                st.write(r.content)


                userdata = {"data": []}
                user = {}
                user["name"]: name
                user["aadhar"]: aadhar
                user["pan"]: pan
                user["address"]: address
                user["phone"]: phone
                userdata["data"].append(user)
            except Exception as e:
                st.write("Connection Issues in adding Transaction")
            try:
                r = requests.get("http://127.0.0.1:5011/replace_chain", data=json.dumps(payload))
            except:
                st.write(r.content)
                st.write("Connection Issues in adding data for other nodes")
            # saveDB(name,aadhar,pan,address,phone)
        except:
            st.write(r.content)
            st.write("Connection Issues in mining block")

def addBank():
    st.header("Enter Bank Node to be added")
    name = st.text_input("Node", "5002")
    bankname=st.text_input("Bank name", "ICICI")


    r = requests.get("http://127.0.0.1:5011/is_valid")

    if st.button('Add Your Bank to Blockchain'):
        r = requests.get("http://127.0.0.1:5011/is_valid")
        # r = requests.post("http://127.0.0.1:5011/connect_node", data=json.dumps(payload))
        st.write(r.content)
        payload = {
            "nodes": ["http://127.0.0.1:5002",
                      "http://127.0.0.1:5003"]
        }
        r = requests.post("http://127.0.0.1:5010/connect_node", data=json.dumps(payload))
        st.write("message:All the nodes are now connected. The Blockchain now contains the following Bank nodes:")
        st.write("Added Bank",bankname)
        st.write("All Bank Nodes: [0.0.0.1:5001,0.0.0.1:5002,0.0.0.1:5003]")
        # r = requests.get("http://127.0.0.1:5011/get_chain")
        # st.write(r.content)

def retreiveDetail():
    st.text("Retreiving..")
    r = requests.get("http://127.0.0.1:5011/is_valid")
    st.write(r.content)
    r = requests.get("http://127.0.0.1:5011/get_chain")
    st.write(r.content)

if add_selectbox == 'Add Your Bank to Blockchain':
    print ("Adding the bank to blockchain")
    addBank()

elif add_selectbox == "Add KYC Details":
    getDetails()
else:
    retreiveDetail()
    print("Authenticated")

