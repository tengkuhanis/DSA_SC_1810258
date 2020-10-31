#NODE CLASS
#test_node(15)
#test_node.setLink(node_2)
# *default constructre

class Node:
    #default value of data and link is none if no data
    def _init_(self, data=None, link=None):
        self.data = data
        self.link = link

    #method to update the data of the Node
    def updateData(self, data):
        self.data = data

    #method to set Link for the Next Node
    def setLink(self, node):
        self.link = node

    #method returns data stored in the Node
    def getData(self):
        return self.data
   
   #method returns address of the Next Node // goes to the Next Node
   def getNextNode(self):
        return self.link



#LINKED LIST CLASS

class LinkedList:
    def _init_(self):
        self.head = None
        self.tail = None


    #method adds elements to the left of the LL
    def addToStart(self, data): # 21
        #create a temporary node
        tempNode = Node(data)
        tempNode.setLink(self.head)
        self.head = tempNode
        del tempNode


    #method adds elements to the right of the LL
    def addToEnd(self, data): # data = 16
        start = self.head
        tempNode = Node(data) # data = 16 : link = None
        # start = 5
        #reach the last element/ the tail:
        while start.getNextNode():
            start = start.getNextNode()
            start.setLink(tempNode)
        del tempNode
        return True

    #method displays Linked List
    def display(self):
        start = self.head
        #what if there is no element at all? - check head
        if start is None:
            print("Empty List!!!")
            return False

        while start:
            print(str(start.getData()), end=" ")
            # the end space fx is to prevent it from printing new line
            start = start.link
            if start:
                print("-->", end=" ")
        print ()

        #method returns length of LL
        def length(self):
            start = self.head
            size = 0
            while start: #start != none
                size += 1
                start = start.getNextNode()
             print(size)
             return size

         
        #method returns index of the received data
        def index(self, data):
            start = self.head
            position = 1

            while start:
                if start.getData() == data:
                    return position
                else:
                    position += 1
                    start = start.getNextNode()

        #method removes item passed from the LL
        def remove(self, item):
            start = self.head
            previous =  None
            found = False
            
            #search element in list
            while not found:
            if start.getData() == item:
                found == True
            else:
                previous = start
                start = start.getNextNode()
                
            #if previous is None then the data is found at 1st position
            if previous is None:
                self.head = start.getNextNode()
            else:
                previous.setLink(start.getNextNode())
            return found
            
        #method returns maximum element from list
        def Max(self):
            start = self.head
            largest = start.getData()
            while start:
                if largest < start.getData():
                    largest = start.getData()
                start = start.getNextNode()
            return largest


        #method returns minimum element from list
        def Min(self):
            start = self.head
            smallest = start.getData()
            while start:
                if smallest > start.getData():
                    smallest = start.getData()
                start = start.getNextNode()
            return smallest

        #method pushes element to the LL
        def push(self, data):
            self.addToEnd(data)
            return True

        #method removes and returns the last element from LL
        def pop(self):
            start = self.head
            previous = None

            while start.getNextNode():
                previous = start
                start = start.getNextNode()
                
            if previous is None:
                self.head = None  
            else:
                previous.setLink(None) // to tell the prev element that you are the new last element
                data = start.getData()
                del start
                return data

         #method to clear LL
         def clear(self):
             self.head = None
             return True

         #method returns count of element received
         def count (self, element):
         start = self.head
         count1 = 0
         while start:
            if start.getData() == element:
                count1 += 1
            start = start.getNextNode()
         return count1




#creating Linked List
myList = LinkedList()

#adding some elements to the start of LL
myList.addToStart(5)
myList.addToStart(4)
myList.addToStart(3)
myList.addToStart(2)
myList.addToStart(1)
#1 -> 2 -> 3 -> 4 -> 5 -> None

myList.display()

#adding some element to the End of LL
myList.addToend(13)
myList.addToend(3)
myList.addToend(31)
myList.display()
#1 -> 2 -> 3 -> 4 -> 5 -> 13 -> 3 -> 31 -> None

#printing length
print(myList.length())

#printing index of an element
print(myList.index(12))

#removing an element
print(myList.remove(12))

myList.display()

#printing max and min element
print(myList.Max())
print(myList.Min())

#pushing and poping elements
print(myList.push(31))
myList.display()
print(myList.pop())
myList.display()

#printing count of particular element in the list
print(myList.count(3))

print(myList.clear())
myList.display()


#sidenote: time complexity for adding to end = O(n) - bcs we need to go thru all elements
