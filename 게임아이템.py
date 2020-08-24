import heapq
def solution(healths, items):    
    sort_items=sorted(items,key=lambda item: item[1])  #체력을 기준으로 오름차순 정렬
    heapq.heapify(healths) #healths를 sort로 정렬해도 시간 초과
    answer=[] 
    
    while healths:  #사람이 없을 때 까지 반복
        health = heapq.heappop(healths)
        equips = []
        for i in range(len(sort_items)):  
            if health - sort_items[i][1] < 100:
                break
            else:
                heapq.heappush(equips,(-sort_items[i][0],sort_items[i]))
        
        if equips:
            equip = heapq.heappop(equips)
            answer.append(items.index(equip[1])+1)
            sort_items.remove(equip[1])
            #sort_items.pop(sort_items.index(equip[1]))
            
    return sorted(answer)
