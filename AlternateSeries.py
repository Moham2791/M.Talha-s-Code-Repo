
series = []

f_answer = 0
power = 0

for k in range(1, 1000000):

    power = k+1
    item = (-1)**power/(2 * k-1)

    series.append(item)
# print(series)
for i in range(len(series)):

    f_answer += series[i]

print(f_answer*4)
