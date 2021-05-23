import collections

def main():                                    
    starting_node = [[0, 0]]    #Initial stage is defined
    jugs = get_jugs()           #Assigning user inputs for jug capacities
    goal_amount = get_goal(jugs)    #Assigning the target volume user needed
    check_dict = {}                 #a dictionary storing visited nodes
    search(starting_node, jugs, goal_amount, check_dict)    #Calling search function with attributes
   

def get_jugs():
    
    jugs = []   
    
    temp = int(input("Enter first jug capacity: "))         #Getting the user input for the 1st jug capacity
    while temp < 1:                                         #Validating the jug capacity
        temp = int(input("Enter a valid amount (Should be lager than one)): "))       
    jugs.append(temp)
    
    temp = int(input("Enter second jug capacity: "))         #Getting the user input for the 2st jug capacity
    while temp < 1:                                          #Validating the jug capacity
        temp = int(input("Enter a valid amount (Should be lager than one): "))     
    jugs.append(temp)
    
    return jugs                                              #returning jug capcities


def get_goal(jugs):

    max_amount = max(jugs[0], jugs[1])
    s = "Enter the desired amount of water (1 - {0}): ".format(max_amount)  #Getting the user input for the target volume of water
    goal_amount = int(input(s))
    while goal_amount < 1 or goal_amount > max_amount:                      #Validating the target amount of water
        goal_amount = int(input("Enter a valid amount (1 - {0}): ".format(max_amount)))
        
    return goal_amount              #Returns desired amount of water.


def search(starting_node, jugs, goal_amount, check_dict):  #searching for a path between starting node and goal node
 
    goal = []
    accomplished = False
    
    q = collections.deque()         #A deque is a double-ended queue. It can be used to add or remove elements from both ends.
    q.appendleft(starting_node)     #inserting the value in its argument to the left end of deque
    
           




if __name__ == '__main__':      #to prevent parts of code from being run when the modules are imported.
    main()