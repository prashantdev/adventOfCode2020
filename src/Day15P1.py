#nums=[0,3,6]
nums=[12,1,16,3,11,0]
numsSpoken=[]
lastSpokenNum=-1

def speakNum(turn):
    global lastSpokenNum
    if turn<len(nums):
        currentNum=nums[turn]
    else:
        lastSpokenNum = numsSpoken[len(numsSpoken)-1]
        try:
            lastSpokenNumWasSpokenPreviouslyAtIndex = len(numsSpoken) - numsSpoken[len(numsSpoken)-2::-1].index(lastSpokenNum)-1
            currentNum = len(numsSpoken) - lastSpokenNumWasSpokenPreviouslyAtIndex
            #print(" lastSpokenNum="+str(lastSpokenNum)+" lastSpokenNumWasSpokenPreviouslyAtIndex:"+str(lastSpokenNumWasSpokenPreviouslyAtIndex))
        except ValueError as e:#lastSpokenNum was never spoken earlier
            currentNum = 0
            
    numsSpoken.append(currentNum)
    if (turn==2019):
        print("turn="+str(turn+1)+" lastSpokenNum="+str(lastSpokenNum)+" spoken:"+str(currentNum))
        numsSpoken.sort()
        print(numsSpoken)

turn=0
while turn<2020:
    speakNum(turn)
    turn=turn+1
    
#30000000
#29999999
