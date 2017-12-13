"Timeout dummy cache backend"

from django.core.cache.backends.base import DEFAULT_TIMEOUT

class TimeoutDummyCache():
    def __init__(self, *args, **kwargs):
        self.last_timeout = [] # Start out with empty list for easy testing

    def add(self, key, value, timeout=DEFAULT_TIMEOUT, version=None):
        self.last_timeout = timeout
        return True

    def get(self, key, default=None, version=None):
        return default

    def set(self, key, value, timeout=DEFAULT_TIMEOUT, version=None):
        self.last_timeout = timeout

    def delete(self, key, version=None):
        pass

    def has_key(self, key, version=None):
        return False

    def clear(self):
        pass

    def get_last_timeout(self):
        return self.last_timeout
