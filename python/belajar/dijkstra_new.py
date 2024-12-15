class Edges:
    def __init__(self, ver, dist):
        self.distance = dist
        self.vertex = ver


def dijkstra(al, start, end):
    prev = {v: None for v in al.keys()}
    visit = {v: False for v in al.keys()}
    dist = {v: float("inf") for v in al.keys()}
    prioque = []
    dist[start] = 0
    prioque.append([0, start])
    while len(prioque) != 0:
        remdis = prioque[-1][0]
        removed = prioque[-1][1]
        prioque.pop()
        visit[removed] = True
        for edg in al[removed]:
            if visit[edg.vertex]:
                continue
            newdist = remdis + edg.distance
            if newdist < dist[edg.vertex]:
                dist[edg.vertex] = newdist
                prev[edg.vertex] = removed
                prioque.append([newdist, edg.vertex])
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
        print(i, end=" ")
    print(f"\n jarak antara {start} ke {end} adalah {jarak}")
    return


def main():
    al = {}
    total = int(input("masukan banyak titik atau vertex yang ada: "))
    for i in range(total):
        ver = input("masukan titiknya: ")
        cabang = int(input("masukan banyak cabang yang ada di titik tersebut: "))
        data = []
        for j in range(cabang):
            data.append(Edges(input("masukan vertex tujuan: "), int(input("masukan distance nya: "))))
        al[ver] = data
    start = input('start: ')
    end = input('End: ')
    dijkstra(al, start, end)


main()
