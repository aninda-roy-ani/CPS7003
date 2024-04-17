import random
import string


class SimulatedMongoCollection:
    def __init__(self):
        self.documents = []

    def insert_one(self, document):
        document_id = "".join(random.choices(string.ascii_letters + string.digits, k=10))
        document['_id'] = document_id
        self.documents.append(document)
        return document

    def aggregate(self, pipeline):
        aggregated_data = self.documents
        for stage in pipeline:
            if '$match' in stage:
                aggregated_data = [doc for doc in aggregated_data if all(k in doc and doc[k] == v for k,v in stage['$match'].items())]
            elif '$group' in stage:
                group_field = stage['group']['_id']
                accumulator = next(iter(stage['$group'].values()))
                if '$sum' in accumulator:
                    aggregated_data = [{group_field: sum(doc[accumulator['$sum']] for doc in aggregated_data)}]
            return aggregated_data


collection = SimulatedMongoCollection()

for i in range(5):
    collection.insert_one({'name':'Sample', 'value':i})

pipeline = [
    {'$match':{'name':'Sample'}},
    {'$group':{'_id':'total','total_value':{'$sum':'value'}}}
]

aggregated_result = collection.aggregate(pipeline)

for doc in aggregated_result:
    print(doc)


'''
document_id = "".join(random.choices(string.ascii_letters + string.digits, k=10))
print(document_id)
'''
