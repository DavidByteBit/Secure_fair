from Compiler import mpc_math
from Compiler import ml
import sys


ALICE = 0
BOB = 1


def dot_product(a, b):
    assert (len(a) == len(b))

    res = sint(0)
    for i in range(len(a)):
        res += a[i] * b[i]

    return res


def load_model(param_size):

    model_coefs = Array(param_size - 1, sfix)

    @for_range_opt(param_size - 1)
    def _(i):
        model_coefs[i] = sfix.get_input_from(ALICE)
    bias = sfix.get_input_from(ALICE)

    return (model_coefs, bias)


def load_data(param_size, row_length):

    # Note that 'param_size - 1' should be the number of features of the dataset
    data = Matrix(row_length, param_size - 1, sfix)

    @for_range_opt(row_length)
    def _(i):
        @for_range_opt(param_size - 1)
        def _(j):
            data[i][j] = sfix.get_input_from(BOB)

    return data


def get_labels(row_length):
    labels = Array(row_length, sint)

    @for_range_opt(row_length)
    def _(i):
        labels[i] = sint.get_input_from(BOB)

    return labels


def infer_data(model, data, param_size, row_length):

    cmp_against = sfix(0.5)
    predicted_labels = Array(row_length, sint)

    @for_range_opt(row_length)
    def _(i):
        label_intermediate = dot_product(model[0], data[i]) + model[1]
        label = cmp_against >= label_intermediate
        predicted_labels[i] = label

    return predicted_labels


# 0: Number of Params, 1: Number of rows in data
#args = sys.argv[1:]

# i = 0
# while not args[i].__eq__('-'):
#     i += 1
#
# args = args[i + 1:]

# num_of_params = int(args[0])
# row_length = int(args[1])

num_of_params = 62
row_length = 1000

model = load_model(num_of_params)

data = load_data(num_of_params, row_length)

predicted_labels = infer_data(model, data, num_of_params, row_length)

actual_labels = get_labels(row_length)

TP = sint(0)
FP = sint(0)
TN = sint(0)
FN = sint(0)

for i in range(row_length):
    a = predicted_labels[i]
    b = actual_labels[i]

    x = (a == 1)
    y = (b == 1)
    z = 1 - a
    w = 1 - b

    TN += z * w
    FP += z * b
    FN += x * w
    TP += x * y

print("howdy!")
print_ln("howdy!")

print(str(TP.reveal()))
print_ln(str(TP.reveal_list()))


