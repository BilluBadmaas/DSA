class T1:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
root=T1('ROOT')
nodeA=T1('Node A')
nodeB=T1('Node B')
nodeC=T1('Node C')
nodeD=T1('Node D')
nodeE=T1('Node E')
nodeF=T1('Node F')
nodeG=T1('Node G')
root.left=nodeA
root.right=nodeB
nodeA.left=nodeC
nodeA.right=nodeD
nodeB.left=nodeE
nodeB.right=nodeF
nodeF.left=nodeG
print("Root.Right.Left.Data : ",root.right.left.data)
