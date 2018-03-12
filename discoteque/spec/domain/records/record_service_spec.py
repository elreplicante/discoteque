from mamba import description, it
from expects import *
from doublex import Spy, Mock, assert_that, called
from doublex_expects import *

from discoteque.infrastructure.records_repo import RecordsRepository
from discoteque.domain.records.record_service import RecordService
from discoteque.domain.records.record import Record


with description(RecordService):
    with description('Add records'):
        with before.each:
            self.records_repo = Spy(RecordsRepository)
            self.record_service = RecordService(self.records_repo)


        with it('calls the repo to save the record'):
            record = Record('And Justice For All', 'Metallica')

            result = self.record_service.save_record(record)

            assert_that(self.records_repo.save, called())
