class CountVectorizer:
    def __init__(self):
        self.unique_words = {}
        self.count_matrix = []

    def fit_transform(self, data):
        ind = 0
        for sentence in data:
            for word in sentence.lower().split():
                if word not in self.unique_words:
                    self.unique_words[word] = ind
                    ind += 1

        matrix = []
        num_of_words = len(self.unique_words)

        for ind, sentence in enumerate(data):
            cnt_line = [0] * num_of_words
            for word in sentence.lower().split():
                ind = self.unique_words[word]
                cnt_line[ind] += 1
            matrix.append(cnt_line)

        self.count_matrix = matrix
        return matrix

    def get_feature_names(self):
        return list(self.unique_words.keys())


corpus = [
 'Crock Pot Pasta Never boil pasta again',
 'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]
vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform(corpus)
print(vectorizer.get_feature_names())
for line in count_matrix:
    print(line)

