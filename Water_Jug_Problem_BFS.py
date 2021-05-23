import collections

def main():                                    
    starting_node = [[0, 0]]    #Initial stage is defined
    jugs = get_jugs()           #Assigning user inputs for jug capacities
   

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




if __name__ == '__main__':      #to prevent parts of code from being run when the modules are imported.
    main()