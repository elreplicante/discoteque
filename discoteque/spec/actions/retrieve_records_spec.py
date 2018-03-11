from mamba import description, it
from expects import *
from doublex import Stub

from discoteque.actions.retrieve_records import RetrieveRecords
from discoteque.infrastructure.records_repo import RecordsRepository


with description('Retrieve records'):
    with description('with no records on the list'):
        with before.each:
            self.records_repo = Stub(RecordsRepository)
            with self.records_repo:
                self.records_repo.find_all().returns([])

        with it('retrieves no records'):
            action = RetrieveRecords(self.records_repo)
            result = action.execute()

            expect(result).to(equal([]))
