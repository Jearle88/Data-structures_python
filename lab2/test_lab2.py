import unittest
import pqueue
import mheap


class T0_pqueue_insert(unittest.TestCase):


    def test_1_pq_insert(self):
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        pq.insert(4)
        pq.insert(5)
        pq_list = [element for element in pq]
        self.assertEqual(pq_list, [5,4,2,1,3])
        print("\n")

    def test_2_pq_insert(self):
        print("\n")
        pq = pqueue.pqueue(6)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        pq.insert(4)
        pq.insert(5)
        pq.insert(1)
        pq_list = [element for element in pq]
        self.assertEqual(pq_list, [5,4,2,1,3,1])
        print("\n")

    def test_1_pq_insert(self):
        print("\n")

        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        pq.insert(4)
        pq.insert(5)
        pq_list = [element for element in pq]
        self.assertEqual(pq_list, [5, 4, 2, 1, 3])
        print("\n")

class T1_pqueue_peek(unittest.TestCase):

    def test_1_pq_peek(self):
        print("Just return the fist element of the queue.")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(pq.peek(), 3)
        print("\n")


class T2_pqueue_extract_max(unittest.TestCase):

    def test_1_pq_extract_max(self):
        print("extract and return the maximum element of the queue")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        self.assertEqual(pq.extract_max(), 3)
        print("\n")

    def test_2_pq_extract_max(self):
        print("check if heap is sorted after extract max")
        print("\n")
        pq = pqueue.pqueue(5)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        pq.extract_max()

        self.assertEqual(pq.get_pqueue(),[2,1])
        print("\n")



    def test_insert_extract_max(self):
        '''Check if an object of pqueue is still a valid heap after
        the following series of insert()
        and extract max() calls on the same pqueue object.'''
        pq = pqueue.pqueue(4)
        pq.insert(1)
        pq.insert(2)
        pq.insert(3)
        pq.insert(4)
        pq.extract_max()

        check=pq.get_pqueue()
        self.assertEqual([3,1,2],check)

    def test_insert_extract_max(self):
        'Checking subsequent extract_max() calls and get_pqueue'''
        pq = pqueue.pqueue(10)
        l=[3, 4, 7, 10, 24, 37, 57, 67, 87]
        for i in range(len(l)-1):
            pq.insert(l[i])

        pq.extract_max()
        pq.extract_max()
        pq.extract_max()
        pq.extract_max()
        pq.extract_max()



        check = pq.get_pqueue()
        self.assertEqual([3, 1, 2], check)


class T5_heap_sort(unittest.TestCase):

    def test_heap_sort_1(self):
        print("\n")
        to_sort_list = [10,24,3,57,4,67,37,87,7]
        sorted_list = mheap.heap_sort(to_sort_list)

        self.assertEqual( [3, 4, 7, 10, 24, 37, 57, 67, 87], sorted_list)
        print("\n")

    def test_heap_sort_2(self):
        print("\n")
        to_sort_list = [10, 24, 3, 57, 4, 67, 37, 87, 7,7]
        sorted_list = mheap.heap_sort(to_sort_list)

        self.assertEqual([3, 4, 7, 7,10, 24, 37, 57, 67, 87], sorted_list)
        print("\n")


class test_heap_errors(unittest.TestCase):

    def test_build_heap(self):
        # Test that build_heap properly builds a max heap.
        to_sort_list = [1,3,6,5,4,2,8,9,10]
        max_heap_obj = mheap.max_heap(size=len(to_sort_list), data=to_sort_list)
        max_heap_obj.build_heap()

        # After building the heap, the root should be the maximum element.
        self.assertEqual(max_heap_obj.peek(), 10)

    def test_insert_full_heap(self):
        # Test that an IndexError is raised when inserting to a full heap.
        max_heap_obj = mheap.max_heap(size=5)
        data = [10, 24, 3, 57, 4]

        for item in data:
            max_heap_obj.insert(item)

        # Now, the heap is full. Inserting again should raise an IndexError.
        with self.assertRaises(IndexError):
            max_heap_obj.insert(67)

    def test_extract_max_empty_heap(self):
        # Test that a KeyError is raised when extract_max is called on an empty heap.
        max_heap_obj = mheap.max_heap(size=5)

        # The heap is empty, extracting should raise a KeyError.
        with self.assertRaises(KeyError):
            max_heap_obj.extract_max()




class test_extract_max(unittest.TestCase):
    def test_extract_max_order(self):
        heap = mheap.max_heap(6)
        heap.insert(7)
        heap.insert(3)
        heap.insert(5)
        heap.insert(1)
        heap.insert(9)

        max_val = heap.extract_max()
        self.assertEqual(max_val, 9)
        self.assertEqual([7, 3, 5, 1],heap.get_heap())

    def test_extract_same_val(self):
        heap = mheap.max_heap(6)
        heap.insert(7)
        heap.insert(3)
        heap.insert(5)
        heap.insert(1)
        heap.insert(9)
        heap.insert(9)
        heap.extract_max()

        max_val = heap.extract_max()
        self.assertEqual(max_val, 9)
        self.assertEqual([7, 3, 5, 1], heap.get_heap())

    def test_mix_insertions_and_extractions(self):
        # Create a max heap
        heap = mheap.max_heap(7)

        # Insert values into the heap
        heap.insert(10)
        heap.insert(20)
        heap.insert(30)

        # Extract a value from the heap
        max_val = heap.extract_max()
        self.assertEqual(max_val, 30)

        # Insert more values
        heap.insert(5)
        heap.insert(40)

        # Extract another value
        max_val = heap.extract_max()
        self.assertEqual(max_val, 40)

        # Insert additional values
        heap.insert(15)
        heap.insert(35)

        # Extract the remaining values
        extracted_values = []
        while heap.length > 0:
            extracted_values.append(heap.extract_max())

        # Verify that extracted values are in descending order
        self.assertEqual(extracted_values, [35, 20, 15, 10, 5])
class Test_Single_ElementHeap(unittest.TestCase):

    def test_single_element_heap(self):
        # Create a heap with a single element
        heap = mheap.max_heap(1)
        heap.insert(42)

        # Extract the single element
        max_val = heap.extract_max()

        # Check if the extracted value is correct
        self.assertEqual(max_val, 42)

        # Ensure the heap is empty after extraction
        self.assertEqual(heap.get_heap(), [])

if __name__ == '__main__':
    unittest.main()