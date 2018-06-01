import paths
import re

class Reader:

    def __init__(self):
        self.stop_words = []
        self.stop_word_n_grams = []
        self.open_stop_words()

    def open_stop_words(self, file_path=paths.stop_words):
        file = open(file_path)
        self.stop_words = [x.strip() for x in file.readlines()]

    def find_stop_word_n_grams(self, n):
        for i in range(1 + len(self.stop_words) - n):
            self.stop_word_n_grams.append('_'.join(self.stop_words[i:i + n]))

    def default_read_from_file(self, file_path):
        file = open(file_path)
        line = file.read().replace("'", "").lower()
        rgx = re.compile("(\w[\w']*\w|\w)")
        words = [x for x in rgx.findall(line) if x not in self.stop_words]
        return words

    def get_stop_words(self):
        return self.stop_words


