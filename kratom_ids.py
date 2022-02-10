import json
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps

uri = "mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb][?options]]" # Temporary URI value
client = MongoClient(uri)

db = client.mirrulations
comments = db.comments
documents = db.documents
dockets = db.dockets


def get_comment_ids():
    file = open('comment_ids.json', 'w')
    file.write('[')
    for comment in comments.find({"data.attributes.comment": {"$regex": "kratom", "$options": "i"}},{"data.id": 1}):
        file.write(json.dumps(comment, default=str))
        file.write('\n')
    file.write(']')
    file.close()


def get_document_ids():
    file = open('document_ids.json', 'w')
    file.write('[')
    for document in documents.find({"data.attributes.title": {"$regex": "kratom", "$options": "i"}},{"data.id": 1}):
        file.write(json.dumps(document, default=str))
        file.write('\n')
    file.write(']')
    file.close()


def get_docket_ids():
    file = open('docket_ids.json', 'w')
    file.write('[')
    for docket in dockets.find({"data.attributes.title": {"$regex": "kratom", "$options": "i"}},{"data.id": 1}):
        file.write(json.dumps(docket, default=str))
        file.write('\n')
    file.write(']')
    file.close()


if __name__ == '__main__':
    get_comment_ids()
    get_document_ids()
    get_docket_ids()
