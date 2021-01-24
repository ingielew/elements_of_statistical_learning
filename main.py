from trees import binary_tree as bt
from trees import regression_tree as rt


def main():
    #  Example usage:
    tree = bt.BinaryTree(max_depth=4)
    tree.insert(bt.BinaryTree.Node(5))

    features = ['wzrost', 'waga']
    reg_tree = rt.RegressionTree(features, max_depth=4)

    split_points = [150, 100]
    split_points_dict = dict(zip(features, split_points))
    node = rt.RegressionTree.Node('wzrost', split_points_dict, 100, 200)
    reg_tree.insert(node)

    split_points = [160, 100]
    split_points_dict = dict(zip(features, split_points))
    node = rt.RegressionTree.Node('waga', split_points_dict, 100, 200)
    reg_tree.insert(node)

    split_points = [120, 100]
    split_points_dict = dict(zip(features, split_points))
    node = rt.RegressionTree.Node('wzrost', split_points_dict, 100, 200)
    reg_tree.insert(node)
    reg_tree.print_tree()


if __name__ == '__main__':
    main()
