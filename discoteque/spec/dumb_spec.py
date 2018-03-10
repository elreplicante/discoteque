from mamba import *
from expects import *

with description('Mamba'):
    with it('works') as target:
        expect(True).to(equal(True))