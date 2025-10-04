class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue operation
    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} added to the queue.")

    # Dequeue operation
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Nothing to dequeue.")
        else:
            removed = self.queue.pop(0)
            print(f"{removed} removed from the queue.")

    # Check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Display the queue
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue contents:", self.queue)

# Example usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()

q.dequeue()
q.display()
