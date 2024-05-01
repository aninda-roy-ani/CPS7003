import datetime
import random

class SimulatedMongoDBCollection:
    def __init__(self):
        self.documents = []

    def insert_one(self, document):
        self.documents.append(document)
        return {"inserted_id": len(self.documents)}

    def find(self, query=None):
        return self.documents


class IoTDataCollector:
    def __init__(self):
        self.collection = SimulatedMongoDBCollection()

    def collect_sensor_data(self):
        sensor_data = {
            'temperature':round(random.uniform(20.0, 30.0), 2),
            'humidity':round(random.uniform(30.0, 50.0), 2),
            'timestamp':datetime.datetime.now()
        }
        return sensor_data

    def insert_sensor_data(self):
        result = self.collection.insert_one(self.collect_sensor_data())
        print(f"Inserted data: {result['inserted_id']}")

def main():
    iot_collector = IoTDataCollector()
    for _ in range(5):
        iot_collector.insert_sensor_data()

    all = iot_collector.collection.find()
    for a in all:
        print(a)

main()