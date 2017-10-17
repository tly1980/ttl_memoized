import threading
import time


class memoized(object):
  def __init__(self, ttl=2):
    self._var = threading.local()
    self._var.cache = {}
    self._var.ttl = ttl

  def __call__(self, func):
    def _memoized(*args):
      self._var.func = func
      now = time.time()
      try:
        value, last_update = self._var.cache[args]
        age = now - last_update
        if age > self._var.ttl:
            raise AttributeError
        return value

      except (KeyError, AttributeError):
        value = self._var.func(*args)
        self._var.cache[args] = (value, now)
        return value

      except TypeError:
          return self._var.func(*args)
    return _memoized
