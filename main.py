from trees import binary_tree as bt
from trees import regression_tree as rt


def main():
    #  Example usage:
    tree = bt.BinaryTree(max_depth=2)
    tree.insert(bt.BinaryTree.Node(5))

    features = ['wzrost', 'waga']
    reg_tree = rt.RegressionTree(features, max_depth=3)
    split_points = [150, 100]
    split_points_dict = dict(zip(features, split_points))
    node = rt.RegressionTree.Node('wzrost', split_points_dict, 100, 200)
    reg_tree.insert(node)


if __name__ == '__main__':
    main()



