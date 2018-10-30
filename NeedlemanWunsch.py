import numpy as np

gap_score = -1
match_score = 1
mis_match_score = -1


def match(left, up, diagonal):
    left += gap_score
    up += gap_score
    diagonal += match_score
    best_score = (max(left, up, diagonal))

    return best_score


def mis_match(left, up, diagonal):
    left += gap_score
    up += gap_score
    diagonal += mis_match_score
    best_score = (max(left, up, diagonal))

    return best_score


def build_matrix(seq1, seq2):
    alignment_matrix = np.arange((len(seq2)) * (len(seq1))).reshape(len(seq2), len(seq1))

    for i in range(0, len(seq1)):
        alignment_matrix[0][i] = i * gap_score
        for j in range(0, len(seq2)):
            alignment_matrix[j][0] = j * gap_score

    return alignment_matrix


def nw_alignment():
    seq1 = input("Geben sie die erste Sequenz ein: ")
    seq2 = input("Geben sie die zweite Sequenz ein: ")
    seq1 = list("-" + seq1)
    seq2 = list("-" + seq2)
    print("Sequenz 1: " + seq1.__str__())
    print("Sequenz 2: " + seq2.__str__())

    A = build_matrix(seq1, seq2)
    for i in range(1, len(seq1)):
        for j in range(1, len(seq2)):
            if seq1[i] == seq2[j]:
                best_score = match(left=A[j][i - 1], up=A[j - 1][i],
                                   diagonal=A[j - 1][i - 1])
                A[j][i] = best_score
            else:
                best_score = mis_match(left=A[j][i - 1], up=A[j - 1][i],
                                       diagonal=A[j - 1][i - 1])
                A[j][i] = best_score

    print(A)
    print("Editierdistanz:", A[len(seq2) - 1][len(seq1) - 1])


if __name__ == "__main__":
    print("Gap Score:", gap_score)
    print("Match Sore:", match_score)
    print("Mismatch Score:", mis_match_score)
    nw_alignment()

    for i in range(3):
        yes = input("Möchten Sie ein weiteres Alignment ausrechnen --> yes(y) no(n): ")
        if yes == "y":
            nw_alignment()
        else:
            break
