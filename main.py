import os

from word import Word


def read_data():
    with open('query_word.txt', "r", encoding="utf-8") as f:
        lines = f.readlines()
    num = 1
    odd_lines = []
    even_lines = []
    for line in lines:
        if (num % 2) == 0:
            even_lines.append(line.strip())
        else:
            odd_lines.append(line.strip())
        num += 1

    assert len(odd_lines) == len(even_lines), '数据文件格式不对'

    data_list = []
    for index in range(len(odd_lines)):
        data_list.append(Word(odd_lines[index], even_lines[index]))

    return data_list


def generate_apkg_file(data_list):
    from anki import Anki
    anki = Anki()
    for i in data_list:
        anki.add_item(i.english_word, i.chinese_word)
    return anki.generate_apkg_file()


def upload_apkg_file(file_path):
    from icloud import Cloud
    user = Cloud()
    user.upload_file(file_path)


def clear_file(path):
    if os.path.exists(path):
        os.remove(path)


def main():
    # 读取数据
    data_list = read_data()
    # 生成apkg文件
    file_path = generate_apkg_file(data_list)
    # 上传apkg文件到iCloud
    upload_apkg_file(file_path)
    # 清理文件
    clear_file(file_path)


if __name__ == '__main__':
    main()
