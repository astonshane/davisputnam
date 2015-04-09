import threading
from helpers import *

class csCreator(object):
    def __init__(self):
        self.lock = threading.Lock()
        self.value = []

    def append(self, i):
        self.lock.acquire()
        try:
            if not clauseIn(i, self.value):
                self.value.append(i)
        finally:
            self.lock.release()
