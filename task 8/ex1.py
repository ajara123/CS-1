#Exercise 1
#function chop that creates a list and modifies it, removing the first and last elements, and returns "None"

def chop(ListNum):
    del ListNum[0] #deleting first element
    del ListNum[len(ListNum)-1] #deleting last element
    print(ListNum)

#fucntion called middle that takes a list and returns a new list that contains all but the first and last elements

def middle(ListNum):
    NumLen=len(ListNum) #defining lenght of the list
    return (ListNum[1:NumLen-1]) 



