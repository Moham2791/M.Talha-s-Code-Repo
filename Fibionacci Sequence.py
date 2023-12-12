L = [1, 1]


for i in range((len(L))+98):
    if len(L) < 100:
        c = L[i]+L[i+1]

        L.append(c)
    else:
        break

print(L)
