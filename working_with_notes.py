import working_with_files as wf
import Note
import user_interface as ui

number = 3


def add():
    """
    TODO
    :return:
    """
    note = ui.create_note(number)
    array = wf.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    wf.write_file(array, 'a')
    print('Заметка добавлена...')


def show(text):
    """
    TODO
    :param text:
    :return:
    """
    logic = True
    array = wf.read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(Note.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + Note.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in Note.Note.get_date(notes):
                print(Note.Note.map_note(notes))
    if logic:
        print('Нет ни одной заметки...')


def id_edit_del_show(text):
    """
    TODO
    :param text:
    :return:
    """
    id = input('Введите id необходимой заметки: ')
    array = wf.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = ui.create_note(number)
                Note.Note.set_title(notes, note.get_title())
                Note.Note.set_body(notes, note.get_body())
                Note.Note.set_date(notes)
                print('Заметка изменена...')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена...')
            if text == 'show':
                print(Note.Note.map_note(notes))
    if logic:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    wf.write_file(array, 'a')
