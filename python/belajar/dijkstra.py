al = {'A':{'B':False,'C':False,'D':False, 'E': False},
      'B':{'A':False,'C':False,'D':False},
      'C':{'A':False,'B':False,'D':False},
      'D':{'A':False,'B':False, 'C':False, 'E':False},
      'E':{'A':False,'D':False},
      }
def dijkstra(al, start, end):
    prev = {v: None for v in al.keys()}
    visit = {v: False for v in al.keys()}
    dist =  {v: False for v in al.keys()}
    prioque = []
    dist[start] = 0
    prioque.append([0, start])
    while len(prioque) != 0:
        remdis = prioque[-1][0]
        removed = prioque[-1][1]
        prioque.pop()
        visit[removed] = True
        for edg in al[removed]:
            if visit[edg]:
                continue
            newdist = remdis + al[removed][edg]
            if newdist < dist[edg]:
                dist[edg] = newdist
                prev[edg] = removed
                prioque.append([newdist, edg])
        prioque.sort()
        prioque.reverse()
    path = []
    current = end
    jarak = dist[end]
    while current is not None:
        path.append(current)
        current = prev[current]
        if current is not None:
            path.append('=>')
    path.reverse()
    for i in path:
        print(i, end="")
    print(f"\n jarak antara {start} ke {end} adalah {jarak}")
    return
start = input('start: ')
end = input('End: ')
dijkstra(al, start, end)