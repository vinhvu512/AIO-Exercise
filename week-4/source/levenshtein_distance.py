import streamlit as st


def initialize_distance_matrix(token1, token2):
    distances = [[0] * (len(token2) + 1) for _ in range(len(token1) + 1)]
    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1
    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2
    return distances


def compute_distance(distances, token1, token2):
    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if token1[t1 - 1] == token2[t2 - 1]:
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                distances[t1][t2] = min(
                    distances[t1][t2 - 1],
                    distances[t1 - 1][t2],
                    distances[t1 - 1][t2 - 1]
                ) + 1
    return distances


def levenshtein_distance(token1, token2):
    distances = initialize_distance_matrix(token1, token2)
    distances = compute_distance(distances, token1, token2)
    return distances[len(token1)][len(token2)]


def load_vocab(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    words = sorted(set(line.strip().lower() for line in lines))
    return words


vocabs = load_vocab(file_path='/Users/vinhvu/AIO-Exercise/week-4/source/data/vocab.txt')


def main():
    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input('Word:')

    if st.button("Compute"):
        leven_distances = {vocab: levenshtein_distance(word, vocab) for vocab in vocabs}
        sorted_distances = sorted(leven_distances.items(), key=lambda item: item[1])
        correct_word = sorted_distances[0][0]
        st.write('Correct word: ', correct_word)

        col1, col2 = st.columns(2)
        col1.write('Vocabulary:')
        col1.write(vocabs)

        col2.write('Distances:')
        col2.write(dict(sorted_distances))


if __name__ == "__main__":
    main()
