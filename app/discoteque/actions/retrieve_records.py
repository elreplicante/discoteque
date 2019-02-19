class RetrieveRecords:
    def __init__(self, records_repo):
        self._records_repo = records_repo

    def execute(self):
        return self._records_repo.find_all()
