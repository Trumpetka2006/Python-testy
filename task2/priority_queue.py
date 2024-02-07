class PriorityQueue:
    def __init__(self) -> None:
        self.mem = []
        pass

    def __len__(self):
        return len(self.mem)

    def push(self, name=str, prio=int):
        self.mem.append()
        pass

    pass


priority_queue = PriorityQueue()
priority_queue.push("Task 1", 3)
priority_queue.push("Task 2", 1)
priority_queue.push("Task 3", 2)

print("Priority Queue Length:", len(priority_queue))

print("Tasks in Priority Order:")
for task in priority_queue:
    print(task)

print("Processing tasks in Priority Order:")
while len(priority_queue) > 0:
    task = priority_queue.pop()
    print("Processing:", task)
