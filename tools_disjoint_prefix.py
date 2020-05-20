from tools import build_tree,Node,search_ip

def leaf_pushing(node,interface):
    if (node.interface == None):
        inter = interface
    else:
        inter = node.interface
    if(node.left == None and node.right == None):
        if(node.interface==None):
            node.interface = inter
        return()
    else:
        if(node.left == None):
            node.left = Node()
        if(node.right == None):
            node.right = Node()
        leaf_pushing(node.left, inter)
        leaf_pushing(node.right,inter)
        node.interface = None

############## Etablir l'arbre apres leaf pushing#############
def disjoint_prefix_tree(table):
    root=build_tree(table)
    leaf_pushing(root,root.interface)
    return (root)


##########---- Faire la recherche ---########
def disjoint_prefix_trie(root):
    fd = open("destinations.txt", 'r')
    fr = open("result-disjoint-prefix.txt", 'w')
    lines = fd.readlines()
    for x in lines:
        dst = x.split()
        fr.write(search_ip(root,dst[0])+'\n')

    fd.close()
    fr.close()

