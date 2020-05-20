
def patricia(node):
    if(node.right == None and node.left == None):
        print("fin")
        return()

    elif (node.left == None and node.right != None):
        if(node.interface != None):
            node.left = Node()
            node.left.interface = node.interface
            node.interface = None
            print('copy interface')
            node.left.index = node.index + 1
            patricia(node)
        else:
            if(node.prefix[-1] == 0):
                node.parent.left = node.right
                node.right.parent = node.parent
                nextnode = node.right
                del node
                print("delete left")
                patricia(nextnode)
                return ()
            else:
                node.parent.right = node.right
                node.right.parent = node.parent
                nextnode = node.right
                del node
                print("delete right")
                patricia(nextnode)
                return ()

    elif(node.right == None and node.left != None):
        if (node.interface != None):
            node.right = Node()
            node.right.interface = node.interface
            node.interface = None
            print("copy")
            node.right.index = node.index + 1
            patricia(node)
        else:
            if(node.prefix[-1] == 0):
                node.parent.left = node.left
                node.left.parent = node.parent
                nextnode = node.left
                del node
                print("delete left")
                patricia(nextnode)
                return ()
            else:
                node.parent.right = node.left
                node.left.parent = node.parent
                nextnode = node.left
                del node
                print("delete right")
                patricia(nextnode)
                return ()
    else:
        patricia(node.left)
        patricia(node.right)