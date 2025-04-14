from queue import Queue

q = Queue()
q.put("database")
print(q.qsize())
print(q.get())