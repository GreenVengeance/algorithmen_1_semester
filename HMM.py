import numpy as np

class State:
    def __init__(self, start, outside, inside, table):
        self.start = start
        self.outside = outside
        self.inside = inside
        self.table = table


def create_state(A, C, G, T):
    start = 0.5
    outside = 0.01
    inside = 0.99
    table = {"A": A, "C": C, "G": G, "T": T }
    state = State(start, outside, inside, table)
    return state


def calculate(genom, insel, A, x):
    # erste Spalte
    A[0][0] = genom.start
    A[1][0] = insel.start

    for i in range(1, (len(x)+1)):
        G_0 = A[0][i-1] * genom.inside * genom.table[x[(i-1)]]
        I_0 = A[0+1][i-1] * insel.outside * insel.table[x[(i-1)]]
        A[0][i] = max(G_0, I_0)

        G_1 = A[1-1][i-1] * genom.outside * genom.table[x[(i-1)]]
        I_1 = A[1][i-1] * insel.inside * insel.table[x[(i-1)]]
        A[1][i] = max(G_1, I_1)

    return A


def HMM_main():
    genom = create_state(A=0.4, C=0.1, G=0.1, T=0.4)
    insel = create_state(A=0.25, C=0.25, G=0.25, T=0.25)
    # print(genom.table["A"])
    x = input("Geben Sie eine Sequenz ein: ")
    x = list(x)
    A = matrix = np.zeros((2, (len(x)+1)), dtype=float)

    calculate(genom, insel, A, x)
    print(A)


if __name__ == "__main__":
    HMM_main()
