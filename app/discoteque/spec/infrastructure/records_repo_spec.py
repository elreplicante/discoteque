from mamba import description, it
from expects import *

from app.discoteque.domain.records.record import Record
from app.discoteque.infrastructure.records_repo import RecordsRepository

with description(RecordsRepository):
    with description('Add records'):
        with before.each:
            self.records_repo = RecordsRepository()

        with it('saves records'):
            record = Record('And Justice For All', 'Metallica')

            self.records_repo.save(record)
            records = self.records_repo.find_all()

            expect(records).to(have_len(1))
