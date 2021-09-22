data_pred = []
data_cars = []

M = int(input())
for i in range(M):
    data_pred.append(set(input()))

N = int(input())
for i in range(N):
    data_cars.append(input())

fit_data = [0] * len(data_cars)
for i in range(len(data_cars)):
    for j in range(len(data_pred)):
        if set(data_cars[i]).intersection(data_pred[j]) == data_pred[j]:
            fit_data[i] += 1

for i in range(len(fit_data)):
    if fit_data[i] == max(fit_data):
        print(data_cars[i])