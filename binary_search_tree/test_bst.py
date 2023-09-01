from .bst import TreeNode, BinarySearchTree


def test_create_tree():
    bst = BinarySearchTree(TreeNode(10, TreeNode(5), TreeNode(15)))
    assert bst.root.value == 10
    assert bst.root.left_child.value == 5


def test_insert_new_value():
    bst = BinarySearchTree(TreeNode(10, TreeNode(5), TreeNode(15)))
    bst.recursive_insert(2)
    expected = BinarySearchTree(TreeNode(10, TreeNode(5, TreeNode(2)), TreeNode(15)))
    assert bst == expected


def test_search_existing_value():
    bst = BinarySearchTree(TreeNode(10, TreeNode(5), TreeNode(15)))
    assert bst.recursive_search(5).value == 5


def test_search_absent_value():
    bst = BinarySearchTree(TreeNode(10, TreeNode(5), TreeNode(15)))
    assert not bst.recursive_search(3)


def test_delete_childless_node():
    bst = BinarySearchTree(TreeNode(10, TreeNode(5, TreeNode(1)), TreeNode(15)))
    bst.delete(1)
    expected = BinarySearchTree(TreeNode(10, TreeNode(5), TreeNode(15)))
    assert bst == expected


def test_delete_node_with_left_child():
    bst = BinarySearchTree(TreeNode(10, TreeNode(5, TreeNode(2)), TreeNode(15)))
    bst.delete(5)
    expected = BinarySearchTree(TreeNode(10, TreeNode(2), TreeNode(15)))
    assert bst == expected


def test_delete_node_with_right_child():
    bst = BinarySearchTree(
        TreeNode(10, TreeNode(5), TreeNode(15, right_child=TreeNode(20)))
    )
    bst.delete(15)
    expected = BinarySearchTree(TreeNode(10, TreeNode(5), TreeNode(20)))
    assert bst == expected


def test_successor_node_is_right_child():
    bst = BinarySearchTree(
        TreeNode(10, TreeNode(5), TreeNode(15, TreeNode(12), TreeNode(20)))
    )
    bst.delete(15)
    expected = BinarySearchTree(TreeNode(10, TreeNode(5), TreeNode(20, TreeNode(12))))
    assert bst == expected


def test_successor_node_is_left_child():
    bst = BinarySearchTree(
        TreeNode(
            10, TreeNode(5), TreeNode(15, TreeNode(12), TreeNode(20, TreeNode(18)))
        )
    )
    bst.delete(15)
    expected = BinarySearchTree(
        TreeNode(10, TreeNode(5), TreeNode(18, TreeNode(12), TreeNode(20)))
    )
    assert bst == expected


def test_successor_node_has_right_child():
    bst = BinarySearchTree(
        TreeNode(
            10,
            TreeNode(5),
            TreeNode(
                15, TreeNode(12), TreeNode(20, TreeNode(18, right_child=TreeNode(19)))
            ),
        )
    )
    bst.delete(15)
    expected = BinarySearchTree(
        TreeNode(
            10,
            TreeNode(5),
            TreeNode(18, TreeNode(12), TreeNode(20, TreeNode(19))),
        )
    )
    assert bst == expected
