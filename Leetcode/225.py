class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue_A = []
        self.queue_B = []
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue_A.append(x)
        #self.queue_A.push(x) # your only error
      
    def move(self):
        while len(self.queue_A) > 1:
            self.queue_B.append(self.queue_A.pop(0))
            

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.empty():
            return
        else:
            if not self.queue_A:
                self.queue_A, self.queue_B = self.queue_B, self.queue_A
            if len(self.queue_A) == 1:
                return self.queue_A.pop(0)
            else:
                self.move()
                return self.queue_A.pop(0)
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.empty():
            return
        else:
            if not self.queue_A:
                self.queue_A, self.queue_B = self.queue_B, self.queue_A
            if len(self.queue_A) == 1:
                return self.queue_A[0]
            else:
                self.move()
                return self.queue_A[0]
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.queue_A and not self.queue_B
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
