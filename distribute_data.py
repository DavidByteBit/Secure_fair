import sys


# 0: Model Path, 1: Data Path

args = sys.argv[1:]

# TODO: Make dynamic
row_length = 1000

m_path = args[0]
d_path = args[1]
l_path = args[2]

model_params = []
data = [[] for i in range(row_length)]
labels = []

with open(m_path, 'r') as f:
    # Only one line
    for line in f:
        model_params = line.split(",")

with open(d_path, 'r') as f:
    index = 0
    for line in f:
        line = line.replace('\n', '').split(',')
        data[index] = line
        index += 1

with open(l_path, 'r') as f:
    for line in f:
        labels.append(line.replace('\n', ''))

P0 = "Player-Data/Input-P0-0"
P1 = "Player-Data/Input-P1-0"

with open(P0, 'w') as f:
    f.write(" ".join(model_params))
    print("Counted " + str(len(model_params)) + " parameters")

all_elements_data = 0
with open(P1, 'w') as f:
    for row in data:
        f.write(" ".join(row) + " ")
        all_elements_data += len(row)
    print("Counted " + str(all_elements_data) + " total elements of data")

with open(P1, 'a+') as f:
    f.write(" ".join(labels))
    print("Counted " + str(len(labels)) + " labels")