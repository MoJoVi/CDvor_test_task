"""
Построить инвертированный индекс по стихотворению "Чепушники" Сергея Михалкова:

На выходе индекс должен представлять из себя массив вида:
[
  {
    <слово>:
      [
        { <номер_строки>, <номер_позиции> },
        ...
      ]
  },
  ...
]
Язык программирования может быть любой. Как передавать входные данные, тоже не важно.
Вывод либо в консоль, либо в файл.

Бонусом - можно попробовать реализовать поиск слов по построенному индексу.
"""
from pprint import pprint


def words_indexing(text_file):
    """
    :param text_file: название/путь текстового файла
    :return: необходимый по условию массив.
    """
    words_dict = {}
    with open(text_file, 'r') as file:
        for line_ix, line in enumerate(file.readlines()):
            line = ''.join([letter for letter in line.lower() if letter not in '.,:;']).split()
            # В предыдущей строке кода мы убираем знаки препинания, и разбиваем строку
            # на отдельные слова. Я решил не трогать дефиз в словах "жили-были" т.к. это
            # является устойчивым выражением и если их записать как 2 слова то это будет
            # искажением значения.
            for word in line:
                words_dict[word] = words_dict.get(word, list()) + [(line_ix, line.index(word))]
    return [{words[0]: words[1]} for words in words_dict.items()]  # возвращаем массив необходимого формата


def find_word(word, array):
    """
    :param word: искомое слово
    :param array: массив заданного формата в котором необходимо найти слово
    :return: список кортежей формата [(<номер_строки>, <номер_позиции>)]
    """
    try:
        res = next(x[word] for x in array if x.get(word, False))
    except StopIteration:
        res = 'Слово не найдено!'
    return res


if __name__ == '__main__':
    array = words_indexing('text.txt')
    pprint(array)
    print(find_word('две', array))
    print(find_word('sdthxfg', array))
