import pytest
from cache_lib import CachedDict
import time
@pytest.fixture(scope='module')
def cd():
    cd = CachedDict()
    yield cd

def test_cacheIt(cd):
    assert cd.cacheIt('a', 10) == '<CachedItem {a:10} last updated with frequency 1>'
    assert cd.cacheIt('b', 11) == '<CachedItem {b:11} last updated with frequency 1>'
    time.sleep(2)
    assert cd.cacheIt('c', 12) == '<CachedItem {c:12} last updated with frequency 1>'
    assert cd.cacheIt('c', 13) == '<CachedItem {c:13} last updated with frequency 2>'
    time.sleep(2)
    assert cd.cacheIt('b', 13) == '<CachedItem {b:13} last updated with frequency 2>'
    time.sleep(1)
    assert cd.cacheIt('a', 13) == '<CachedItem {a:13} last updated with frequency 2>'
    time.sleep(1)
    assert cd.cacheIt('c', [1, 2, 3]) == '<CachedItem {c:[1, 2, 3]} last updated with frequency 3>'
    assert cd.cacheIt('f', {'a': 1, 'b': 2}) == '<CachedItem {f:{\'a\': 1, \'b\': 2}} last updated with frequency 1>'
