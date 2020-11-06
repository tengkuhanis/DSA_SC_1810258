#============================= Node Class =====================================
class Node:
    #default value of data and link is none if no data is passed
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link

    #-----------method to update the data of the Node--------------------------
    def updateData(self, data):
        self.data = data

    #-----------method to set Link for the Next Node---------------------------
    def setLink(self, node):
        self.link = node

    #----------method returns data stored in the Node--------------------------
    def getData(self):
        return self.data

    #-----method returns address of the next Node // goes to the Next Node-----
    def getNextNode(self):
        return self.link

# =========================== LinkedList class ================================
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    #--------method adds elements to the left of the Linked List---------------
    def addToStart(self, data):# 21
        # create a temporary node
        tempNode = Node(data)
        tempNode.setLink(self.head)
        self.head = tempNode
        del tempNode
        if self.tail is None:
            self.tail = self.head

    # ------method adds elements to the right of the Linked List---------------
    def addToEnd(self, data): # data = 16
        start = self.head
        if start is None:
            self.addToStart(data)
        else:
            while start.getNextNode():
                start = start.getNextNode()
            tempNode = Node(data) # data = 16 : link = None
            start.setLink(tempNode)
            del tempNode
            self.tail = start.getNextNode()
        return True

    # -------------method displays Linked List---------------------------------
    def display(self):
        start = self.head
        if start is None:
            print("Empty List!!!")
            return False

        while start:
            print(str(start.getData()), end=" ")
            start = start.link
            if start:
                print("-->", end=" ")
        print()

    # --------------method returns length of linked list-----------------------
    def length(self):
        start = self.head
        size = 0
        while start:# start != None
            size += 1
            start = start.getNextNode()
        #print(size)
        return size

    # ----------method returns index of the received data----------------------
    def index(self, data):
        start = self.head
        position = 1

        while start:
            if start.getData() == data:
                return position
            else:
                position += 1
                start = start.getNextNode()


    #---------- method removes item passed from the Linked List----------------
    def remove(self, item):
        start = self.head
        previous = None
        found = False

        #------------ search element in list-----------------------------------
        while not found:
            if start.getData() == item:
                found = True
            else:
                previous = start
                start = start.getNextNode()

        #---- if previous is None then the data is found at first position-----
        if previous is None:
            self.head = start.getNextNode()
        else:
            previous.setLink(start.getNextNode())

        # if the tail is linked to the data
        if self.tail is start:
            self.tail = previous
        return found

    # -------------method returns max element from the List--------------------
    def Max(self):
        start = self.head
        largest = start.getData()
        while start:
            if largest < start.getData():
                largest = start.getData()
            start = start.getNextNode()
        return largest

    # -----------method returns minimum element of Linked list-----------------
    def Min(self):
        start = self.head
        smallest = start.getData()
        while start:
            if smallest > start.getData():
                smallest = start.getData()
            start = start.getNextNode()
        return smallest

    # --------------method pushes element to the Linked List-------------------
    def push(self, data):
        start = self.tail
        if start is None:
            self.addToStart(data)
        else:
            tempNode = Node(data)
            start.setLink(tempNode)
            del tempNode
            self.tail = start.link
        return True

    #--- method removes and returns the last element from the Linked List------
    def pop(self):
        start = self.head
        previous = None

        while start.getNextNode():
            previous = start
            start = start.getNextNode()

        self.tail = previous

        if previous is None:
            self.head = None
        else:
            previous.setLink(None)
            data = start.getData()
            del start
            return data

    #------------------method to clear linked list-----------------------------
    def clear(self):
        self.head = None
        self.tail = None
        return True

    # ------method returns count of Element recieved---------------------------
    def count(self, element):
        start = self.head
        count1 = 0

        while start:
            if start.getData() == element:
                count1 += 1
            start = start.getNextNode()
        return count1

#============================ Assignment 2 ====================================

#1----------method to print first K elements in the Linked List----------------
    def displayFirstK(self, k):
        start = self.head
        if start is None:
            print("Empty List!!")
            return False

        while start and k:
            print(str(start.getData()), end=" ")
            start = start.link
            k -= 1
            if start and k != 0:
                print("-->", end= " ")
        print()
        if k != 0:
            print("pending {} elements".format(k))

#2-----------------method to Push in O(1)--------------------------------------
    def push(self, data):
        start = self.tail
        if start is None:
            self.addToStart(data)
        else:
            tempNode = Node(data)
            start.setLink(tempNode)
            del tempNode
            self.tail = start.link
        return True

#3 ------------------method to reverse the Linked List-------------------------
#3A-----method to reverse linked list by creating a new linked list(easy)------
    def reverse_easy(self, listA):
        listA.clear()
        start = self.head
        while start:
            listA.addToStart(start.getData())
            start = start.getNextNode()
#3B---method to reverse linked list without creating a new linked list(hard)---
    def reverse_hard(self):
        previous = None
        current = self.head
        self.tail = current
        next = None

        while current:
            next = current.link
            current.setLink(previous)
            previous = current
            current = next

        self.head = previous

#4---method to copy the content of the Linked List in a new LinkedList Object---
    def copylist(self,listA):
           listA.clear()
           start = self.head
           while start:
               listA.push(start.getData())
               start = start.getNextNode()

#5 ------------method to convert the Linked List to a List---------------------
    def LLtoArray(self):
        current = self.head
        size = self.length()
        array = []

        while current:
            array.append(current.getData())
            current = current.getNextNode()

        for i in range(size):
            print("{}".format(array[i]), end=", ")

#6------------method to Check if the Linked List is Sorted --------------------
    def checkifsort(self):
        current = self.head
        next = current.getNextNode()
        order = 0

        if current is None:
            print("Empty List!!!")
            return False

        while next:
            if next.getData() > current.getData():
                if order == 0:
                    order = 1
                elif order == -1:
                    return False
            elif next.getData() < current.getData():
                if order == 0:
                    order = -1
                elif order == 1:
                    return False
            current = next
            next = next.getNextNode()

        return True

#7--- method to Swap 2 indexes in the Linked List w/o creating new LL----------
    def swap(self,x,y):
        current = self.head
        k = 1
        swapx = None
        swapy = None

        while current:
            if k is x:
                swapx = current
            if k is y:
                swapy = current
            current = current.getNextNode()
            k += 1

        if swapx and swapy:
            temp = swapx.getData()
            swapx.updateData(swapy.getData())
            swapy.updateData(temp)
        else:
            print("List is not big enough")

#=========================== creating LinkedList ==============================
myList = LinkedList()
easylist = LinkedList()

#----------- adding some elements to the start of LinkedList-------------------
myList.addToStart(4)
myList.addToStart(3)
myList.addToStart(2)
myList.addToStart(1)
print("First Linked List Created:")
myList.display()
# 1 --> 2 --> 3 --> 4 --> None

# -------------adding some elements to the End of the LinkedList---------------
myList.addToEnd(13)
myList.addToEnd(3)
print("\n\nTwo nodes were added to the tail:")
myList.display()
# 1 --> 2 --> 3 --> 4 --> 13 --> 3 --> None

#---------------printing length------------------------------------------------
print("\nThe length of this linked list:")
print(myList.length())

#------------------ printing index of an element-------------------------------
print("\nIndex of 12:")
print(myList.index(12))
print("\nIndex of 13:")
print(myList.index(13))

# --------------removing an element--------------------------------------------
print("\nNode 1 were removed. The new linked list is:")
print(myList.remove(1))
myList.display()
print("\nNode 13 were removed. The new linked list is:")
print(myList.remove(13))
myList.display()

# -------------printing max and min element------------------------------------
print("\nMax number in the LL is:")
print(myList.Max())
print("\nMin number in the LL is:")
print(myList.Min())

#------------ pushing elements-------------------------------------------------
print(myList.push(10))
print(myList.push(10))
print("\nTwo nodes were pushed. The new LL is:")
myList.display()

# -----------popping elements---------------------------------------------------
print(myList.pop())
print("\nOne node were popped. The new LL is:")
myList.display()


# --------printing count of particular element in the List---------------------
print("\nCounts of 1, 10 & 3 in the LL respectively is:")
print(myList.count(1))
print(myList.count(10))
print(myList.count(3))

# ------------clearing the list-------------------------------------------------------
#print(myList.clear())
#myList.display()

#============================ Assignment 2 ====================================

#1 -------------------printing first K elements---------------------------------
print("\nThe first 2 elements in the LL is:")
myList.displayFirstK(2)
print("\nThe first 4 elements in the LL is:")
myList.displayFirstK(6)

#2 -------------------printing Pushed in O(1)-----------------------------------
myList.push(20)
myList.addToStart(13)
myList.addToStart(12)
myList.addToStart(11)
print("\nLL when pushed in O(1):")
myList.display()

#3 - Reversed Linked List :
#3a---------printing reversed LL by creating a new linked list (easy)-----------
myList.reverse_easy(easylist)
print("\nLL is reversed by creating a new LL:")
easylist.display()
#3b---------printing reversed LL without creating a new linked list (hard)------
myList.reverse_hard()
print("\nLL is reversed without creating a new LL:")
myList.display()

#4 ----------printing the copied Linked List in a new LinkedList Object---------
myList.copylist(easylist)
print("\nThe reversed LL is copied in a new LL object:")
easylist.display()

#5 ------------printing converted linked list to a list-------------------------
print("\nThe Linked List were changed to a List:")
myList.LLtoArray()


#6 ------------------printing to check if the list is sorted-------------------
print("\n\nIs the linked list sorted? Yes=True, No=False:")
print(myList.checkifsort())

#7 ------printing indexes swapping in the Linked List w/o creating new LL------
myList.swap(1,9)
myList.swap(1,8)
myList.swap(7,8)
myList.swap(1,7)
myList.swap(1,6)
myList.swap(2,6)
myList.swap(2,5)
myList.swap(5,6)
print("\nIndexes were swapped. The LL become:")
myList.display()

print("\nIs the list sorted? Yes=True, No=False")
print(myList.checkifsort())
