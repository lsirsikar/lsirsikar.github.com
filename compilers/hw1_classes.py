class PBF:
    pass

class OR(PBF):
    def __init__(self,f1,f2):
        self.lchild = f1
        self.rchild = f2
    def __str__(self):
        return str(self.lchild) + " " + str(self.rchild) + " |"
    def isNNF(self):
        return (self.lchild.isNNF() & self.rchild.isNNF())
    def toNNF(self):
        return self.lchild.toNNF()
        return self.rchild.toNNF()

class AND(PBF):
    def __init__(self,f1,f2):
        self.lchild = f1
        self.rchild = f2
    def __str__(self):
        return str(self.lchild) + " " + str(self.rchild) + " &"
    def isNNF(self):
        return (self.lchild.isNNF() & self.rchild.isNNF())
    def toNNF(self):
        return self.lchild.toNNF()
        return self.rchild.toNNF()
    
class NOT(PBF):
    def __init__(self,f):
        self.child = f
    def __str__(self):
        return str(self.child) + " !"
    def isNNF(self):
        if ( self.child.__class__ == OR or self.child.__class__ == AND or self.child.__class__ == NOT ):
            return False
        else:
            return True
    def toNNF(self):
        if( self.child.__class__ == OR ):
            return AND( NOT(self.child.lchild).toNNF(), NOT(self.child.rchild).toNNF() ).toNNF()
        elif( self.child.__class__ == AND):
            return OR ( NOT(self.child.lchild).toNNF(), NOT(self.child.rchild).toNNF() ).toNNF()

class PROP(PBF):
    def __init__(self,p):
        self.prop = p
    def __str__(self):
        return self.prop
    def isNNF(self):
        return True
    def toNNF(self):
        return PROP

def parse(str_arr):
    stack = []
    
    for i in range(0,len(str_arr)):
        if str_arr[i] == '|':
            y = stack.pop()
            x = stack.pop()
            stack.append(OR(x,y))
        elif str_arr[i] == '&':
            y = stack.pop()
            x = stack.pop()
            stack.append(AND(x,y))
        elif str_arr[i] == '!':
            stack.append(NOT(stack.pop()))
        else:
            stack.append(PROP(str_arr[i]))
            
    if(len(stack) > 1):
        print "not as many operands"
    
    return stack.pop()

x = AND(PROP("x"), NOT(OR(PROP("y"),PROP("z"))))
y = AND(PROP("x"), AND(NOT(PROP("y")),NOT(PROP("z"))))
print x.__str__()
if x.isNNF() == False:
    print "False"
else:
    print "True"

print y.__str__()
if y.isNNF() == False:
    print "False"
else:
    print "True"

x.toNNF()
x.isNNF()

str_arr = ['x', 'y', '!', 'z', '!', '|', '&']
z = parse(str_arr)
print str(z)
