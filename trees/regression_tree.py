from .binary_tree import BinaryTree


class RegressionTree(BinaryTree):
    def __init__(self, feature_key_list, max_depth=5):
        super().__init__(max_depth=max_depth)
        self.features = dict.fromkeys(feature_key_list)

    class Node(BinaryTree.Node):
        def __init__(self, feature_key, features_split_points_dict, c_left, c_right):
            self.feature_key = feature_key
            self.feature_split_points_dict = features_split_points_dict
            self.label = "{} > {}".format(self.feature_key, self.feature_split_points_dict[feature_key])

            self.c_left = c_left
            self.c_right = c_right

            super(RegressionTree.Node, self).__init__(self.NodeValue(features_split_points_dict, feature_key))

        def __repr__(self):
            return '- - - - - - -\n{}\n{}\nc_l: {},c_r: {},\nleaf: {}'.format(
                self.label, self.feature_split_points_dict, self.c_left, self.c_right, self.is_leaf())

        def __str__(self):
            return '- - - - - - -\n{}\n{}\nc_l: {},c_r: {},\nleaf: {}'.format(
                self.label, self.feature_split_points_dict, self.c_left, self.c_right, self.is_leaf())

        class NodeValue:  # Takie zagniezdzenie deklarowanych klas to juz patologia ale nie mialem lepszego pomyslu
            def __init__(self, features_split_point_dict, feature_key):
                self.features_split_point_dict = features_split_point_dict
                self.feature_key = feature_key

            def __lt__(self, o):
                return self.features_split_point_dict[self.feature_key] < o.features_split_point_dict[self.feature_key]

            def __gt__(self, o):
                return self.features_split_point_dict[self.feature_key] > o.features_split_point_dict[self.feature_key]

            def __le__(self, o):
                return self.features_split_point_dict[self.feature_key] <= o.features_split_point_dict[self.feature_key]

            def __ge__(self, o):
                return self.features_split_point_dict[self.feature_key] >= o.features_split_point_dict[self.feature_key]

            def __repr__(self):
                return '{}\n{}'.format(self.feature_key, self.features_split_point_dict)
