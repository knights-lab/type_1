from pathlib import Path

from type_1 import logger

from ete3 import Tree


def get_closest_leave(leaves_to_index: dict, prepostorder_leaves: list, tree: Tree, leave: str) -> Tuple[str, float, float]:
    index = leaves_to_index[leave]
    if index == 0:
        closest = prepostorder_leaves[index + 1]
    elif index == len(prepostorder_leaves) - 1:
        closest = prepostorder_leaves[index - 1]
    else:
        leave_1 = prepostorder_leaves[index - 1]
        leave_2 = prepostorder_leaves[index + 1]
        dist_1 = tree.get_distance(leave_1, leave)
        dist_2 = tree.get_distance(leave_2, leave)
        if dist_1 < dist_2:
            closest = leave_1
        else:
            closest = leave_2
    if closest != leave:
        dist = tree.get_distance(leave, closest)
        top_distance = tree.get_distance(leave, closest, True)
    else:
        logger.warning(f"Nearest neighbor to node {leave} is itself!")
        dist = 0
        top_distance = 0
    return closest, dist, top_distance


def read_tree(nw_path: Path) -> Tree:
    with open(nw_path) as inf:
        nw_tree = inf.readlines()

    t = Tree(nw_tree[0], format=3, quoted_node_names=True)
    t.unroot()
    return t
