from rb_tree import Node, rb_tree
import unittest


class T0_tree_left_rotation(unittest.TestCase):

    def test_tree_left_rotation_1(self):
        print("\n")
        print("tree_left_rotation")
        tree = rb_tree()
        tree.bst_insert(2)
        tree.bst_insert(1)
        tree.bst_insert(3)
        tree.print_tree()
        print("intial tree", "\n")
        tree.left_rotate(tree.root)
        tree.print_tree()
        print("new tree", "\n")

        tree_preorder = [node.data for node in tree.preorder()]

        self.assertEqual([3, 2, 1], tree_preorder)

        print("tree after left rotation about root  in prorder")
        print("\n")

    def test_tree_left_rotation_2(self):
        print("\n")
        print("tree_left_rotation")
        tree = rb_tree()
        tree.bst_insert(7)
        tree.bst_insert(5)
        tree.bst_insert(9)
        tree.bst_insert(3)
        tree.bst_insert(6)
        tree.bst_insert(8)
        tree.bst_insert(10)
        tree.bst_insert(1)
        tree.bst_insert(2)
        tree.print_tree()
        print("intial prorder tree", "\n")
        tree.left_rotate(tree.root)
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual([9, 7, 5, 3, 1, 2, 6, 8, 10], tree_preorder)
        tree.print_tree()
        print("tree after left rotation about root  in prorder")
        print("\n")


class T1_tree_right_rotation(unittest.TestCase):

    def test_tree_right_rotation_1(self):
        print("\n")
        print("tree_right_rotation")
        tree = rb_tree()
        tree.bst_insert(2)
        tree.bst_insert(1)
        tree.bst_insert(3)

        tree.print_tree()
        print("intial prorder tree", "\n")
        tree.right_rotate(tree.root)
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual(tree_preorder, [1, 2, 3])
        tree.print_tree()
        print("tree after right rotation about root  in prorder")
        print("\n")

    def test_tree_right_rotation_2(self):
        print("\n")
        print("tree_right_rotation")
        tree = rb_tree()
        tree.bst_insert(7)
        tree.bst_insert(5)
        tree.bst_insert(9)
        tree.bst_insert(3)
        tree.bst_insert(6)
        tree.bst_insert(8)
        tree.bst_insert(10)
        tree.bst_insert(1)
        tree.bst_insert(2)
        tree.print_tree()
        print("intial prorder tree", "\n")
        tree.right_rotate(tree.root)
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual([5, 3, 1, 2, 7, 6, 9, 8, 10], tree_preorder)
        tree.print_tree()
        print("tree after right rotation about root  in prorder")
        print("\n")


class T2_tree_insert_color(unittest.TestCase):

    def test_tree_insert_color_0(self):
        print("\n")
        print("tree_color_check")

        tree = rb_tree()

        tree.insert(2)
        tree.insert(1)
        tree.insert(3)
        tree.insert(4)
        tree.print_tree()
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual([2, 1, 3, 4], tree_preorder)
        self.assertEqual(['black', 'black', 'black', 'red'], tree_preorder_color)
        print("\n")

    def test_tree_insert_color_1(self):
        print("\n")
        print("tree_color_check")

        tree = rb_tree()
        tree.insert(1)
        print("check tree1", "\n")
        print(tree.print_tree())

        tree.insert(2)
        print("check tree A", "\n")
        print(tree.print_tree())
        tree.insert(3)
        print("check tree1.5", "\n")
        print(tree.print_tree())
        tree.insert(4)
        print("check tree2", "\n")
        print(tree.print_tree())
        tree.insert(5)
        print("check tree2.5", "\n")
        print(tree.print_tree())
        tree.insert(6)
        print("check tree3", "\n")
        print(tree.print_tree())
        tree.insert(7)
        # i=0
        # while i<8:
        # tree.insert(i)
        # i+=1
        # for i in range(1, 8):
        # tree.insert(i)
        print("check tree4", "\n")

        print(tree.print_tree())
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [2, 1, 4, 3, 6, 5, 7])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'red', 'black', 'black', 'red', 'red'])
        print("\n")


class T3_tree_delete(unittest.TestCase):

    def test_tree_delete_0(self):
        print("\n")
        print("tree_insert")
        # print("checking in order, preorder and post order")
        tree = rb_tree()
        tree.insert(5)
        tree.insert(7)
        tree.insert(9)
        tree.insert(6)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 5, 6, 9])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'red', 'black'])
        tree.delete(9)
        tree.print_tree()
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        print(tree_preorder)
        self.assertEqual([6, 7], tree_preorder)
        self.assertEqual(tree_preorder_color, ['black', 'black', 'black'])
        print("\n")

    def test_tree_delete_1(self):
        print("\n")
        print("tree_insert")
        print("checking in order, preorder and post order")
        tree = rb_tree()

        for i in range(1, 8):
            tree.insert(i)
        tree.delete(5)
        tree.delete(4)
        # tree.print_tree()
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [2, 1, 6, 3, 7])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'red', 'black', 'black'])
        print("\n")

    def test_tree_delete_color_2(self):
        print("\n")
        print("tree_left_rotation")
        tree = rb_tree()
        tree.insert(7)
        tree.insert(5)
        tree.insert(9)
        tree.insert(3)
        tree.insert(6)
        tree.insert(8)
        tree.insert(10)
        tree.insert(1)
        tree.insert(2)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 5, 2, 1, 3, 6, 9, 8, 10])
        self.assertEqual(tree_preorder_color, ['black', 'red', 'black', 'red', 'red', 'black', 'black', 'red', 'red'])
        tree.delete(6)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 2, 1, 5, 3, 9, 8, 10])
        self.assertEqual(tree_preorder_color, ['black', 'red', 'black', 'black', 'red', 'black', 'red', 'red'])
        tree.delete(7)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual([8, 2, 1, 5, 3, 9, 10], tree_preorder)
        self.assertEqual(tree_preorder_color, ['black', 'red', 'black', 'black', 'red', 'black', 'red'])
        print("\n")

    class TestRedBlackTree(unittest.TestCase):
        def test_insertion(self):
            # Test case for basic insertion
            tree = rb_tree()
            tree.insert(10)
            self.assertEqual([10], [node.data for node in tree.inorder()])

            # Test case for insertion with rotation
            tree.insert(5)
            tree.insert(15)
            self.assertEqual([5, 10, 15], [node.data for node in tree.inorder()])

            # Test case for insertion with color change
            tree.insert(20)
            tree.insert(25)
            self.assertEqual([5, 10, 15, 20, 25], [node.data for node in tree.inorder()])
            self.assertEqual(['black', 'red', 'black', 'red', 'black'], [node.color for node in tree.inorder()])

            # Add more insertion test cases as needed

        def test_deletion(self):
            # Test case for deleting a leaf node
            tree = rb_tree()
            tree.insert(10)
            tree.delete(10)
            self.assertEqual([], [node.data for node in tree.inorder()])

            # Test case for deleting a node with one child
            tree.insert(10)
            tree.insert(5)
            tree.delete(10)
            self.assertEqual([5], [node.data for node in tree.inorder()])

            # Test case for deleting a node with two children
            tree.insert(10)
            tree.insert(5)
            tree.insert(15)
            tree.delete(10)
            self.assertEqual([5, 15], [node.data for node in tree.inorder()])

            # Test case for deleting a node with color change
            tree.insert(10)
            tree.insert(5)
            tree.insert(15)
            tree.insert(20)
            tree.delete(15)
            self.assertEqual([5, 10, 20], [node.data for node in tree.inorder()])
            self.assertEqual(['black', 'red', 'black'], [node.color for node in tree.inorder()])

        def test_left_rotate_with_none(self):
            tree = rb_tree()
            tree.left_rotate(None)
            self.assertRaises(KeyError)

        def test_right_rotate_with_none(self):
            tree = rb_tree()

            tree.right_rotate(None)
            self.assertRaises(KeyError)


if __name__ == "__main__":
    unittest.main()
