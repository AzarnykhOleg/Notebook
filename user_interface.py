import Note


def create_note(number):
    """
    TODO
    :param number:
    :return:
    """
    title = check_len_text_input(
        input('Введите Название заметки: '), number)
    body = check_len_text_input(
        input('Введите Тело заметки: '), number)
    return Note.Note(title=title, body=body)


def menu():
    """
    TODO
    :return:
    """
    print("\nЭто программа 'Заметки'. Имеются следующие функции:"
          "\n\n1 - показать все заметки"
          "\n2 - добавить новую заметку"
          "\n3 - удалить заметку"
          "\n4 - редактировать заметку"
          "\n5 - найти заметки по дате"
          "\n6 - показать заметку по id"
          "\n7 - выход"
          "\n\nВыбирете пункт меню: ")


def check_len_text_input(text, n):
    """
    TODO
    :param text:
    :param n:
    :return:
    """
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text


def buy():
    """
    TODO
    :return:
    """
    print("Приходите к нам еще =). До новых встреч!")
