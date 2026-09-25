class Stack:
    def __init__(self,size = 100):
        self.arr = [None] * size
        self.top = -1

    def push(self,x):
        if self.top >= len(self.arr) - 1 :
            print(f"Stack day ko the push {x}")
            return
        self.top += 1
        self.arr[self.top] = x

    def pop(self):
        if self.top == -1:
            return "Trong"
        x = self.arr[self.top]
        self.top -= 1
        return x

class Queue:
    def __init__(self,size = 100):
        self.arr = [None] * size
        self.front = 0
        self.rear = -1

    def enqueue(self,x):
        if self.rear >= len(self.arr) - 1:
            print(f"Queue day ko the them {x}")
            return
        self.rear += 1
        self.arr[self.rear] = x
        

    def unqueue(self):
        if self.front > self.rear:
            return "Trong"
        x = self.arr[self.front]
        self.front += 1
        return x

def to_binary(n):
    if n == 0:
        return "0"
    st = Stack()
    while n >0:
        st.push(n%2)
        n //= 2
    result = "" 
    while st.top != -1:
        result += str(st.pop())
    return result

if __name__ == "__main__":
    st = Stack(2)
    st.push(10)
    st.push(20)
    st.push(30)
    print("Stack pop:",st.pop())
    print("Stack pop:",st.pop())
    q = Queue(2)
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("Queue dequeue:",q.unqueue())
    print("Queue dequeue:",q.unqueue())
    number = 13
    print("13 doi ra nhi phan la",to_binary(number))