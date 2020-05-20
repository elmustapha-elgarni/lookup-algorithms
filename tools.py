

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
    interface = None

#----insérer une adresse en binaire ------
def insert(node,l,interface):
    if (l):
        if (l[0] == 0):
            if(node.left == None):
                node.left=Node()
            insert(node.left, l[1:],interface)
        elif (l[0] == 1):
            if(node.right == None):
                node.right=Node()
            insert(node.right, l[1:],interface)
    else:
        node.interface = interface

#-------------insérer  addresse ip-------------
def insert_ip(node,s,interface):
    l = stringToList(s)
    insert(node,l,interface)


#----chercher next hope | entrer adresse en binaire---

def search(node,dst,interface):
    if(node.interface == None):
        inter = interface
    else:
        inter = node.interface
    if (dst == []):
        return (inter)
    else:
        if (dst[0] == 0):
            if(node.left == None):
                return (inter)
            else:
                return (search(node.left, dst[1:], inter))
        else:
            if(node.right == None):
                return(inter)
            else:
                return(search(node.right, dst[1:],inter))

def search_ip(node,dst):
    s = ip_to_bin(dst)
    l= stringToList(s)
    return(search(node,l,node.interface))

#---- Draw a tree------
def drawtree(root):
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1

    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y - 20)
            s=str(node.interface)
            t.write(s, align='center', font=('Arial', 10, 'normal'))
            draw(node.left, x - dx, y - 60, dx / 2)
            jumpto(x, y - 20)
            draw(node.right, x + dx, y - 60, dx / 2)

    import turtle
    t = turtle.Turtle()
    t.speed(0);
    turtle.delay(0)
    h = height(root)
    jumpto(0, 30 * h)
    draw(root, 0, 30 * h, 50 * h)
    t.hideturtle()
    turtle.mainloop()


def build_tree(table):
    root = Node()
    f = open(table, 'r')
    lines = f.readlines()
    for x in lines:
        s = x.split()
        insert_ip(root, s[2], s[4])
    f.close()
    return(root)

def binary_trie(root):
    fd = open("destinations.txt", 'r')
    fr = open("result-binary-tree.txt", 'w')
    lines = fd.readlines()
    for x in lines:
        dst = x.split()
        fr.write(search_ip(root,dst[0])+'\n')

    fd.close()
    fr.close()
