import math

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swap(num_one, num_two):
    temp = num_one
    num_one = num_two
    num_two = temp
        
    return num_one, num_two

def gcd(num_one, num_two):
    if num_one < num_two:
        swap(num_one, num_two)
        
    if 0 in [num_one, num_two]:
        return max(num_one, num_two)

    multiplier = math.floor(num_one/num_two)
    return gcd(num_two, num_one - math.floor(num_two * multiplier))


def insertGreatestCommonDivisors(head):
    node = head
    
    while node.next:
        temp = node.next
        new_node = ListNode(gcd(node.val, temp.val))
        new_node.next = temp
        
        node = temp
        
print()