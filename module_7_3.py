import io
from pprint import pprint


class WordsFinder:

    def __init__(self, *files):
        self.file_names = list(files)

    def get_all_words(self):
        all_words = {'file1.txt', 'file2.txt', 'file3.txt'}

            for file_name in self.file_names:

            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
                    for punct in punctuation:
                        line = line.replace(punct, ' ')
                    all_words[file_name] = words
            return all_words
    #
    # def find(self, word):
    #     places = self.get_all_words()
    #     for name, words in places:
    #         if word.lower() in words:
    #             places[name] = words.index(word.lower()) + 1
    #     return places
    #
    # def count(self, word):
    #     counters = {}
    #
    #     for name, words in get_all_words().items():
    #         words_count = name.count(word.lower())
    #         counters[words] = words_count
    #     return counters


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
# print(finder2.find('TEXT')) # 3 слово по счёту
# print(finder2.count('teXT')) # 4 слова teXT в тексте всего

