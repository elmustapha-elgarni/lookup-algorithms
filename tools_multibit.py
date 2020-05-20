

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
    first = None
    second = None
    third = None
    fourth = None
    interface = None

#----insérer une adresse en binaire ------
def insert(node,l,interface):
    print("call")
    print(l)
    if (l != []):
        if (l[:2] == [0,0]):
            if(node.first == None):
                node.first=Node()
            insert(node.first, l[2:],interface)
            return
        elif(l[:2] == [0, 1]):
            if (node.second == None):
                node.second = Node()
            insert(node.second, l[2:], interface)
            return
        elif (l[:2] == [1, 0]):
            if (node.third == None):
                print("hhh")
                node.third = Node()
            insert(node.third, l[2:], interface)
            return
        elif (l[:2] == [1, 1]):
            if (node.fourth == None):
                node.fourth = Node()
            insert(node.fourth, l[2:], interface)
            return
        else:
            if(l[0] == 0):
                if (node.first == None):
                    node.first = Node()
                if (node.first.interface == None):
                    insert(node.first, l[1:], interface)
                if (node.second == None):
                    node.second = Node()
                if (node.second.interface == None):
                    insert(node.second, l[1:], interface)
                return
            else:
                print("here")
                if (node.third == None):
                    node.third = Node()
                if(node.third.interface == None):
                    insert(node.third, l[1:], interface)
                if (node.fourth == None):
                    node.fourth = Node()
                if(node.fourth.interface == None):
                    insert(node.fourth, l[1:], interface)
                return

    else:
        print("interf")
        node.interface = interface
        return
#-------------insérer  addresse ip-------------
def insert_ip(node,s,interface):
    l = stringToList(s)
    insert(node,l,interface)


#----chercher next hope | entrer adresse en binaire---

def search(node,dst,interface):
    print("look")
    print(dst)
    if(node.interface == None):
        inter = interface
    else:
        inter = node.interface
    if (dst == []):
        return (inter)
    else:
        if (dst[:2] == [0,0]):
            if(node.first == None):
                return (inter)
            else:
                return (search(node.first, dst[2:], inter))
        elif(dst[:2] == [0,1]):
            if(node.second == None):
                return (inter)
            else:
                return (search(node.second, dst[2:], inter))
        elif(dst[:2] == [1,0]):
            if(node.third == None):
                return (inter)
            else:
                return (search(node.third, dst[2:], inter))
        elif(dst[:2] == [1,1]):
            if(node.fourth == None):
                return (inter)
            else:
                return (search(node.fourth, dst[2:], inter))
        else:
             return(inter)


def search_ip(node,dst):
    s = ip_to_bin(dst)
    l= stringToList(s)
    return(search(node,l,node.interface))


def multibit_tree(table):
    root = Node()
    f = open(table, 'r')
    lines = f.readlines()
    for x in lines:
        s = x.split()
        insert_ip(root, s[2], s[4])
    f.close()
    return(root)

def multibit_trie(root):
    fd = open("destinations.txt", 'r')
    fr = open("result-multibit.txt", 'w')
    lines = fd.readlines()
    for x in lines:
        dst = x.split()
        fr.write(search_ip(root,dst[0])+'\n')

    fd.close()
    fr.close()
