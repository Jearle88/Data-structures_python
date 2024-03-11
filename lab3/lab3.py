class Node(object):
    """
     Node object for accessing data in a tree.

    Attributes:
        parent: Parent node in the tree.
        left: Left child node.
        right: Right child node.
        data: Data stored in the node.

    Methods:
        __init__(self, data)
            Initializes a new Node with the specified data.e
    """
    def __init__(self, data):
        """
        Initializes a new Node with the specified data.

        parameters:
             data: The data to be stored in the node.

     """
        self.parent = None
        self.left = None
        self.right = None
        self.data = data


class Tree(object):
    """
      Binary Search Tree class.

      Class Constants:
          PREORDER: Constant representing pre-order traversal.
          INORDER: Constant representing in-order traversal.
          POSTORDER: Constant representing post-order traversal.

      Attributes:
          root: The root node of the binary search tree.

      Methods:
          __init__(self)
              Initializes an empty binary search tree.

          print(self)
              Prints the data of all nodes in in-order traversal.

          __print(self, curr_node)
              Recursively prints a subtree in in-order traversal, rooted at curr_node.

          insert(self, data)
              Inserts a new node with the given data into the binary search tree.

          min(self)
              Returns the minimum value held in the tree.

          sub_tree_min(self, x)
              Helper method to find the minimum value in the subtree rooted at node x.

          max(self)
              Returns the maximum value held in the tree.

          __find_node(self, data)
              Returns the node with the specified data value or None if not found.

          contains(self, data)
              Returns True if a node containing the given data is present in the tree, otherwise returns False.

          __iter__(self)
              Initiates an in-order traversal iterator.

          inorder(self)
              Returns an in-order traversal of the tree.

          preorder(self)
              Returns a pre-order traversal of the tree.

          postorder(self)
              Returns a post-order traversal of the tree.

          __traverse(self, curr_node, traversal_type)
              Helper method implemented using generators for traversing the tree.

          find_successor(self, data)
              Finds the successor node of the node with the specified data.

          transplant(self, u, v)
              Replaces subtree rooted at node u with subtree rooted at node v.

          delete(self, data)
              Deletes the node with the specified data from the tree.

      """

    # Binary Search Tree
    # class constants
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

    def __init__(self):
        """
             Initializes an empty binary search tree.
        """

        # Do not create any other private variables.
        # You may create more helper methods as needed.
        self.root = None

    def print(self):
        """
        Prints the data of all nodes in in-order traversal.
            """
        # Print the data of all nodes in order
        self.__print(self.root)


    def __print(self, curr_node):
        """
        Recursively prints a subtree in in-order traversal, rooted at curr_node.

        Parameters:
            curr_node: The current node in the traversal.
        """
        # Recursively print a subtree (in order), rooted at curr_node
        if curr_node is not None:
            self.__print(curr_node.left)
            print(str(curr_node.data), end=' ')  # save space
            self.__print(curr_node.right)
            

    def insert(self, data):
        """
        inserts a new node with the given data into the binary search tree.

            Parameters:
                data: The data to be inserted into the tree.
        """
        # Find the right spot in the tree for the new node
        # Make sure to check if anything is in the tree
        # Hint: if a node n is None, calling n.data will cause an error
        new_node=Node(data)
        if self.root == None:
            self.root = new_node
            return
        root=self.root
        y= None
        if self.contains(data):
            return
        while root is not None:
            y = root
            if new_node.data < y.data:
                root = root.left
            else:
                root = root.right

        new_node.parent = y

        if new_node.data < y.data:
            y.left = new_node
        else:
            y.right = new_node



    def min(self):
        """
        Returns the minimum value held in the tree.

        Returns:
        The minimum value in the tree, or None if the tree is empty.
        """
        # Returns the minimum value held in the tree
        # Returns None if the tree is empty
        if self.root== None:  # If the tree is empty, raise exception
            return None
        node = self.root  # Start at root
        while node.left:  # While node has a left child,
            node = node.left # follow left child reference
        return (node.data)

    def sub_tree_min(self, x):
        '''
        min helper to find minium value of subtress
        within the tree starting at node x

         Parameters:
            x: The root node of the subtree.

        Returns:
            The minimum value in the subtree.
        '''
        # Returns the minimum value in the subtree rooted at node  x
        while x.left is not None:
            x = x.left
        return x

    def max(self):
        """
        Returns the maximum value held in the tree.

        Returns:
            The maximum value in the tree, or None if the tree is empty.
        """
        # Returns the maximum value held in the tree
        # Returns None if the tree is empty
        if self.root == None:  # If the tree is empty, raise exception
            return None
        node = self.root  # Start at root
        while node.right:  # While node has a righ child,
            node = node.right  # follow right child reference
        return (node.data)  # return final node key and data


    def __find_node(self, data):
        """
        Returns the node with the specified data value or None if not found.

        Parameters:
            data: The data value to search for.

        Returns:
            The node with the specified data value, or None if not found.
        """

        # returns the node with that particular data value else returns None
        if self.root == None:
            raise KeyError(" empty tree")
        node =self.root
        if node.data== data:
            return node
        while node is not None and node.data != data:
            if data < node.data:
                node = node.left
            else:
                node = node.right

        return node


    def contains(self, data):
        # return True of node containing data is present in the tree.
        # otherwise, return False.
        # you may use a helper method __find_node() to find a particular node with the data value and return that node

        if self.__find_node(data) is not None:
            return True
        return False

    def __iter__(self):
        """
         # iterate over the nodes with inorder traversal
          using a for loop
        """

        return self.inorder()

    def inorder(self):
        """
        in order traversal of tree
        """
        # inorder traversal : (LEFT, ROOT, RIGHT)
        return self.__traverse(self.root, Tree.INORDER)

    def preorder(self):
        """
        preorder traversal of tree
        """
        # preorder traversal : (ROOT, LEFT, RIGHT)
        return self.__traverse(self.root, Tree.PREORDER)

    def postorder(self):
        """
        postorder traversal of tree
        """
        # postorder traversal : (LEFT, RIGHT, ROOT)
        return self.__traverse(self.root, Tree.POSTORDER)

    def __traverse(self, curr_node, traversal_type):
        """
         Helper method implemented using generators for traversing the tree.

         Parameters:
             curr_node: The current node in the traversal.
             traversal_type: The type of traversal to perform.

         Yields:
             The data of the correct node in the specified traversal order.
         """
        # helper method implemented using generators
        # all the traversals can be implemented using a single method

        #Yield data of the correct node/s
        stack = []
        node = curr_node
        last_visited = None

        while node or stack:
            if node:
                if traversal_type == Tree.INORDER:
                    stack.append(node)
                    node = node.left
                elif traversal_type == Tree.PREORDER:
                    yield node.data
                    stack.append(node)
                    node = node.left
                elif traversal_type == Tree.POSTORDER:
                    stack.append(node)
                    if node.left:
                        node=node.left
                    else:
                        node=node.right

            else:
                node = stack.pop()
                if traversal_type == Tree.INORDER:
                    yield node.data
                    node = node.right
                elif traversal_type == Tree.PREORDER:
                    node = node.right
                elif traversal_type == Tree.POSTORDER:
                    if last_visited == node.right or node.right is None:
                        yield node.data
                        last_visited = node
                        node = None
                    else:
                        stack.append(node)
                        node = node.right

    def find_successor(self, data):
        """
            Finds the successor node of the node with the specified data.

            Parameters:
                data: The data value of the node to find the successor for.

            Returns:
                The successor node of the specified node.

            Raises:
                KeyError: If the node with the specified data is not found in the tree.
            """

        # Find the successor node
        # If the value specified by find_successor does NOT exist in the tree, then raise a KeyError
        # helper method to implement the delete method but may be called on its own
        # If the right subtree of the node is nonempty,then the successor is just 
        # the leftmost node in the right subtree.
        # If the right subtree of the node is empty, then go up the tree until a node that is
        # the left child of its parent is encountered. The parent of the found node will be the
        # successor to the initial node.
        # Note: Make sure to handle the case where the parent is None
    
    	# Return object of successor if found else return None
        if self.root== None:
            raise KeyError( "empty tree")
        data_node = self.__find_node(data)

        if data_node is None:
            raise KeyError(f"Node with data {data} not found in the tree")

        if data_node.right is not None:
            return self.sub_tree_min(data_node.right)

        successor = data_node.parent
        while successor is not None and data_node == successor.right:
            data_node = successor
            successor = successor.parent

        return successor


    def transplant(self, u, v):
        """
         Replaces the subtree rooted at node u with the subtree rooted at node v.

        Parameters:
            u: The node to be replaced.
            v: The node to replace u with.
              """
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent
    def delete(self, data):
            """
        Deletes the node with the specified data from the tree.

            Parameters:
                 data: The data value of the node to be deleted.

            Raises:
                 KeyError: If the node with the specified data is not found in the tree.
        """
        # Find the node to delete.
        # If the value specified by delete does NOT exist in the tree, then don't change the tree and raise a KeyError
        # If you find the node and ...
        #  a) The node has no children, just set its parent's pointer to None.
        #  b) The node has one child, make the node's parent point to its child.
        #  c) The node has two children, replace it with its successor, and remove
        #       successor from its previous location.
        # Recall: The successor of a node is the left-most node in the node's right subtree.
        # Note: Make sure to handle the case where the parent is None
            node = self.__find_node(data)
            if node is None:
                raise KeyError(f"Node with data {data} not found in the tree.")

            if node.left is None:
                self.transplant(node, node.right)
            elif node.right is None:
                self.transplant(node, node.left)
            else:
                y = self.sub_tree_min(node.right)
                if y.parent != node:
                    self.transplant(y, y.right)
                    y.right = node.right
                    y.right.parent = y
                self.transplant(node, y)
                y.left = node.left
                y.left.parent = y

