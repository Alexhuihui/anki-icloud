import time

import genanki


class Anki(object):
    def __init__(self):
        name = time.strftime("%Y-%m-%d", time.localtime()) + ' words'
        self.my_deck = genanki.Deck(int(time.time()), name)
        self.my_model = genanki.Model(
            1376484377,
            'Simple Model',
            fields=[
                {'name': 'Question'},
                {'name': 'Answer'},
            ],
            templates=[
                {
                    'name': 'Card 1',
                    'qfmt': '{{Question}}',
                    'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
                },
            ])

    def add_item(self, english_word, chinese_word):
        my_note = genanki.Note(
            model=self.my_model,
            fields=[english_word, chinese_word])
        self.my_deck.add_note(my_note)

    def generate_apkg_file(self):
        file_name = time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.apkg'
        genanki.Package(self.my_deck).write_to_file(file_name)
        return file_name


if __name__ == '__main__':
    anki = Anki()
    anki.add_item('', '')
    anki.generate_apkg_file()
