import time

class Stopwatch(object):
    """A simple timer class"""
    
    def __init__(self):
        pass
    def start(self):
        """Starts the timer"""
        self.start = time.time()
        return self.start
    
    def stop(self):
        """Stops the timer.  Returns the time elapsed"""
        self.stop = time.time()
        return (self.stop - self.start)
    
    def now(self, message="Now: "):
        """Returns the current time with a message"""
        return time.time()
    
    def elapsed(self, message="Elapsed: "):
        """Time elapsed since start was called"""
        return (time.time() - self.start)
    
    def split(self, message="Split started at: "):
        """Start a split timer"""
        self.split_start = datetime.datetime.now()
        return self.split_start
    
    def unsplit(self, message="Unsplit: "):
        """Stops a split. Returns the time elapsed since split was called"""
        return datetime.datetime.now() - self.split_start

