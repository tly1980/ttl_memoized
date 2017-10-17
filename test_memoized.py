from memoized import memoized
import datetime
import time


def test_basic():

  @memoized(ttl=0.5)
  def t(name):
    return datetime.datetime.now()

  t1 = t('1')

  for i in range(10):
    assert t1 == t('1')

  time.sleep(0.51)

  assert t('1') != t1