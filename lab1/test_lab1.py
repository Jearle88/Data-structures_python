import lab1
import unittest

class T0_TestingQueue(unittest.TestCase):

    def test_basic_enqueue(self):
        # testing the basic enqueue operation
        print("\n")
        q = lab1.Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        self.assertEqual(q.__str__(), '[1, 2, 3, 4]')
        print("\n")
    def test_space_enqueue(self):
        # testing on a string with a space enqueue operation on string space charcter
        print("\n")
        q = lab1.Queue()
        s="sp ace"
        for char in s:
            q.enqueue(char)
        self.assertEqual('[s, p,  , a, c, e]',q.__str__(), )
        print("\n")

    def test_empty_dequeue(self):
        # testing the basic dequeue operation on empty dequeue
        print("\n")
        q = lab1.Queue()
        with self.assertRaises(AttributeError):
            q.dequeue()
        print("\n")

    def test_enqueue_on_empty(self):
        # testing the basic enqueue operation
        print("\n")
        q = lab1.Queue()
        q.enqueue(1)
        self.assertEqual(q.__str__(), '[1]')
        print("\n")

    def test_dequeue_on_1(self):
        # testing the basic enqueue operation
        print("\n")
        q = lab1.Queue()
        q.enqueue(1)
        self.assertEqual(q.dequeue(), 1)
        print("\n")

class T1_TestingStack(unittest.TestCase):


    def test_is_empty_false(self):
        "return false if the stack is not empty"
        print("\n")
        s = lab1.Stack()
        s.push("4")
        print("return false if the stack is not empty")
        self.assertEqual(s.isEmpty(), False)
        print("\n")

    def test_is_empty_True(self):
        ''' returns True testing if stack is empty'''
        print("\n")
        s = lab1.Stack()

        print("return True if the stack is  empty")
        self.assertTrue(s.isEmpty())
        print("\n")

    def test_pop_on_empty_stack(self):
        '''testing pop on empty stack '''
        print("\n")
        s = lab1.Stack()
        with self.assertRaises(AttributeError):
            s.pop()
        print("\n")

    def test_push_on_empty(self):
        ''' testing if push works on empty stack'''
        print("\n")
        s = lab1.Stack()
        s.push('3')
        self.assertEqual( '[3]',s.__str__())
        print("\n")

    def test_basic_pop(self):
        ''' testing pop  on stack with elments in it'''
        print("\n")
        s = lab1.Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        self.assertEqual(s.pop(), 4)
        print("\n")

    def test_pop_on_1(self):
        ''' testing pop works on  stack 1 elments '''
        print("\n")
        s = lab1.Stack()
        s.push(1)
        self.assertEqual(s.pop(), 1)
        print("\n")

    def test_basic_push(self):
        ''' testing ifpop works on  stackwith elments in it'''
        print("\n")
        s = lab1.Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        self.assertEqual('[4,3,2,1]',s.__str__(), )
        print("\n")
class T2_TestingPalindrome(unittest.TestCase):

    def test_basic_string(self):
        # testing with basic string
        print("\n")
        string = "hello"
        p = lab1.isPalindrome(string)
        print("The string being tested is -> ", string)
        self.assertFalse(p )
        print("\n")

    def test_taco_cat(self):
        '''Test string "Taco Cat" in is_palindrome function
        Return True'''
        print("\n")
        string = "Taco Cat"
        p = lab1.isPalindrome(string)
        self.assertTrue(p)  # Use self.assertTrue to check for True value
        print("\n")
    def test_race_car(self):
        '''test string "Taco Cat" in is_palindrome fucniton
         return True'''
        print("\n")
        string ="raCe car"
        p= lab1.isPalindrome(string)
        self.assertEqual(True,p)
        print("\n")

    def test_taco_cat(self):
        '''Test string "Taco Cat" in is_palindrome function
        Return True'''
        print("\n")
        string = "Taco Cat"
        p = lab1.isPalindromeEC(string)
        self.assertTrue(p)  # Use self.assertTrue to check for True value
        print("\n")

if __name__ == '__main__':
    unittest.main()
