class AddRecord:
    def __init__(self, record_service):
        self._record_service = record_service

    def execute(self, record):
        self._record_service.save_record(record)

