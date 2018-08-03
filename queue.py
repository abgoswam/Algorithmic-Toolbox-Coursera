class Queue:
    def __init__(self):
        self.store = [0] * 3
        self.i = 0
        self.j = 0

    def show(self):
        n = len(self.store)
        i_prime = (self.i + 1) % n

        while True:
            print(self.store[i_prime])
            if i_prime == self.j:
                break

            i_prime = (i_prime + 1) % n

    def enqueue(self, v):
        n = len(self.store)
        j_prime = (self.j + 1) % n

        if j_prime == self.i:
            print("Q Full")
            return False

        self.store[j_prime] = v
        self.j = j_prime
        self.show()
        return True

    def dqueue(self):
        if self.i == self.j:
            print("Q Empty")
            return None

        n = len(self.store)
        self.i = (self.i + 1) % n
        return self.store[self.i]


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)