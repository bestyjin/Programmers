class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
    
class DoublyLinkedList:
    def __init__(self, cacheSize):
        self.cacheSize = cacheSize
        self.head = Node("")
        self.tail = Node("")
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def LRU(self, data, time):
        node = self.head.next
        while(node.data):
            if node.data == data:
                time=self.cacheHit(node, data, time)
                return time
            node = node.next
        time=self.cacheMiss(data, time)
        return time
    
    # 원소 맨앞으로 이동
    def cacheHit(self, node, data, time):
        time += 1
        self.removeNode(node)
        self.addFront(data)
        return time
        
    
    # node 삭제
    def removeNode(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        
    # head 의 바로 뒤에 원소 넣기
    def addFront(self, data):
        newNode = Node(data)
        self.head.next.prev = newNode
        newNode.next = self.head.next
        self.head.next = newNode
        newNode.prev = self.head
        
    # 원소의 맨앞에 추가 (cacheSize 보다 커지면 tail에 가까운 노드 삭제)
    def cacheMiss(self, data, time):
        time += 5
        self.addFront(data)
        if self.totalLen() > self.cacheSize:
            self.removeTail()
        return time
        
    # linked list 의 총 길이 반환
    def totalLen(self):
        answer = 0
        node = self.head.next
        while(node.data):
            answer += 1
            node = node.next
        return answer
        
    # tail 에 가장 가까운 원소 삭제
    def removeTail(self):
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

def solution(cacheSize, cities):
    time = 0
    linkedList = DoublyLinkedList(cacheSize)
    for city in cities:
        time=linkedList.LRU(city.lower(), time)
    return time