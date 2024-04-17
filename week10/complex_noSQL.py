class SimulatedMongoDB:

    def __init__(self):
        self.database = {}

    def insert_one(self, collection, document):
        if collection not in self.database:
            self.database[collection] = []
        self.database[collection].append(document)
        return {'inserted_id': len(self.database[collection])-1}

    def find(self, collection, query):
        if collection in self.database:
            return [doc for doc in self.database[collection] if all(item in doc.items() for item in query.items())]
        '''
        if collection in self.database:
            for document in self.database[collection]:
                if all(item in document.items() for item in query.items()):
                    return document
                    '''
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

    def aggregate(self, collection, pipeline):
        result = self.database[collection]
        for stage in pipeline:
            if '$match' in stage:
                result = [doc for doc in result if all(item in doc.items() for item in stage['$match'].items())]
            elif '$group' in stage:
                group_field = stage['$group']['_id']
                group_values = set(doc[group_field] for doc in result)
                grouped_result = []
                for value in group_values:
                    group = {'_id':value}
                    for key,agg in stage['$group'].items():
                        if key != '_id':
                            if agg['$sum']:
                                group[key] = sum(doc.get(agg['$sum'],0) for doc in result if doc[group_field] == value)
                    grouped_result.append(group)
                result = grouped_result
            return result
        return []


if __name__ == "__main__":
    db = SimulatedMongoDB()

    db.insert_one('orders', {'customer_id': 1, 'amount': 100, 'status': 'shipped'})
    db.insert_one('orders', {'customer_id': 1, 'amount': 200, 'status': 'processing'})
    db.insert_one('orders', {'customer_id': 2, 'amount': 300, 'status': 'shipped'})
    db.insert_one('orders', {'customer_id': 3, 'amount': 400, 'status': 'shipped'})
    db.insert_one('orders', {'customer_id': 4, 'amount': 500, 'status': 'shipped'})

    orders = db.find('orders', {'status':'shipped'})
    print(db.find('orders', {'status':'shipped'}))

    pipeline = [
        {'$match': {'status':'processing'}},
        {'$group': {'_id':'customer_id', 'total_amount': {'$sum':'amount'}}}
    ]

    aggregated_orders = db.aggregate('orders',pipeline)
    for order in aggregated_orders:
        print(order)
