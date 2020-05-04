from queue import Queue
​
def truckTour(petrolpumps):
    # Your code here.
    # we need to know the index of the pump that allows us to
    # travel along the entire circle 
    route = Queue()
​
    # put all of the pumps in the queue 
    for p in petrolpumps:
        # insert the current pump into the queue 
        route.put(p)
​
    start = 0 
    tank = 0
    # keep track of how many pumps we've traversed 
    traversed = 0
​
    # to exhaustively check if we've found a pump that allows us to 
    # traverse all of the pumps, we could:
    # 1. use a queue data structure 
    # 2. use a while loop and loop until we have traversed all of
    # the pumps; when the while loop reaches the end of the array,
    # we'd need to circle back to the beginning by resetting the
    # index 
​
    # loop over every pair in the input array 
    while traversed < len(petrolpumps):
        # check how much gas is left after traveling to the next pump 
        # at the current pump, keep track of gas - distance 
        pump = route.get()
        gas, distance = pump
        # update our tank amount with the difference between
        # gas and distance 
        tank += (gas - distance)
        # if we see that we have a negative amount of gas left, 
        if tank < 0:
            # that means this pump is not valid 
            # consider the next pump
            start += traversed + 1
            # reset the tank 
            tank = 0
            traversed = 0
        else:
            traversed += 1
        
        # add the pump back to the queue
        route.put(pump)
    
    # return the pump index
    return start