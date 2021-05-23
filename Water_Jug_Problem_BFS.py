import collections

def main():                                    
    starting_node = [[0, 0]]    #Initial stage is defined
    jugs = get_jugs()           #Assigning user inputs for jug capacities
    goal_amount = get_goal(jugs)    #Assigning the target volume user needed
    check_dict = {}                 #a dictionary storing visited nodes
    search(starting_node, jugs, goal_amount, check_dict)    #Calling search function with attributes
   

def get_index(node):

    return pow(7, node[0]) * pow(5, node[1])  #returns a key value for a given node


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


def is_goal(path, goal_amount):         #In this function checking whether the goal is achieved

    print("Checking if the gaol is achieved...")
    
    return path[-1][0] == goal_amount or path[-1][1] == goal_amount 


def been_there(node, check_dict):    #This function will return True, if the given node is already visited
    
    print("Checking if {0} is visited before...".format(node))

    return check_dict.get(get_index(node), False)


def next_transitions(jugs, path, check_dict):  #This function will returns list of all possible transitions whcih do not cause loops

    print("Finding next transitions and checking for the loops...")
    
    result = []
    next_nodes = []
    node = []
    
    a_max = jugs[0]
    b_max = jugs[1]
    
    a = path[-1][0]  # initial amount in the first jug
    b = path[-1][1]  # initial amount in the second jug

    # 1. fill in the first jug
    node.append(a_max)
    node.append(b)
    if not been_there(node, check_dict):
        next_nodes.append(node)
    node = []

    # 2. fill in the second jug
    node.append(a)
    node.append(b_max)
    if not been_there(node, check_dict):
        next_nodes.append(node)
    node = []

    # 3. second jug to first jug
    node.append(min(a_max, a + b))
    node.append(b - (node[0] - a))  # b - ( a' - a)
    if not been_there(node, check_dict):
        next_nodes.append(node)
    node = []

    # 4. first jug to second jug
    node.append(min(a + b, b_max))
    node.insert(0, a - (node[0] - b))
    if not been_there(node, check_dict):
        next_nodes.append(node)
    node = []

    # 5. empty first jug
    node.append(0)
    node.append(b)
    if not been_there(node, check_dict):
        next_nodes.append(node)
    node = []

    # 6. empty second jug
    node.append(a)
    node.append(0)
    if not been_there(node, check_dict):
        next_nodes.append(node)

    # create a list of next paths
    for i in range(0, len(next_nodes)):
        temp = list(path)
        temp.append(next_nodes[i])
        result.append(temp)

    if len(next_nodes) == 0:        
        print("No more unvisited nodes...\nBacktracking...")
    else:
        print("Possible transitions: ")
        for nnode in next_nodes:
            print(nnode)

    return result     #Returns list of all possible transitions whcih do not cause loops


def transition(old, new, jugs):   #returns a string explaining the transition from old state/node to new state/node
    
    a = old[0]         #old: a list representing old state/node
    b = old[1]         
    a_prime = new[0]    #new: a list representing new state/node
    b_prime = new[1]    
    a_max = jugs[0]     #jugs: a list of two integers representing volumes of the jugs
    b_max = jugs[1]     

    if a > a_prime:
        if b == b_prime:
            return "Removing {0}-liter jug:\t\t\t".format(a_max)
        else:
            return "Pour {0}-liter jug into {1}-liter jug:\t".format(a_max, b_max)
    else:
        if b > b_prime:
            if a == a_prime:
                return "Removing {0}-liter jug:\t\t\t".format(b_max)
            else:
                return "Pour {0}-liter jug into {1}-liter jug:\t".format(b_max, a_max)
        else:
            if a == a_prime:
                return "Fill {0}-liter jug:\t\t\t".format(b_max)
            else:
                return "Fill {0}-liter jug:\t\t\t".format(a_max)


def print_path(path, jugs): #printing the goal path
    
    print("Starting from:\t\t\t\t", path[0])
    for i in  range(0, len(path) - 1):
        print(i+1,":", transition(path[i], path[i+1], jugs), path[i+1])                


def search(starting_node, jugs, goal_amount, check_dict):  #searching for a path between starting node and goal node
 
    goal = []
    accomplished = False
    
    q = collections.deque()         #A deque is a double-ended queue. It can be used to add or remove elements from both ends.
    q.appendleft(starting_node)     #inserting the value in its argument to the left end of deque
    
    while len(q) != 0:              #while loop until number of objects in q = 0
        path = q.popleft()          # to delete an argument from the left end of deque and assigning it
        check_dict[get_index(path[-1])] = True  #storing the visited nodes
        if len(path) >= 2:
            print(transition(path[-2], path[-1], jugs), path[-1])       #Printing transition paths
        if is_goal(path, goal_amount):      #Checking for the goal
            accomplished = True
            goal = path
            break

        next_moves = next_transitions(jugs, path, check_dict)       #Calling next_transitions function and assigning to next_moves
        for i in next_moves:
                q.append(i)

    if accomplished:            #Checking weather the goal is achieved
        print("The goal is achieved\nPrinting the sequence of the moves...\n")
        print_path(goal, jugs)
    else:
        print("Problem cannot be solved.")   #For example if jug 1 = 18L, jug 2 = 16L and when the target volume is 9 it can not be solved.             



if __name__ == '__main__':      #to prevent parts of code from being run when the modules are imported.
    main()