from src.lib.FunctionObject import FunctionObject
from src.lib.TreeNode import TreeNode


class BinarySearchTree(FunctionObject):
    def __init__(self):
        self.root = None

    def insert(self, key):
        node = TreeNode(key)
        if self.root is None:
            self.root = node
            return
        # if self.__findNode(self.root, key) is not None:
        #    return

        self.__insert_recursive(self.root, node)

    def __insert_recursive(self, curr, node):
        if node.get_key() < curr.get_key():
            if curr.get_left() is None:
                node.set_parent(curr)
                curr.set_left(node)
                self.__fix(curr)
                return
            self.__insert_recursive(curr.get_left(), node)
        else:
            if curr.getRight() is None:
                node.setParent(curr)
                curr.setRight(node)
                self.__fix(curr)
                return
            self.__insert_recursive(curr.getRight(), node)

    def delete(self, key):
        if self.root is None:
            return
        if self.root.get_left() is None and self.root.getRight() is None and self.root.getKey() == key:
            self.root = None
            return
        node = self.__find_node(self.root, key)
        if node is None:
            return

        self.__delete_recursive(node)

    def __delete_recursive(self, node):
        if node.get_left() is None:
            right = node.getRight()
            self.__mix_with_parent(node, right)
        elif node.getRight() is None:
            left = node.get_left()
            self.__mix_with_parent(node, left)
        else:
            successor = self.__get_min(node.getRight())
            node.setKey(successor.getKey())
            self.__delete_recursive(successor)

    def get_minimum(self):
        if self.root is None:
            return None
        return self.__get_min(self.root).getKey()

    def get_maximum(self):
        if self.root is None:
            return None
        return self.__get_max(self.root).getKey()

    def __get_min(self, curr):
        if curr.get_left() is None:
            return curr
        return self.__get_min(curr.get_left())

    def __get_max(self, curr):
        if curr.getRight() is None:
            return curr
        return self.__get_max(curr.getRight())

    def __mix_with_parent(self, node, child):
        if node == self.root:
            self.root = child
            self.root.setParent(None)
            return
        parent = node.getParent()
        if parent.get_left() == node:
            parent.set_left(child)
        else:
            parent.setRight(child)
        if child is not None:
            child.setParent(parent)
        self.__fix(parent)

    def __find_node(self, curr, key):
        if curr is None:
            return None
        if curr.getKey() == key:
            return curr
        if curr.getKey() > key:
            return self.__find_node(curr.get_left(), key)
        else:
            return self.__find_node(curr.getRight(), key)

    def __rotate_left(self, node):
        right = node.getRight()
        a = node.get_left()
        b = right.get_left()
        c = right.getRight()

        x = node.getKey()
        y = right.getKey()

        node.setKey(y)
        right.setKey(x)

        node.set_left(right)
        right.setParent(node)

        node.setRight(c)
        if c is not None:
            c.setParent(node)

        self.__rotate(a, b, node, right)

    def __rotate(self, a, b, node, right):
        right.set_left(a)
        if a is not None:
            a.setParent(right)
        right.setRight(b)
        if b is not None:
            b.setParent(right)
        self.__update(right)
        self.__update(node)

    def __rotate_right(self, node):
        left = node.get_left()
        a = left.get_left()
        b = left.getRight()
        c = node.getRight()

        x = node.getKey()
        y = left.getKey()

        node.setKey(y)
        left.setKey(x)

        node.setRight(left)
        left.setParent(node)

        node.set_left(a)
        if a is not None:
            a.setParent(node)

        self.__rotate(b, c, node, left)

    @staticmethod
    def __get_height(node):
        if node is None:
            return -1
        return node.getHeight()

    def __update(self, node):
        node.setSkew(self.__get_height(node.getRight()) - self.__get_height(node.get_left()))
        node.setHeight(max(self.__get_height(node.getRight()), self.__get_height(node.get_left())) + 1)

    def __fix(self, node):
        if node is None:
            return
        self.__update(node)
        if node.getSkew() == 2:
            if node.getRight().getSkew() == -1:
                self.__rotate_right(node.getRight())
            self.__rotate_left(node)
        elif node.getSkew() == -2:
            if node.get_left().getSkew() == -1:
                self.__rotate_left(node.get_left())
            self.__rotate_right(node)
        self.__fix(node.getParent())

    def minimum_number_greater_than(self, key):
        return self.__mng(self.root, key)

    def __mng(self, node, key):
        if node is None:
            return None
        if node.getKey() <= key:
            return self.__mng(node.getRight(), key)
        else:
            result = self.__mng(node.get_left(), key)
            if result is not None:
                return result
            return node.getKey()

    def maximum_number_less_than(self, key):
        return self.__mnl(self.root, key)

    def has(self, key):
        if self.__find_node(self.root, key) is not None:
            return True
        else:
            return False

    def __mnl(self, node, key):
        if node is None:
            return None
        if node.getKey() >= key:
            return self.__mnl(node.get_left(), key)
        else:
            result = self.__mnl(node.getRight(), key)
            if result is not None:
                return result
            return node.getKey()

    def print_tree(self):
        self.__print(self.root)
        print()

    def sorted_order(self):
        if self.root is None:
            return []
        result = []
        self.__in_order(self.root, result)
        return result

    def __in_order(self, node, result):
        if node is None:
            return
        self.__in_order(node.get_left(), result)
        result.append(node.getKey())
        self.__in_order(node.getRight(), result)

    def __print(self, node):
        if node is None:
            return
        self.__print(node.get_left())
        print(node.getKey(), end=" ")
        self.__print(node.getRight())
