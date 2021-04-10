


def neuronne(inputs, weigths, activation_func):
    return activation_func(
        sum(
            z[0] * z[1] for z in zip([1.0] + inputs, weigths)
        )
    )

def step(x):
    return 1 if x > 0 else 0

weigths = [-0.25, 1, -0.45]

glenmorangie = [-0.21, 0.18]
talisker = [0.6, -0.31]

print("Glenmorangie", neuronne(glenmorangie, weigths, step))
print("Talisker", neuronne(talisker, weigths, step))


