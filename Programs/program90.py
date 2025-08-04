
class Node:
    def __init__(self,No):
        self.Data=No
        self.next=None

class SinglyLL:
    def __init__(self):
        self.first=None
        self.iCount=0
    #8
#######################################################################
    def InsertFirst(self,No):
        newn=Node(No)

        if(self.first==None):   #LL is empty
            self.first=newn
        else:                   #LL atleast contains 1 node
            newn.next=self.first
            self.first=newn

        self.iCount=self.iCount+1
#######################################################################

    def InsertLast(self,No):
        pass
#######################################################################

    def Display(self):
        temp=self.first
        while(temp!=None):
            print(f"| {temp.Data} |->",end=" ")
            temp=temp.next
        print("None")
        
#######################################################################

    def Count(self):
        return self.iCount
    
#######################################################################

def main():
    print("Demonstration of Singly linear linked List")
    sobj=SinglyLL()
    sobj.InsertFirst(51)
    sobj.InsertFirst(21)
    sobj.InsertFirst(11)

    sobj.Display()

    iRet=sobj.Count()
    print("Number of Nodes in LL are:",iRet)

    

if __name__=="__main__":
    main()
