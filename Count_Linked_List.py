def getCount(head):
    if head == None:
        return -1
        
    curr = head.next
    count = 1
    while curr!= None:
        count +=1
        curr = curr.next
    return count