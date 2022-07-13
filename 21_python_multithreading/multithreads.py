import threading
import time

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter, delay):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
      self.delay = delay
   def run(self):
      print ("\nStarting " + self.name)
      print_time(self.name, self.counter, self.delay)
      print ("\nExiting " + self.name)

      

def print_time(threadName, counter, delay):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print ("\n%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

      

# Create new threads
thread1 = myThread(1, "Thread-1", 2, 1)
thread2 = myThread(2, "Thread-2", 3, 0.4)
thread3 = myThread(3, "Thread-3", 5, 3)

# Start new Threads
thread1.start()
thread2.start()
thread3.start()

print ("\nExiting Main Thread")
