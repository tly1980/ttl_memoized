from ttl_memoized import memoized
import datetime
import time


def test_basic():

  @memoized(ttl=0.5)
  def a(name):
    return datetime.datetime.now()

  @memoized(ttl=0.5)
  def b(name, *args, **kwargs):
    return datetime.datetime.now()

  a1 = a(1)
  b1 = b(1, 2, 3, what='ever', you='want it', to='be')

  for i in range(100):
    assert a1 is a(1)

  for i in range(100):
    assert b1 is b(1, 2, 3, what='ever', you='want it', to='be')

  a2 = a(2)
  b2 = b(2, 2, 3, what='ever', you='want it', to='be')

  assert a2 != a1
  assert a2 != b2

  # # let the cache expired...
  time.sleep(0.51)

  assert a(1) != a1
  assert b1 != b(1, 2, 3, what='ever', you='want it', to='be')
