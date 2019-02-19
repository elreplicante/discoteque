class RecordService:
    def __init__(self, records_repo):
        self._records_repo = records_repo

    def save_record(self, record):
        self._records_repo.save(record)
