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



