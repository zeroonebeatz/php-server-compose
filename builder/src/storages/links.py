class Links:
    store = {}

    def __init__(self, store):
        self.store = store

    def exists(self, key: str):
        return key in self.store

    def get(self, key: str):
        return self.store[key]
