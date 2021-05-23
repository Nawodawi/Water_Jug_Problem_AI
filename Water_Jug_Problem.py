import JugClass
import sys


jugVolume1 = int(input('Jug 1 Volume:'), 10)     #getting user input for the volume of jug one
jugVolume2 = int(input('Jug 2 Volume:'), 10)     ##getting user input for the volume of jug two


if jugVolume1 == jugVolume2:                  #checking whethere eqaul volumes are in two jugs
    print('Jugs can\'t have equal Volumes')
    sys.exit(1)

targetVolume = int(input('Target Volume:'), 10)   #getting user input for the target volume

if targetVolume > jugVolume1 and targetVolume > jugVolume2:    #Target volume cant be larger than jug volume
    print('Target volume can\'t be larger than jug Volumes')
    sys.exit(1)


smaller = JugClass.JugState(min(jugVolume1, jugVolume2), 'Jug 1')   #Assigning minimum volume jug as smaller


larger = JugClass.JugState(max(jugVolume1, jugVolume2), 'Jug 2')    #Assigning maximum volume jug as larger

def getGCD(a, b):          #Calculating the gratest common divisor of vulumes of two jugs
    larger = max(a, b)
    smaller = min(a, b)
    if larger != smaller:
        smaller = getGCD(larger - smaller, smaller)
    return smaller

def makeMove(smaller, larger):        #actions to take according to the condition
    
    if smaller.is_empty():
        smaller.fill()
        print('A -> [', smaller.currentVol, ',', larger.currentVol,']')
        return True
  
    if larger.is_full():
        larger.dump()
        print('B -> [', smaller.currentVol, ',', larger.currentVol,']')
        return True

    if not(smaller.is_empty()):
        smaller.transfer(larger)
        print('C -> [', smaller.currentVol, ',', larger.currentVol,']')
        return True

gcd = getGCD(smaller.capacity, larger.capacity)  #Assigning gcd

if targetVolume % gcd != 0:                      #Checking for a exception
    print('No possible Solution with these volumes')
    sys.exit(0)   

found_it = (smaller.currentVol + larger.currentVol) == targetVolume     
step_count = 0

while not(found_it):                            #While loop until find the solution
    makeMove(smaller, larger)
    step_count += 1
    found_it = (smaller.currentVol + larger.currentVol) == targetVolume

print('Found target volume in', step_count, 'steps')   #Printing the step count
