from tools import build_tree,binary_trie,drawtree,stringToList,search
from tools_disjoint_prefix import disjoint_prefix_tree,disjoint_prefix_trie
#from tools_patricia import patricia_tree,search_p
from tools_multibit import insert_ip,Node,search_ip,multibit_tree,multibit_trie

#########-------Binary Trie ----------######################

root = build_tree("table_routage.txt")
binary_trie(root)


#########-------Disjoint-prefix binary trie----------#################################

root1 = disjoint_prefix_tree("table_routage.txt")
disjoint_prefix_trie(root1)

#########-------Patricia----------#################################

#root2 = patricia_tree("table_routage.txt")
#drawtree(root)
#l = stringToList("00000101")
#print(search(root,l,root.interface))
#print(search(root1,l,root1.interface))
#drawtree(root2)
#print(search_p(root2,l))

#########-------Multibits----------#################################

root3 = multibit_tree("table_routage.txt")
multibit_trie(root3)


