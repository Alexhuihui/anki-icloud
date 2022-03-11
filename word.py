class Word(object):
    def __init__(self, english_word, chinese_word):
        self.english_word = english_word
        self.chinese_word = chinese_word

    def __str__(self):
        return '<' + self.english_word + ', ' + self.chinese_word + '>'
