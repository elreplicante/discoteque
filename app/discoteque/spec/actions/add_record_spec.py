from mamba import description, it
from doublex import Spy, Mock, assert_that, called

from app.discoteque.actions.add_record import AddRecord
from app.discoteque.domain.records.record_service import RecordService
from app.discoteque.infrastructure.records_repo import RecordsRepository

with description(AddRecord):
    with description('with no records on the list'):
        with before.each:
            self.records_repo = Mock(RecordsRepository)
            self.record_service = Spy(RecordService(self.records_repo))

        with it('calls the repo to save the record'):
            action = AddRecord(self.record_service)

            result = action.execute({
                'name': 'And Justice For All',
                'artist': 'Metallica'
            })

            assert_that(self.record_service.save_record, called())
