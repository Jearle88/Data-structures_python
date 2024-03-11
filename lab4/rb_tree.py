class Node(object):
    """
         Node object for accessing data in a tree.

        Attributes:
            parent: Parent node in the tree.
            left: Left child node.
            right: Right child node.
            data: Data stored in the node.
            color: color of the node

        Methods:
            __init__(self, data)
                Initializes a new Node with the specified data.e
        """

    def __init__(self, data, left = None, right = None, parent = None, color = 'red'):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color


class rb_tree(object):
    """
       A Red-Black Tree implementation.

       ...

       Attributes
       ----------
       root : Node
           The root of the Red-Black Tree.
       sentinel : Node
           A sentinel node representing the null leaf in the Red-Black Tree.

       Methods
       -------
       print_tree()
           Prints the data of all nodes in order.
       print_with_colors()
           Prints the data of all nodes with color indicators.
       inorder()
           Returns an iterator for in-order traversal.
       preorder()
           Returns an iterator for pre-order traversal.
       postorder()
           Returns an iterator for post-order traversal.
       find_min()
           Returns the node with the minimum value in the Red-Black Tree.
       find_node(data)
           Returns the Node object for the given data.
       find_successor(data)
           Returns the successor node for the given data.
       insert(data)
           Inserts a new node with the given data into the Red-Black Tree.
       delete(data)
           Deletes the node with the specified data from the Red-Black Tree.
       left_rotate(current_node)
           Performs a left rotation on the Red-Black Tree.
       right_rotate(current_node)
           Performs a right rotation on the Red-Black Tree.
       __rb_insert_fixup(z)
           Maintains balancing and coloring properties after insertion.
       __rb_delete_fixup(x)
           Maintains balancing and coloring properties after deletion.
       """

    PREORDER = 1
    INORDER = 2
    POSTORDER = 3
    # initialize root and size
    def __init__(self):
        """
            Initializes an empty Red-Black Tree.

            Attributes
            ----------
            root : None
                The root of the Red-Black Tree.
            sentinel : Node
                A sentinel node representing the null leaf in the Red-Black Tree.
            """
        self.root = None
        self.sentinel = Node(None, color = 'black')
        self.sentinel.parent = self.sentinel
        self.sentinel.left = self.sentinel
        self.sentinel.right = self.sentinel
    
    def print_tree(self):
        # Print the data of all nodes in order
        self.__print_tree(self.root)
    
    def __print_tree(self, curr_node):
        """
             Prints the data of all nodes in the Red-Black Tree in order.
             """
        # Recursively print a subtree (in order), rooted at curr_node
        # Printed in preorder
        if curr_node is not self.sentinel:
            print(str(curr_node.data), end=' ')  # save space
            self.__print_tree(curr_node.left)
            self.__print_tree(curr_node.right)

    def __print_with_colors(self, curr_node):
        """
          Prints the data of all nodes in the Red-Black Tree with color indicators.
          """
        ...
        # Recursively print a subtree (in order), rooted at curr_node
        # Printed in PREORDER
        # Extracts the color of the node and print it in the format -dataC- where C is B for black and R for red
        if curr_node is not self.sentinel:

            if curr_node.color == "red":
                node_color = "R"
            else:
                node_color = "B"

            print(str(curr_node.data)+node_color, end=' ')  # save space
            self.__print_with_colors(curr_node.left)
            self.__print_with_colors(curr_node.right)

    def print_with_colors(self):
        """
             Returns an iterator for in-order traversal of the Red-Black Tree.
             """
        # Also prints the data of all node but with color indicators
        self.__print_with_colors(self.root)
            
            
    def __iter__(self):
        """ iterates through tree in inorder traversal"""
        return self.inorder()

    def inorder(self):
        """ inorder traversal helper function"""
        return self.__traverse(self.root, rb_tree.INORDER)

    def preorder(self):
        "" "preorder traversal helper function"""
        return self.__traverse(self.root, rb_tree.PREORDER)

    def postorder(self):
        """ postorder traversal helper function"""

        return self.__traverse(self.root, rb_tree.POSTORDER)

    def __traverse(self, curr_node, traversal_type):
        """
                 Helper method implemented using generators for traversing the tree.

                 Parameters:
                     curr_node: The current node in the traversal.
                     traversal_type: The type of traversal to perform.

                 Yields:
                     The data of the correct node in the specified traversal order.
                 """
        if curr_node is not self.sentinel:
            if traversal_type == self.PREORDER:
                yield curr_node
            yield from self.__traverse(curr_node.left, traversal_type)
            if traversal_type == self.INORDER:
                yield curr_node
            yield from self.__traverse(curr_node.right, traversal_type)
            if traversal_type == self.POSTORDER:
                yield curr_node

    # find_min travels across the leftChild of every node, and returns the
    # node who has no leftChild. This is the min value of a subtree
    def find_min(self):
        """ Finds min value of a subtree"""
        current_node = self.root
        while current_node.left.data != None:
            current_node = current_node.left
        return current_node
    
    # find_node expects a data and returns the Node object for the given data
    def find_node(self, data):
        """ Finds a given node of a tree using the data prameter.
        parameter:
        data type int
        The number that nedds to be found in tree
        """
        if self.root:
            res = self.__get(data, self.root)
            if res:
                return res
            else:
                raise KeyError('Error, data not found')
        else:
            raise KeyError('Error, tree has no root')

    # helper function __get receives a data and a node. Returns the node with
    # the given data
    def __get(self, data, current_node):
        """ Helper functino receives a data and node, returns node with given data
        parameters:
        data:
        the data we want to get in tree
        current_node:
        the current Node in the tree
        """
        if current_node is self.sentinel: # if current_node does not exist return None
            print("couldnt find data: {}".format(data))
            return None
        elif current_node.data == data:
            return current_node
        elif data < current_node.data:
            # recursively call __get with data and current_node's left
            return self.__get( data, current_node.left )
        else: # data is greater than current_node.data
            # recursively call __get with data and current_node's right
            return self.__get( data, current_node.right )
    

    def find_successor(self, data):
        """
           Returns the successor node for the given data.

           Parameters
           ----------
           data :
               The data for which to find the successor.

           Raises
           ------
           KeyError
               If the data is not found in the tree.
           """
        # Private Method, can only be used inside of BST.
        current_node = self.find_node(data)

        if current_node.data == self.sentinel.data:
            raise KeyError

        # Travel left down the rightmost subtree
        if current_node.right:
            current_node = current_node.right
            while current_node.left.data is not self.sentinel.data:
                current_node = current_node.left
            successor = current_node

        # Travel up until the node is a left child
        else:
            parent = current_node.parent
            while parent is not self.sentinel and current_node is not parent.left:
                current_node = parent
                parent = parent.parent
            successor = parent

        if successor:
            return successor
        else:
            return None

    # put adds a node to the tree
    def insert(self, data):
        """
                Inserts a new node with the given data into the Red-Black Tree.

                Parameters
                ----------
                data :
                    The data to insert into the Red-Black Tree.
                """
        # if the tree has a root
        if self.root:
            # use helper method __put to add the new node to the tree
            new_node = self.__put(data, self.root)
            #self.bst_insert(data)
            self.__rb_insert_fixup(new_node)
        else: # there is no root
            # make root a Node with values passed to put
            self.root = Node(data, parent = self.sentinel, left = self.sentinel, right = self.sentinel)
            new_node = self.root
            self.__rb_insert_fixup(new_node)

    
    #Insertion for Binary Search Tree
    def bst_insert(self, data):
        """
                      Inserts a new node with the given data into the Red-Black Tree.
                      uses the BST insert algorithm.

                      Parameters
                      ----------
                      data :
                          The data to insert into the Red-Black Tree.
                      """
        # if the tree has a root
        if self.root:
            # use helper method __put to add the new node to the tree
            self.__put(data, self.root)
        else: # there is no root
            # make root a Node with values passed to put
            self.root = Node(data, parent = self.sentinel, left = self.sentinel, right = self.sentinel)
        
    # helper function __put finds the appropriate place to add a node in the tree
    def __put(self, data, current_node):
        """ Helper function that finds teh right place in the tree for a node given its data


        parameters:
        data:
            the data of the Node we want to find
        Current_Node:
            The Node we are currently on
    """
        if data < current_node.data:
            if current_node.left != self.sentinel:
                new_node = self.__put(data, current_node.left)
            else: # current_node has no child
                new_node = Node(data,
                parent = current_node,
                left = self.sentinel,
                right = self.sentinel )
                current_node.left = new_node
        else: # data is greater than or equal to current_node's data
            if current_node.right != self.sentinel:
                new_node = self.__put(data, current_node.right)
            else: # current_node has no right child
                new_node = Node(data,
                parent = current_node,
                left = self.sentinel,
                right = self.sentinel )
                current_node.right = new_node
        return new_node

    def rb_transplant(self, u, v):
        """
                Replaces the subtree rooted at node u with the subtree rooted at node v.

               Parameters:
                   u: The node to be replaced.
                   v: The node to replace u with.
                     """
        if u.parent == self.sentinel:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:

            v.parent = u.parent
        else:
            # If v is None, update the parent pointer of u's parent to None
            if u == u.parent.left:
                u.parent.left = None
            else:
                u.parent.right = None

    def delete(self, data):
        """
           Deletes the node with the specified data from the Red-Black Tree.

           Parameters
           ----------
           data : type
               The data to delete from the Red-Black Tree.
           """
        # Same as binary tree delete, except we call rb_delete fixup at the end.
        z = self.find_node(data)  # Find the node with the specified data
        y = z
        y_original_color = y.color
        print(z.left.data)

        if z.left.data is None:
            x = z.right

            self.rb_transplant(z, z.right)


        elif z.right == self.sentinel:
            x = z.left
            self.rb_transplant(z, z.left)
        else:
            y = self.find_successor(z.data)  # y is z’s successor
            y_original_color = y.color
            x = y.right

            if y != z.right:  # is y farther down the tree?
                self.rb_transplant(y, y.right)  # replace y by its right child
                y.right = z.right  # z’s right child becomes y’s right child
                y.right.parent = y  # y’s right child
                x.parent = y  # Update the parent of x to y
            else:
                x.parent = y  # in case x is self.sentinel

            self.rb_transplant(z, y)  # replace z by its successor y
            y.left = z.left  # and give z’s left child to y
            y.left.parent = y  # which had no left child

            y.color = z.color


        if y_original_color == 'black':
            self.__rb_delete_fixup(x)

    def left_rotate(self, current_node):
        """
            Performs a left rotation on the Red-Black Tree.

            Parameters
            ----------
            current_node : Node
                The node around which the left rotation is performed.

            Raises
            ------
            KeyError
                If the current_node is None.
            """
        # If there is nothing to rotate with, then raise a KeyError
        # if x is the root of the tree to rotate with left child subtree T1 and right child y, 
        # where T2 and T3 are the left and right children of y then:
        # x becomes left child of y and T3 as its right child of y
        # T1 becomes left child of x and T2 becomes right child of x

        # refer page 328 of CLRS book for rotations

        if current_node is None:
            raise KeyError("Cannot perform left rotation on a None node.")
        y = current_node.right
        if y is None:
            return #raise KeyError("Cannot perform left rotation when there is no right child.")
   # Update current_node's right child
        current_node.right = y.left

        if y.left: # is not  self.sentinel:
            y.left.parent = current_node

        # Update y's parent
        if y is not self.sentinel :
            y.parent = current_node.parent

        if current_node.parent.data is None: # check for rooot
            self.root = y

        elif current_node is current_node.parent.left:
                current_node.parent.left = y
        else:
                current_node.parent.right = y
        y.left = current_node
        current_node.parent = y
    def right_rotate(self, current_node):
        """
                    Performs a right rotation on the Red-Black Tree.

                    Parameters
                    ----------
                    current_node : Node
                        The node around which the left rotation is performed.

                    Raises
                    ------
                    KeyError
                        If the current_node is None.
                    """

        # If there is nothing to rotate with, then raise a KeyError
        # If y is the root of the tree to rotate with right child subtree T3 and left child x, 
        # where T1 and T2 are the left and right children of x then:
        # y becomes right child of x and T1 as its left child of x
        # T2 becomes left child of y and T3 becomes right child of y

        # refer page 328 of CLRS book for rotations

        if current_node is None:
            raise KeyError("Cannot perform right rotation on a None node.")
        y = current_node.left  # Change from current_node.right to current_node.left
        # Update current_node's left child  # Change from current_node.right to current_node.left
        current_node.left = y.right  # Change from current_node.right to current_node.left

        if y.right:  # Change from y.left to y.right
            y.right.parent = current_node

        # Update y's parent
        if y is not self.sentinel:
            y.parent = current_node.parent

        if current_node.parent.data is None:  # check for root
            self.root = y

        elif current_node is current_node.parent.right:  # Change from current_node.left to current_node.right
            current_node.parent.right = y

        else:
            current_node.parent.left = y  # Change from current_node.right to current_node.left

        y.right = current_node  # Change from y.left to y.right
        current_node.parent = y

    def __rb_insert_fixup(self, z):
        """
             Maintains balancing and coloring properties after deletion.

             Parameters
             ----------
             z : Node
                 The node around which to fix the Red-Black Tree properties.
             """
        # This function maintains the balancing and coloring property after bst insertion into
        # the tree. Please red the code for insert() method to get a better understanding
        # refer page 330 of CLRS book and lecture slides for rb_insert_fixup
        while z.parent.color == 'red':
            if z.parent == z.parent.parent.left: #orig left
                y = z.parent.parent.right  # y is z’s uncle
                if y.color == 'red':  # are z’s parent and uncle both red?
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:

                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)


                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.right_rotate(z.parent.parent)


            else:  # same as lines 3–15, but with “right” and “left” exchanged

                y = z.parent.parent.left
                if y.color == 'red':  # are z’s parent and uncle both red?
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent

                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)


                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.left_rotate(z.parent.parent)

        self.root.color = 'black'

    def __rb_delete_fixup(self, x):
        """
               Maintains balancing and coloring properties after insertion.

               Parameters
               ----------
               x : Node
                   The node around which to fix the Red-Black Tree properties.
               """
        ...
        # This function maintains the balancing and coloring property after bst deletion 
        # from the tree. Please read the code for delete() method to get a better understanding.
        # refer page 338 of CLRS book and lecture slides for rb_delete_fixup
        while x != self.root and x.color == 'black':
            if x.data == x.parent.left.data:  # is x a left child?
                w = x.parent.right  # w is x’s sibling
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.left_rotate(x.parent)
                    w = x.parent.right

                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'black':
                        w.left.color = 'black'
                        w.color = 'red'
                        self.right_rotate(w)
                        w = x.parent.right

                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self.left_rotate(x.parent)
                    x = self.root
            else:  # same as lines 3–22, but with “right” and “left” exchanged
                w = x.parent.left
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.right_rotate(x.parent)
                    w = x.parent.left

                if w.right.color == 'black' and w.left.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.left.color == 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self.left_rotate(w)
                        w = x.parent.left

                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.left.color = 'black'
                    self.right_rotate(x.parent)
                    x = self.root

        x.color = 'black'
