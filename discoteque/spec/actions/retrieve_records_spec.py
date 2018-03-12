from mamba import description, it
from expects import *
from doublex import Stub

from discoteque.actions.retrieve_records import RetrieveRecords
from discoteque.domain.records.record import Record
from discoteque.infrastructure.records_repo import RecordsRepository


with description(RetrieveRecords):
    with before.each:
        self.records_repo = Stub(RecordsRepository)

    with description('with no records on the discoteque'):
        with before.each:
            with self.records_repo:
                self.records_repo.find_all().returns([])

        with it('returns no records'):
            action = RetrieveRecords(self.records_repo)
            result = action.execute()

            expect(result).to(equal([]))

    with description('with some records on the discoteque'):
        with before.each:
            self.dumb_record = Record('Mötorhead', 'Ace Of Spades')
            self.records = [self.dumb_record]

            with self.records_repo:
                self.records_repo.find_all().returns(self.records)

        with it('returns all records'):
            action = RetrieveRecords(self.records_repo)
            result = action.execute()

            expect(result).to(contain(self.dumb_record))
