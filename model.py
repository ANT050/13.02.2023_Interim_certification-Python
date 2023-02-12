#Функция открытия всех заметок
def open_all_notes():
    pass

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

#Функция обработки запроса пользователя основного меню
def selecting_note_menu_item(choice):
    if choice == 1:
        open_all_notes()
    elif choice == 2:
        adding_notes()
    elif choice == 3:
        editing_notes()
    elif choice == 4:
        deleting_notes()
    elif choice == 5:
        selection_of_notes_by_date()
    elif choice == 6:
        exit()

