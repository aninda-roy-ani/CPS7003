class SimulatedMongoDB:

    def __init__(self):
        self.database = {}

    def insert_one(self, collection, document):
        if collection not in self.database:
            self.database[collection] = []
        self.database[collection].append(document)
        return {'inserted_id': len(self.database[collection])-1}

    def find_one(self, collection, query):
        if collection in self.database:
            for document in self.database[collection]:
                if all(item in document.items() for item in query.items()):
                    return document
        return None

    def update_one(self, collection, query, update):
        if collection in self.database:
            for index, document in enumerate(self.database[collection]):
                if all(item in document.items() for item in query.items()):
                    for key, value in update.get('$set',{}).items():
                        document[key] = value
                    self.database[collection][index] = document
                    return {'matched_count':1, 'modified_count':1}
        return {'matched_count':0, 'modified_count':0}

    def delete_one(self, collection, query):
        if collection in self.database:
            for index, document in enumerate(self.database[collection]):
                if all(item in document.items() for item in query.items()):
                    del self.database[collection][index]
                    return {'deleted_count':1}
        return {'deleted_count':0}


if __name__ == "__main__":
    db = SimulatedMongoDB()

    print(db.insert_one('users',{'name':'Aninda Roy Ani', 'age':28}))

    print(db.find_one('users', {'name':'Aninda Roy Ani'}))

    print(db.update_one('users',{'name':'Aninda Roy Ani'}, {'$set':{'age':29}}))

    print(db.delete_one('users',{'name':'Aninda Roy Ani'}))