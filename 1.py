def find_max_min(a):  
    if not a:  
        return None, None  # 如果数组为空，返回None  
      
    maxe = mine = a[0]  
    for i in range(1, len(a)):  
        if a[i] > maxe:  
            maxe = a[i]  
        if a[i] < mine:  
            mine = a[i]  
    return maxe, mine  
  
# 示例  
a = [3, 1, 4, 1, 5, 9, 2, 6]  
maxe, mine = find_max_min(a)  
print(f"Max: {maxe}, Min: {mine}")
'''最好情况：数组已经是有序的（无论是升序还是降序）。
即使在这种情况下，算法仍然需要遍历整个数组来确认最大
值和最小值，因此时间复杂度为O(n)。
最坏情况：数组完全无序。算法仍然需要遍历整个数组来找
到最大值和最小值，因此时间复杂度仍然是O(n)。
平均情况：由于数组的无序程度对算法的行为（即
需要遍历整个数组）没有影响，平均时间复杂度也是O(n)。'''