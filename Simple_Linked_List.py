class Node:
    def __init__(self,element = None):
        self.element = element
        self.next = None
    def get(self):
        return self.element

class Linked_List:
    def __init__(self):
        self.first = None
        self.size = 0
    def append(self,element):
        new = Node(element)
        if self.size == 0 :
            self.first = new
        else:
            temp = self.first
            while temp.next != None:
                temp = temp.next
            temp.next = new
        self.size += 1
        return new.element
    def remove (self,value):
        try:
            if self.size == 0:
                return False
            else:
                temp = self.first
                while temp.next.element != value: 
                    if temp.next == None:
                        break
                    else:
                        temp = temp.next
                del_node= temp.next
                temp.next = del_node.next
                del_node = None
                self.size -= 1
                return del_node + " has been removed"
        except AttributeError:
            return False
    def __len__(self):
        return self.size
    def __str__(self):
        string = "["
        temp = self.first
        while temp != None:
            string += str(temp.element)
            if temp.next != None:
                string += " -> "
            temp = temp.next
        string += "]"
        return string

if __name__ == "__main__":
    def main():
        simple_list = Linked_List()
        simple_list.append("Node 1")
        simple_list.append("Node 2")
        print (str(simple_list))
        print (len(simple_list))
        print (simple_list.remove ("Node 22"))
    
    main()

