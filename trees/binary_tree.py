
class BinaryTree:
    def __init__(self, max_depth=5):
        self.root_node = None
        self.depth = 0
        self.max_depth = max_depth

    def get_root(self):
        return self.root_node

    def insert(self, node):
        if self.root_node is None:
            self.root_node = node
        else:
            node_depth = self._find_insert_node(self.root_node, node)

            if node_depth > self.depth:
                self.depth = node_depth
            elif node_depth > self.max_depth:
                raise Exception('Max depth exceeded.')

    def _find_insert_node(self, par_node, node, recursion_depth=0):
        recursion_depth = recursion_depth + 1
        if recursion_depth > self.max_depth:
            raise Exception('Max depth exceeded.')

        if par_node.value > node.value and par_node.left is not None:
            return self._find_insert_node(par_node.left, node, recursion_depth=recursion_depth)
        elif par_node.value > node.value and par_node.left is None:
            par_node.left = node
            return recursion_depth
        elif par_node.value < node.value and par_node.right is not None:
            return self._find_insert_node(par_node.right, node, recursion_depth=recursion_depth)
        elif par_node.value < node.value and par_node.right is None:
            par_node.right = node
            return recursion_depth
        else:
            raise Exception("BinaryTree: Duplicated value")

# https://stackoverflow.com/questions/1894846/printing-bfs-binary-tree-in-level-order-with-specific-formatting
    def print_tree(self):
        this_level = [self.root_node]

        level = 0
        while this_level:
            print('Tree level', level)
            next_level = list()
            for nodes in this_level:
                print(nodes)
                if nodes.left is not None:
                    next_level.append(nodes.left)
                if nodes.right is not None:
                    next_level.append(nodes.right)
            level = level + 1
            this_level = next_level

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def is_leaf(self):
            return self.left is None and self.right is None
