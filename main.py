from trees import binary_tree as bt
from trees import regression_tree as rt


def main():
    #  Example usage:
    tree = bt.BinaryTree(max_depth=2)
    tree.insert(bt.BinaryTree.Node(5))

    reg_tree = rt.RegressionTree(max_depth=3)
    inserted_node = reg_tree.insert(rt.RegressionTree.Node(rss=12, argmin=2))


if __name__ == '__main__':
    main()



