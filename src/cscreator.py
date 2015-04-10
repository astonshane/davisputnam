import threading
from helpers import *

#clause set creator class:
#   needed for the multithreading in order to ensure values are added to append correctly

class csCreator(object):
    def __init__(self):
        self.lock = threading.Lock()
        self.value = []

    #waits for the lock and then adds the next clause to the clauseSet
    def append(self, i):
        self.lock.acquire()
        try:
            #make sure that we aren't adding duplicates to the clauseSet
            if not clauseIn(i, self.value):
                self.value.append(i)
        finally:
            self.lock.release()
