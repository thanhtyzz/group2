import subprocess
import os


#check pip is exits
try:
    subprocess.check_output(["pip", "--version"])
    subprocess.call(["pip", "install", "--upgrade", "pip"])
except:
    command  = """curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py"""
    #run command
    subprocess.call(command, shell=True)
    #install pip
    subprocess.call(["python", "get-pip.py"])
    #remove get-pip.py
    os.remove("get-pip.py")
    #update pip
    subprocess.call(["pip", "install", "--upgrade", "pip"])


#install requirements
subprocess.call(["pip", "install", "-r", "requirements.txt"])

from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
import ctypes

#prepare for database
load_dotenv(find_dotenv())
host = os.getenv("HOSTNAME")
client = MongoClient(host)
#check there was database named group2 in client
if "group2" in client.list_database_names():
    print("Database already existed")
    db = client['group2']
else:
    #create database
    db = client['group2']
    print("Database created")

#check there was collection named users in db
def import_user_data():
    with open("./Data/users.json", "r") as f:
        data = f.read()

    for element in eval(data):
        #check element is in collection
        if element["Username"] not in db["users"].find({}).distinct("Username"):
            db["users"].insert_one(element)
        else:
            continue
    print("Imported Users' data successfully")
if "users" in db.list_collection_names():
    print("Collection Users already existed")
    #import data from ./Data/users.json
    import_user_data()

else:
    collection = db.create_collection("users")
    print("Collection Users created")
    #import data from ./Data/users.json to collection
    import_user_data()

#check there was collection named warehouse in db
def import_warehouse_data():
    with open("./Data/warehouse.json", "r") as f:
        data = f.read()

    for element in eval(data):
        #check element is in collection
        if element["Film_ID"] not in db["warehouse"].find({}).distinct("Film_ID"):
            db["warehouse"].insert_one(element)
        else:
            continue
    print("Imported Warehouse's data successfully")

if "warehouse" in db.list_collection_names():
    print("Collection Warehouse already existed")
    #import data from ./Data/warehouse.json
    import_warehouse_data()
else:
    collection = db.create_collection("warehouse")
    print("Collection Warehouse created")
    #import data from ./Data/warehouse.json to collection
    import_warehouse_data()

#check there was collection named invoices in db
def import_invoice_data():
    #import data from ./Data/invoices.json to collection
    with open("./Data/invoices.json", "r") as f:
        data = f.read()

    for element in eval(data):
        #check element is in collection
        if element["Invoice_ID"] not in db["invoices"].find({}).distinct("Invoice_ID"):
            db["invoices"].insert_one(element)
        else:
            continue
    print("Imported invoices' data successfully")


if "invoices" in db.list_collection_names():
    print("Collection Invoices already existed")
    #import data from ./Data/invoices.json
    import_invoice_data()
else:
    collection = db.create_collection("invoices")
    print("Collection Invoices created")
    #import data from ./Data/invoices.json to collection
    import_invoice_data()

#notification on the screen for user downloaded successfully, donot use tkinter
ctypes.windll.user32.MessageBoxW(0, "Setup successfully!!!!!\nWe love coding  <3", "group2", 1)
