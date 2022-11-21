class Item:
    def __init__(self, v, w):
        self.value = v
        self.weight = w
        
    
def fractional_knapsack(W : int, arr : list()):
    #pass
    arr.sort(key = lambda x: (x.value / x.weight), reverse = True)
    ans = 0
    for i in range(len(arr)):
        cur = arr[i]
        
        if cur.weight <= W:
            ans += cur.value
            W -= cur.weight
            continue
        
        # we came here because cur.weight > remaining W
        # what fraction can i add?
        # ez
        fraction = W / cur.weight
        ans += cur.value * fraction
        W -= cur.weight * fraction
        break
    
    return ans

if __name__ == "__main__":
    W = 50
    
    arr = [Item(70, 10), Item(100, 20), Item(120, 30)]
    ans = fractional_knapsack(W, arr)
    print(ans)
    
    
    

    
            
        
    
    
