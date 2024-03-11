import lab3
import unittest



class T0_tree__insert(unittest.TestCase):

    def test_balanced_binary_search_tree(self):
        print("\n")
        print("tree_insert_with_individual_check")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)

        #The following check is without using tree as an iterator (which uses inorder traversal)
        #So this function also does not check the implementation of the traversal function

        self.assertEqual(t.root.data, 4)
        self.assertEqual(t.root.left.data, 2)
        self.assertEqual(t.root.left.left.data, 1)
        self.assertEqual(t.root.left.right.data, 3)
        self.assertEqual(t.root.right.data, 6)
        self.assertEqual(t.root.right.left.data, 5)
        self.assertEqual(t.root.right.right.data, 7)

        print("\n")


class T1_min_and_max(unittest.TestCase):

    def test_min_and_max(self):
        print("\n")
        print("Checkin the min and the max functions")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)

        minimum = t.min()
        self.assertEqual(minimum, 1)
        maximum = t.max()
        self.assertEqual(maximum, 7)

        print("\n")

class T2_Traversal(unittest.TestCase):

    def test_traversal(self):
        print("\n")
        print("Checking all the three traversals")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)
        tree_iterator = [node for node in t]
        inorder = [node for node in t.inorder()]
        preorder = [node for node in t.preorder()]


        print("__iter__(): inorder traversal")
        self.assertEqual(tree_iterator, [1, 2, 3, 4, 5, 6, 7])
        print("inorder traversal")
        self.assertEqual(inorder, [1, 2, 3, 4, 5, 6, 7])
        print("preorder traversal")
        self.assertEqual(preorder, [4, 2, 1, 3, 6, 5, 7])
        print("\n")




class T3_successor(unittest.TestCase):

    def test_successor(self):
        print("\n")
        print("successor function")
        tree_success = lab3.Tree()
        tree_success.insert(8)
        tree_success.insert(3)
        tree_success.insert(10)
        tree_success.insert(1)
        tree_success.insert(6)
        tree_success.insert(4)
        tree_success.insert(7)
        tree_success.insert(14)
        tree_success.insert(13)

        easy_success = tree_success.find_successor(8)
        medium_success = tree_success.find_successor(10)
        tough_success = tree_success.find_successor(7)


        self.assertEqual(10,easy_success.data)
        self.assertEqual(13,medium_success.data)
        self.assertEqual(8,tough_success.data)

        print("\n")


class T4_delete(unittest.TestCase):

    def test_delete(self):
        print("\n")
        print("delete function")
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.insert(13)

        l1 = [node for node in t]
        t.delete(7)
        l2 = [node for node in t]
        t.delete(6)
        l3 = [node for node in t]
        t.delete(8)
        l4 = [node for node in t]
        t.delete(10)
        l5 = [node for node in t]



        self.assertEqual([1, 3, 4, 6, 7, 8, 10, 13, 14],l1)
        self.assertEqual([1, 3, 4, 6, 8, 10, 13, 14],l2)
        self.assertEqual([1, 3, 4, 8, 10, 13, 14],l3)
        self.assertEqual(l4, [1, 3, 4, 10, 13, 14])
        self.assertEqual(l5, [1, 3, 4, 13, 14])

        print("\n")

    def test_delete_empty_tree(self):
        # Test delete on an empty tree
        t = lab3.Tree()
        with self.assertRaises(KeyError):
            t.delete(8)

    def test_find_successor_empty_tree(self):
        # Test find_successor on an empty tree
        t = lab3.Tree()
        with self.assertRaises(KeyError):
            t.find_successor(8)

class T5_contains(unittest.TestCase):

    def test_contains(self):
        print("\n")
        print("contains function")
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.insert(13)
        self.assertEqual(t.contains(13), True)
        self.assertEqual(t.contains(15), False)
        print("\n")


class T6_orig_test_cases(unittest.TestCase):


    def test_insert(self):
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)

        self.assertEqual(list(t), [1, 3, 6, 8, 10])

    def test_delete(self):
        tree_delete = lab3.Tree()
        tree_delete.insert(15)
        tree_delete.insert(7)
        tree_delete.insert(22)
        tree_delete.insert(3)
        tree_delete.insert(10)
        tree_delete.insert(18)
        tree_delete.insert(25)
        tree_delete.insert(1)
        tree_delete.insert(5)
        tree_delete.insert(12)

        # Initial tree
        initial_state = [node for node in tree_delete]

        # Delete nodes and check tree after each deletion
        tree_delete.delete(7)
        after_delete_7 = [node for node in tree_delete]

        tree_delete.delete(10)
        after_delete_10 = [node for node in tree_delete]

        tree_delete.delete(22)
        after_delete_22 = [node for node in tree_delete]

        # Assertions
        self.assertEqual([1, 3, 5, 7, 10, 12, 15, 18, 22, 25], initial_state)
        self.assertEqual([1, 3, 5, 10, 12, 15, 18, 22, 25], after_delete_7)
        self.assertEqual([1, 3, 5, 12, 15, 18, 22,25], after_delete_10)
        self.assertEqual([1, 3, 5, 12, 15, 18, 25], after_delete_22)

    def test_successor(self):
        tree_success = lab3.Tree()
        tree_success.insert(15)
        tree_success.insert(7)
        tree_success.insert(22)
        tree_success.insert(3)
        tree_success.insert(10)
        tree_success.insert(18)
        tree_success.insert(25)
        tree_success.insert(1)
        tree_success.insert(5)
        tree_success.insert(12)

        # Successor for the root node (easy case)
        easy_success = tree_success.find_successor(15)
        self.assertEqual(18, easy_success.data)

        # Successor for a node with a right child (medium case)
        medium_success = tree_success.find_successor(22)
        self.assertEqual(25, medium_success.data)

        # Successor for a node without a right child (tough case)
        tough_success = tree_success.find_successor(7)
        self.assertEqual(10, tough_success.data)

    def test_contains(self):

            t = lab3.Tree()
            t.insert(8)
            t.insert(3)
            t.insert(10)
            t.insert(1)
            t.insert(6)

            self.assertTrue(t.contains(6))
            self.assertTrue(t.contains(8))
            self.assertTrue(t.contains(1))

            self.assertFalse(t.contains(5))
            self.assertFalse(t.contains(11))
            self.assertFalse(t.contains(2))

    def test_insert_duplicate(self):
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(3)  # Inserting the same value again

        self.assertEqual(list(t), [1, 3, 6, 8, 10])

    def test_find_node(self):
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)

        node_3 = t._Tree__find_node(3)
        self.assertEqual(node_3.data, 3)
        self.assertEqual(t._Tree__find_node(22), None)

    def test_traversal(self):
            print("\n")
            print("Checking all the three traversals")
            t = lab3.Tree()

            t.insert(8)
            t.insert(4)
            t.insert(12)
            t.insert(2)
            t.insert(6)
            t.insert(10)
            t.insert(14)

            tree_iterator = [node for node in t]
            inorder = [node for node in t.inorder()]
            preorder = [node for node in t.preorder()]
            postorder = [node for node in t.postorder()]

            print("__iter__(): inorder traversal")
            self.assertEqual(tree_iterator, [2, 4, 6, 8, 10, 12, 14])
            print("inorder traversal")
            self.assertEqual(inorder, [2, 4, 6, 8, 10, 12, 14])
            print("preorder traversal")
            self.assertEqual(preorder, [8, 4, 2, 6, 12, 10, 14])
            print("postorder traversal")
            self.assertEqual([2, 6, 4, 10, 14, 12, 8],postorder)
            print("\n")


if __name__ == '__main__' :
    unittest.main()