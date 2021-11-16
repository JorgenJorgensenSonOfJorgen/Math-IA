import random

#in a game where t is a multiple of n, where l = 1, what is x(p) of everyone?
# we want to outputa bunch of lines where it has p and then the % chance of winning
def genEggSet(numH, numR):
    eggSet = []
    for x in range(numH):
        eggSet.append('h')
    for x in range(numR):
        eggSet.append('r')
    return eggSet
def genPlayerSet(n,l):
    playerSet = []
    for x in range(n):
        playerSet.append([x  +1, l])
    return playerSet
def play(a,b,l,n):
    winSet = []
    for x in range(n):
        winSet.append(0)
    for x in range(100000):
        playerSet = genPlayerSet(n,l)
        eggSet = genEggSet(a,b)
        for x in range(a + b):
            egg = eggSet.pop(random.randint(0,len(eggSet) - 1))
            if egg == 'r':
                playerSet[0][1] -= 1
                if playerSet[0][1] == 0:
                    playerSet.pop(0)
                    if len(playerSet) == 1:
                        break
                else:
                    playerSet.append(playerSet.pop(0))
            else:
                playerSet.append(playerSet.pop(0))
        for x in playerSet:
            winSet[x[0] - 1] += 1
    #for x in winSet:
    return winSet
#the play function returns a winset list.
def tgraph():
    n=2
    l = 3
    for x in range(30):
        a = 3 * (x + 3)
        b = x + 3
        print(play(a,b,l,n)[0]/1000)
def lgraph():
    n=2
    a = 60
    b = 20
    for x in range(20):
        l = x + 1
        print(play(a,b,l,n)[0]/1000)
def hrgraph():
    n =2
    l=3
    for x in range(30):
        a = 40 - x -3
        b = x + 3
        print(play(a,b,l,n)[0]/1000)

def ngraph():
    a =30
    b =15
    l=1
    for x in range(5):
        n = 6 * x + 10
        winSet = play(a,b,l,n)
        for x1 in winSet:
            print(x1/1000)
        print('end')
ngraph()