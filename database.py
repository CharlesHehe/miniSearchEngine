class Database:
    def __init__(self):
        self.db = {}

    def add(self, document):
        self.db.update({document['id']: document})

    def get(self, id):
        return self.db.get(id)

    def remove(self, document):
        self.remove(document['id'])
