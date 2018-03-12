class RecordsRepository:
    _records = []

    def find_all(self):
        return self._records

    def save(self, record):
        self._records.append(record)
