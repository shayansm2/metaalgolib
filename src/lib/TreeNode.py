from src.lib.DataStructure import DataStructure


class TreeNode(DataStructure):
    def __init__(self, key):
        self.key = key
        self.skew = 0
        self.height = 0
        self.left = self.right = self.parent = None

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def set_skew(self, skew):
        self.skew = skew

    def get_skew(self):
        return self.skew

    def get_key(self):
        return self.key

    def set_key(self, key):
        self.key = key

    def set_left(self, left):
        self.left = left

    def get_left(self):
        return self.left

    def set_right(self, right):
        self.right = right

    def get_right(self):
        return self.right
