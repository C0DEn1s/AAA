class CountVectorizer:
    """
    Class, which counts number of words in given sentences
    """
    def __init__(self):
        self.unique_words = {}
        self.count_matrix = []

    def fit_transform(self, data: list) -> list:
        ind = 0
        for sentence in data:
            for word in sentence.lower().split():
                if word not in self.unique_words:
                    self.unique_words[word] = ind
                    ind += 1

        matrix = []
        num_of_words = len(self.unique_words)

        for sentence in data:
            cnt_line = [0] * num_of_words
            for word in sentence.lower().split():
                ind = self.unique_words[word]
                cnt_line[ind] += 1
            matrix.append(cnt_line)

        self.count_matrix = matrix
        return matrix

    def get_feature_names(self) -> list:
        return list(self.unique_words.keys())


if __name__ == '__main__':
    corpus = [
     'Crock Pot Pasta Never boil pasta again',
     'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    for line in count_matrix:
        print(line)

    true_feature_names = ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro', 'fresh', 'ingredients', 'parmesan', 'to', 'taste']
    true_matrix = [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]

    assert count_matrix == true_matrix
    assert vectorizer.get_feature_names() == true_feature_names
    assert CountVectorizer().get_feature_names() == []
    assert CountVectorizer().fit_transform([]) == []

