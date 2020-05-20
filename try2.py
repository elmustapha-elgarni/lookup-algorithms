from tools import build_tree,binary_trie,drawtree, search,stringToList
from tools_disjoint_prefix import disjoint_prefix_tree,disjoint_prefix_trie
from tools_patricia import Node, insert_ip,patricia_tree,patricia_1,patricia_2

#########-------Binary Trie ----------######################

root = build_tree("table_routage.txt")
binary_trie(root)


#########-------Disjoint-prefix binary trie----------#################################

root1 = disjoint_prefix_tree("table_routage.txt")
disjoint_prefix_trie(root1)

#########-------Patricia----------#################################
root = Node()
parent = Node()
parent.left = root
root.parent = parent
insert_ip(root,"111","P1")
insert_ip(root,"",None)
insert_ip(root,"10","P2")
insert_ip(root,"1010","P3")
insert_ip(root,"10101","P4")
patricia_1(root)
#patricia_2(root)
drawtree(parent)