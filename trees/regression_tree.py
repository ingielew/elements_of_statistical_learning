from .binary_tree import BinaryTree


class RegressionTree(BinaryTree):
    def __init__(self, max_depth=5):
        super().__init__(max_depth=max_depth)

    def insert(self, node):
        super().insert(node)

    class Node(BinaryTree.Node):
        def __init__(self, sample_index, argmin, result, name=""):
            super(RegressionTree.Node, self).__init__(sample_index)
            self.name = name
            self.argmin = argmin
            self.result = result
            self.label = "{} > {}".format(self.name, self.argmin)
