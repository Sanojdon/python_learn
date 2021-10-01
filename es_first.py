from elasticsearch import Elasticsearch
from datetime import datetime

es = Elasticsearch(["127.0.0.1"], scheme="http", port=9200)

# Creating Data into Index
# mov = input("Enter movie name : ")
# dire = input("Enter director : ")
# mus = input("Enter music director : ")
# sta = input("Enter starring space seprated : ").split(",")
# rel = int(input("Release year : "))
# ids = int(input("Enter ID : "))

# document = {
# 	"name" : mov,
# 	"director" : dire,
# 	"music" : mus,
# 	"starring" : sta,
# 	"release" : rel,
# 	"created_date" : datetime.now()
# }

# es.index(index="movies_malayalam", doc_type="test", id=ids, body=document)


# Getting data by ID
# ind = int(input("Enter the ID to be searched : "))
# result = es.get(index="movies_malayalam", doc_type="test", id=ind)
# retrieved_document = result['_source']
# print("Name : ", retrieved_document["name"])
# print("Director : ", retrieved_document["director"])


# Updating by ID
# es.update(index="movies_malayalam", doc_type="test", id=18, body={"doc" : {"name" : "Changathipoocha"}})



# Querying Data from the Index
search_param = {
    'query': {
        'match': {
            'music': 'Dan Kan'
        }
    }
}
response = es.search(index="movies_malayalam", body=search_param)
results = response["hits"]["hits"]
print(results["_id"])
	
for i in results:
	data = i["_source"]
	print("ID : ", i["_id"])
	print("Film Name : ", data["name"])
	print("Starring : ", data["starring"])
	print("Release Year : ", data["release"])
	print("----------------------------------------------")


# Deleting Data from the index
# es.delete(index="movies_malayalam", doc_type="test", id=7)



# Updating multiple columns in an index
# source_to_update = {
# 	"doc" :{
# 		"release" : 1992,
# 		"created_date" : datetime.now()
# 	}
# }
# es.update(index="movies_malayalam", doc_type="test", id=7, body=source_to_update)


# Delete index in Elasticsearch
# es.indices.delete(index='reestr', ignore=[400, 404])