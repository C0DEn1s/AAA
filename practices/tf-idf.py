import math
from typing import List
from HW3.CountVectorizer import CountVectorizer


class TfIdfTransformer:
    def __init__(self):
        self._tf = []
        self._idf = []

    def _tf_transform(self, count_matrix: List[List[int]]) -> List[List[float]]:
        self._tf = []
        for vec in count_matrix:
            number_of_word = sum(vec)
            tf_matrix_row = [round(elem / number_of_word, 3) for elem in vec]
            self._tf.append(tf_matrix_row)

        return self._tf

    def _idf_transform(self, count_matrix: List[List[float]]) -> List[float]:
        self._idf = []
        total_docs = len(count_matrix)

        for ind, _ in enumerate(count_matrix[0]):
            docs_with_feature = 0
            for doc_counts in count_matrix:
                if doc_counts[ind] > 0:
                    docs_with_feature += 1
            self._idf.append(round(math.log((total_docs + 1) / (docs_with_feature + 1)) + 1, 1))
        return self._idf

    def fit_transform(self, matrix):
        self._tf_transform(matrix)
        self._idf_transform(matrix)

        result = []
        for text in self._tf:
            result.append([round(a * b, 3) for a, b in zip(text, self._idf)])

        return result


class TfIdfVectorizer(CountVectorizer):
    def __init__(self) -> None:
        super().__init__()
        self._tfidf_transformer = TfIdfTransformer()

    def fit_transform(self, corpus):
        count_matrix = super().fit_transform(corpus)
        return self._tfidf_transformer.fit_transform(count_matrix)


if __name__ == '__main__':
    cnt_matrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
    ]
    tf_idf = TfIdfTransformer()
    tf_matrix = tf_idf._tf_transform(cnt_matrix)
    expected_result = [
        [0.143, 0.143, 0.286, 0.143, 0.143, 0.143, 0, 0, 0, 0, 0, 0],
        [0, 0, 0.143, 0, 0, 0, 0.143, 0.143, 0.143, 0.143, 0.143, 0.143],
    ]

    for i in range(len(tf_matrix)):
        for j in range(len(tf_matrix[i])):
            assert abs(expected_result[i][j] - tf_matrix[i][j]) < 10e-10

    idf_matrix = tf_idf._idf_transform(cnt_matrix)
    assert idf_matrix == [1.4, 1.4, 1.0, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4]

    corp = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    transformer = TfIdfVectorizer()
    tfidf_matrix = transformer.fit_transform(corp)
    expected = [[0.2, 0.2, 0.286, 0.2, 0.2, 0.2, 0, 0, 0, 0, 0, 0],
                [0, 0, 0.143, 0, 0, 0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]]
    assert tfidf_matrix == expected
