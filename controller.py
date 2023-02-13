import view
import model

def main():
    #Открытие главного меню, выбор пункта меню
    view.open_main_menu()
    main_menu_choice = view.get_user_choice()
    model.handle_main_menu_choice(main_menu_choice)

    #Открытие основного меню пользователю, выбор пункта меня
    view.display_notes_menu()
    notes_menu_choice = view.user_choice_menu_item()
    selecting_note_menu_item(notes_menu_choice)
  
#Функция обработки запроса пользователя основного меню 
def selecting_note_menu_item(choice):
    while True:
        if choice == 1: 
            view.notes_list()
            model.open_all_notes()
        elif choice == 6:
          view.application_closing()
          break
        view.display_notes_menu()
        choice = view.user_choice_menu_item()
    
    

