p, q, r = map(int, input().split(' '))
lista = [p, q, r]
times = []
times.append(p+q)
times.append(p+r)
times.append(q+r)
times = sorted(times)
print(times[0])
