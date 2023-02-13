import csv
#Функция открытия всех заметок
def open_all_notes():
    with open('notes.csv', 'r', encoding='UTF-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(" - ".join(row).replace(";", " "))

#Функция добавления заметок
def adding_notes():
    pass

#Функция редактирования заметок
def editing_notes():
    pass

#Функция удаления заметок
def deleting_notes():
    pass

#Функция выборки заметок по дате добавления
def selection_of_notes_by_date():
    pass

#Функция обработки открытия основного меню
def handle_main_menu_choice(choice):
    if choice == 2:
        exit()
