def is_sum_tree(self, node):
        
    self.isSumTree = True
        
    def getSum(node):
        if not node:
            return 0
                
        if not(node.left or node.right):
            return node.data
                
        childSubtreeSum = getSum(node.left) + getSum(node.right)
            
        if node.data != childSubtreeSum:
            self.isSumTree = False
            
        return node.data + childSubtreeSum
        
    getSum(node)
        
    return self.isSumTree