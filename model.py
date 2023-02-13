from tabulate import tabulate
import csv
import time

# Функция открытия всех заметок


def open_all_notes():
    notes = []
    with open('notes.csv', 'r', encoding='UTF-8') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            try:
                title = row[1][:30] + '\n' + \
                    row[1][30:] if len(row[1]) > 30 else row[1]
                body = row[2][:30] + '\n' + \
                    row[2][30:] if len(row[2]) > 30 else row[2]
                creation_time = row[3] if row[3] else ''
                change_time = row[4] if row[4] else ''
                notes.append([row[0], title, body, creation_time, change_time])
            except IndexError:
                notes.append(['', '', '', '', ''])
    print(tabulate(notes, headers=['\033[91mID\033[0m', '\033[91mЗаголовок\033[0m', '\033[91mОписание заметки\033[0m',
          '\033[91mДата/время создания\033[0m', '\033[91mДата/время изменения\033[0m'], tablefmt="fancy_grid", stralign="center"))


# Функция добавления заметок
def adding_notes():
    pass

# Функция редактирования заметок


def editing_notes():
    pass

# Функция удаления заметок


def deleting_notes():
    pass

# Функция выборки заметок по дате добавления


def selection_of_notes_by_date():
    pass

# Функция обработки открытия основного меню


def handle_main_menu_choice(choice):
    if choice == 2:
        print("--"*55 + "\n" +
              "\033[35mВы завершили работу в приложении!!!\033[0m")
        exit()
