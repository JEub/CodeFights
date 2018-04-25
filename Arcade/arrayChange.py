"""You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. 
Find the minimal number of moves required to obtain a strictly increasing sequence from the input."""

def arrayChange(inputArray):
    # Setting change as list in case later you want the output of each change value.
    change = [0]
    
    # Iterating over all pairs and getting each value to change.
    while len(inputArray)>1:
        d=0
        if inputArray[0]>=inputArray[1]:
            d = abs(inputArray[0]-inputArray[1])+1
            change.append(d)
        else:
            change.append(0)
           
        # Removing the first value of the original array.
        inputArray.pop(0)
        inputArray[0]=inputArray[0]+d
            
    print(sum(change))
    return sum(change)
