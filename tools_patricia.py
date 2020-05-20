

#--------decimal ip to binary
def ip_to_bin(s):
    list = s.split('.')
    x=''
    for i in list:
        x = x + '{:08b}'.format(int(i))
    return (x)
#-----------string to list
def stringToList(s):
    l = []
    if ( s =='*'):
        return(l)
    else:
        for i in s:
            l.append(int(i))
        return (l)

#----Node class --------
class Node():
    left = None
    right = None
    parent = None
    index = 0
    prefix = []
    interface = None

#----insérer une adresse en binaire ------
def insert(node,l,interface,index):
    node.index = index + 1
    node.prefix = l[:node.index]
    if (node.index < len(l) ):
        if (l[node.index] == 0):
            if(node.left == None):
                node.left=Node()
                node.left.parent=node
            insert(node.left, l,interface,node.index)
        elif (l[node.index] == 1):
            if(node.right == None):
                node.right=Node()
                node.right.parent=node
            insert(node.right, l,interface,node.index)
    else:
        node.interface = interface


#-------------insérer  addresse ip-------------
def insert_ip(node,ip,interface):
    l = stringToList(ip)
    n = len(l)
    node.index = -1
    insert(node,l,interface,node.index)

#------------- Eléminer les neouds Éliminer'les'noeuds'internes'avec'un'seul'descendant-----

def patricia_1(node):
    if(node.prefix == []):
        if(node.left != None):
            patricia_1(node.left)
        if(node.right != None):
            patricia_1(node.right)
        return()

    if(node.right == None and node.left == None):
        return()

    elif (node.left == None and node.right != None):
        if(node.interface != None):
            node.left = Node()
            node.left.interface = node.interface
            node.left.prefix=node.prefix+[0]
            node.left.parent = node
            node.interface = None
            node.left.index = node.index + 1

        patricia_1(node.right)

    elif(node.right == None and node.left != None):
        if (node.interface != None):
            node.right = Node()
            node.right.interface = node.interface
            node.right.prefix = node.prefix+[1]
            node.right.parent = node
            node.interface = None
            node.right.index = node.index + 1
        patricia_1(node.left)

    else:
        patricia_1(node.left)
        patricia_1(node.right)

def change_root(node):
    if (node.prefix == []):
        if (node.left != None and node.right == None):
            node.parent.left = node.left
            node.left.parent = node.parent
            root = node.left
            del node
            return(root)
        elif (node.right != None and node.left == None):
            node.parent.left = node.right
            node.right.parent = node.parent
            root = node.right
            del node
            return(root)
        else:
            return(node)


def patricia_2(node):
    if (node.prefix == []):
        if (node.left != None and node.right == None):
            node.parent.left = node.left
            node.left.parent = node.parent
            patricia_2(node.left)
            del node
        elif (node.right != None and node.left == None):
            node.parent.left = node.right
            node.right.parent = node.parent
            patricia_2(node.right)
            del node
        else:
            patricia_2(node.left)
            patricia_2(node.right)
        return ()
    if (node.right == None and node.left == None):
        return()

    elif (node.left == None and node.right != None):
        if (node.prefix[-1] == 0):
            node.parent.left = node.right
            node.right.parent = node.parent
            patricia_2(node.right)
            del node
            return ()
        else:
            node.parent.right = node.right
            node.right.parent = node.parent
            patricia_2(node.right)
            del node
            return()
    elif (node.left != None and node.right == None):
        if (node.prefix[-1] == 0):
            node.parent.left = node.left
            node.left.parent = node.parent
            patricia_2(node.left)
            del node
            return ()
        else:
            node.parent.right = node.left
            node.left.parent = node.parent
            patricia_2(node.left)
            del node
            return()
    else:
        patricia_2(node.right)
        patricia_2(node.left)




#----chercher next hope | entrer adresse en binaire---

def search_p(node,dst):
    if(node.left == None and node.right == None):
        if(node.prefix == dst[:node.index+1]):
            print("prefix founded")
            return (node.interface)
    if (dst[node.index] == 0 and node.left != None):
        print("left" + str(node.index))
        return (search_p(node.left, dst))
    elif(dst[node.index] == 1 and node.right != None):
        print("right" + str(node.index))
        return(search_p(node.right, dst))

def search_ip(node,dst):
    s = ip_to_bin(dst)
    l= stringToList(s)
    return(search_p(node,l,node.interface))


def patricia_tree(table):
    root = Node()
    parent = Node()
    parent.left = root
    parent.interface = "parent"
    root.parent = parent
    f = open(table, 'r')
    lines = f.readlines()
    for x in lines:
        s = x.split()
        insert_ip(root, s[2], s[4])
    f.close()
    patricia_1(root)
    patricia_2(root)
    root2 = change_root(root)
    return(root2)

def binary_trie(root):
    fd = open("destinations.txt", 'r')
    fr = open("result-binary-tree.txt", 'w')
    lines = fd.readlines()
    for x in lines:
        dst = x.split()
        fr.write(search_ip(root,dst[0])+'\n')

    fd.close()
    fr.close()
