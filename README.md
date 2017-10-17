# TTL Memoized - A memoized decorator with TTL support.

The idea of `memoized` is great, as some resources are expensive, so you want to cache it.

The python3 functools comes with LRU cache.

However, there isn't a memoized lib support TTL at the moment, or I haven't find any thing yet.

So I implement this lib to fill in the gap here.

The usage is simple, and the best way to explain it, is with my test cases:

```
def test_basic():

  @memoized(ttl=0.5)
  def a(name):
    return datetime.datetime.now()

  @memoized(ttl=0.5)
  def b(name, *args, **kwargs):
    return datetime.datetime.now()

  a1 = a(1)
  b1 = b(1, 2, 3, what='ever', you='want', to='be')

  for i in range(100):
    assert a1 == a(1)

  for i in range(100):
    assert b1 is b(1, 2, 3, what='ever', you='want', to='be')

  a2 = a(2)
  assert a2 != a1

  # let the cache expired...
  time.sleep(0.51)

  assert a(1) != a1
  assert b1 != b(1, 2, 3, what='ever', you='want', to='be')

```

