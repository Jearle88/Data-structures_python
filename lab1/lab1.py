class Node(object):
    """
    A class to represent a node.

    ...

    Attributes
    ----------
    data : int or float
        An individual character or number to be stored in a node
    next_node : object of class Node
        A pointer to the next node in a stack or queue

    Methods
    -------
    setData(data):
        Updates the value of data attribute of Node
    setNext(next_node):
        Updates the value of next_node attribute of Node
    getData():
        Returns the value of data attribute
    getNext():
        Returns the value of next_node attribute
    """
    def __init__(self, data = None, next_node = None):
        """
        Constructs (or initializes) the attributes for an object of the class

        ...

        Parameters
        ----------
        data : int or float
            An individual character or number to be stored in a node
        next_node : object of class Node
            A pointer to the next node in a stack or queue

        """
        self.__data = data
        self.__next_node = next_node

    def setData(self, data):
        '''Set the "data" data field to the corresponding input.'''
        self.__data=data


    def setNext(self, next_node):
        '''Set the "next_node" data field to the corresponding input.'''

        self.__next_node=next_node


    def getData(self):
        '''Return the "data" data field.'''
        return self.__data


    def getNext(self):
        '''Return the "next_node" data field.'''
        return self.__next_node

class Queue(object):
    """ Queue Data structcutre that works on FIFO(First in first out) sorting

    Attraibutes
    --------
    self.__head: Node
    lead node in queue, intally set to none until data gets enqued on it
     self. __tail: Node
        tail node in queue, intally set to none until data gets enqeued on it
      ______
     methods:


     enqueue(newData): Enqueue new data to the queue starting

     Dequeue: dequeue data from Queue, returns removed data
     isEmpty: Returns True If queue is empty and false if it is not empty
     """

    def __init__(self):
        ''' constructs data to be added to queue
        '''

        self.__head = None
        self.__tail = None

    def __str__(self):
        '''Loop through your queue and print each Node's data.
        NOTE: on dierctions it says no lists, however on piaza, Yongseok Paul So said that we can use a
         temporary list and join at end for str only
        '''
        current_node=self.__head
        elements=[]
        while current_node  is not None:
            elements.append((str(current_node.getData())))
            current_node=current_node.getNext()
        print(elements)
        return '[' + ', '.join(elements) + ']'

    def enqueue(self, newData):
        '''Create a new node whose data is newData and whose next node is null
        Update head and tail
        parameters:
        ----
        newData: int or float.
            data node from Node class '''
        # Hint: Think about what's different for the first node added to the Queue
        newNode=Node(newData)
        if self.isEmpty(): # if empty queue
          self.__head=newNode
          self.__tail=newNode
        else:
            self.__tail.setNext(newNode)
            self.__tail=newNode

    def dequeue(self):
        '''Return the head of the Queue
        Update head.
        raises
        -----
        Raises attribute error when queue is empty'''
        #  Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #          to hold important information
        #  Hint: Return null on a empty Queue
        # Hint: Return the element(data) that is dequeued.
        if self.isEmpty():
            raise AttributeError

        data= self.__head.getData()
        next_node=self.__head.getNext()
        self.__head= next_node
        return data

    def isEmpty(self):
        '''Check if the Queue is empty. returns true if empty, otherwise false'''
        if not self.__head:
            return True
        return False



class Stack(object):
    """Stack Data structures that operates on LIFO(last in First out)

    Attributes
    --------
    self.top: Node
    lead node in stack, intally set to none until data gets pushed on it
     self.bottom: Node
        bottom node in stack, intally set to none until data gets pushed on it

     methods:
     ______

     push(newData): push new data onto the stack

     pop: removes data from stack, returns removed data
     isEmpty: Returns True If queue is empty and false if it is not empty"""


    def __init__(self):
        ''' We want to initialize our Stack to be empty.
        (ie) Set top as null'''
        self.top= None
        self.bottom=None

    def __str__(self):
        '''Loop through your stack and print each Node's data.'''
        current_node = self.top
        elements = []
        while current_node is not None:
            elements.append((str(current_node.getData())))
            current_node = current_node.getNext()
        print(elements)
        return '[' + ', '.join(elements) + ']'

    def push(self, newData):
        '''We want to create a node whose data is newData and next node is top.
        Push this new node onto the stack
        Update top

        Parameter
        -----
        newData: type Node()
        data that will be pushed into stack'''
        newNode=Node(newData)
        if self.isEmpty():
            self.top=newNode
            self.bottom=newNode
        else:
            newNode.setNext(self.top)
            self.top=newNode


    def pop(self):
        ''' Return the Node that currently represents the top of the stack.
        Update top
        Raises
        ----
        AttributeError
         returns Attribute error on empty stack bc there is nothing to Pop'''
        # Hint: The order you implement the above 2 tasks matters, so use a temporary node
        #         to hold important information
        # Hint: Return null on a empty stack
        # Hint: Return the element(data) that is popped
        if self.isEmpty():
            raise AttributeError
            return None
        data = self.top.getData()
        next_node = self.top.getNext()
        self.top = next_node
        return data       

    def isEmpty(self):
        '''Check if the Stack is empty.
        Returns True if empty, false if not empty'''
        if self.bottom== None:
            return True
        else:
            return False


class TwoStackQueue(object):
    """A queue implemented using two stacks.
    Attributes:
        stack1: stack
        1 of 2 stacks in class
        stack 2: stack
        2nd stack
    methods:
       enqueue(newData): Enqueue new data to the queue of 2 stacks
        Dequeue: dequeue data from Queue, returns removed data
     isEmpty: Returns True If queue is empty and false if it is not empty
       """

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, newData):
        """Enqueue an element by pushing it onto stack1."""
        self.stack1.push(newData)

    def dequeue(self):
        """Dequeue an element by popping from stack2 if it's not empty.
        If stack2 is empty, transfer elements from stack1 to stack2 and then pop from stack2."""
        if self.stack2.isEmpty():
            if self.stack1.isEmpty():
                raise AttributeError("Queue is empty")
            else:
                while not self.stack1.isEmpty():
                    self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def isEmpty(self):
        """Check if the queue is empty by checking both stacks."""
        return self.stack1.isEmpty() and self.stack2.isEmpty()

    def __str__(self):
        """Return a string representation of the queue."""
        elements = []

        # Count the elements in stack2
        count_stack2 = 0
        while not self.stack2.isEmpty():
            count_stack2 += 1
            elements.append(str(self.stack2.pop()))

        # Restore stack2
        while count_stack2 > 0:
            self.stack2.push(elements.pop())
            count_stack2 -= 1

        # Count the elements in stack1
        count_stack1 = 0
        while not self.stack1.isEmpty():
            count_stack1 += 1
            elements.append(str(self.stack1.pop()))

        # Restore stack1
        while count_stack1 > 0:
            self.stack1.push(elements.pop())
            count_stack1 -= 1

        return '[' + ', '.join(elements) + ']'


def isPalindrome(s):
    '''Use your Queue and Stack class to test wheather an input is a palindrome.
    parameter:
    s: string
    string we are testing to see if it is a palindrome or not'''
    myStack = Stack()
    myQueue = Queue()
    s = s.replace(" ", "").lower()
    # Push characters onto the stack and enqueue them in the queue
    for char in s:
        myStack.push(char)
        myQueue.enqueue(char)

        # Compare characters from the stack and queue
        ## Helper function ##
    print("stack data")
    myStack.__str__()
    print("queue data")
    myQueue.__str__()
    # Return appropriate value
    while not myStack.isEmpty() and not myQueue.isEmpty():
        if myStack.pop() != myQueue.dequeue():
            return False

    myQueue.__str__()
    # Return appropriate value
    return True

def isPalindromeEC(s):
    '''Check if a string is a palindrome using TwoStackQueue.'''
    # Create an instance of TwoStackQueue
    tsq = TwoStackQueue()

    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()

    # Enqueue characters into the TwoStackQueue
    for char in s:
        tsq.enqueue(char)
    print(tsq)
    # Dequeue and compare characters from the TwoStackQueue
    while not tsq.isEmpty():
        if tsq.dequeue() != tsq.dequeueFromStack2():
            return False

    # If all characters match, it's a palindrome
    return True
def q():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.pop()
    s.push(4)
    s.push(5)
    s.pop()
    s.pop()
    return s.pop()

print(q())