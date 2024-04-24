class SimulateNeo4jDatabase:
    def __init__(self):
        self.nodes = {}
        self.relationship = []

    def add_node(self, label, **properties):
        node_id = len(self.nodes) + 1
        self.nodes[node_id] = {'label': label, 'properties': properties}
        return node_id

    def add_relationship(self, from_node, to_node, relationship_type, **properties):
        self.relationship.append({
            'from': from_node,
            'to': to_node,
            'type': relationship_type,
            'properties': properties
        })

    def find_node(self, label, **properties):
        flag = True
        for node_id, node in enumerate(self.nodes.items()):
            if node['label'] == label:
                if not flag:
                    break
                for k, v in properties.items():
                    if node['properties'].get(k) == v:
                        pass
                    else:
                        flag = False
                        break
                if flag:
                    return node_id
        # return [node_id for node_id, node in self.nodes.items() if node['label'] == label and if all(node['properties'].get(k) == v for k,v in properties.items()

    def find_relationships(self, from_node=None, to_node=None, relation_type=None):
        return[ rel for rel in self.relationship if
                (from_node is None or rel['from'] == from_node) and
                (to_node is None or rel['to'] == to_node) and
                (relation_type is None or rel['type'] == relation_type)
                ]


db = SimulateNeo4jDatabase()

alice_id = db.add_node('User', name='Alice', age=30)
bob_id = db.add_node('User', name='Bob', age=30)

cooking_id = db.add_node('Interest', name='Cooking')

db.add_relationship(alice_id, cooking_id, 'INTERESTED_IN')
db.add_relationship(alice_id, bob_id, 'FRIENDS_WITH')

alice_interests_id = db.find_relationships(from_node=alice_id, relation_type='INTERESTED_IN')
alice_interest = [db.nodes[rel['to']]['properties']['name'] for rel in alice_interests_id]

print(f"Alice's interest: {alice_interest}")