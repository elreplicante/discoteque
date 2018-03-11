class RecordsRepository:
    def __init__(self):
        self._records = []

    def find_all(self):
        return self._records
