<a id="return"></a>

<center>

# Промежуточная аттестация

## Урок 1. Приложение заметки (Python)

</center>

---

**Реализовать консольное приложение заметки, с сохранением, чтением, добавлением, редактированием и удалением заметок.**

**Заметка должна содержать идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения заметки.**

Сохранение заметок необходимо сделать в формате json или csv формат (разделение полей рекомендуется делать через точку с запятой). Реализацию пользовательского интерфейса студент может делать как ему удобнее, можно делать как параметры запуска программы (команда, данные), можно делать как запрос команды с консоли и последующим вводом данных, как-то ещё, на усмотрение студента.

---

**Главное меню приложения для ведения заметок:**

Функция open_main_menu() в модуле view.py выводит главное меню, в котором два варианта выбора для пользователя.

Функция get_user_choice() в модуле view.py обрабатывает введенные пользователем данные и возвращает результат выбора пользователя. Также проверяется правильность ввода данных пользователем. Должно быть число, которое не должно быть больше или меньше количества пунктов меню и это должно быть именно число без слишних символов.

Функция handle_main_menu_choice() в модуле model.py принимает данные, которые выбрал пользователь и выполняет одно из двух действий - выход из приложения или продолжение работы и переход в основное меню.

Функция main() в модуле controller.py управляет потоком приложения.

А именно:

- view.open_main_menu() для отображения главного меню;

- view.get_user_choice() для получения выбора пользователя;

- model.handle_main_menu_choice() для обработки выбора.

В консоли это выглядит следующим образом:

**- Главное меню приложения:**

<img src="images\main_menu(1).jpg" height="181" width="907"/>

**- Выход:**

<img src="images\main_menu(2).jpg" height="208" width="911"/>

**- Ошибки при вводе числа:**

<img src="images\main_menu(3).jpg" height="312" width="903"/>

При выборе пункта меню 1 идет следующий шаг - **Открытие основного меню**

---

**Основное меню приложения для ведения заметок:**

Функция display_notes_menu в модуле view.py выводит список основного меню приложения, в котором несколько вариантов выбора для пользователя (посмотреть все заметки, добавить заметк, редактировать заметку, удалить заметку, сделать выборку заметок по дате добавления, выход).

Функция user_choice_menu_item в модуле view.py предлагает пользователю выбрать пункт меню и возвращает результат выбора пользователя. Также проверяется правильность ввода данных пользователем. Должно быть число, которое не должно быть больше или меньше количества пунктов меню и это должно быть именно число без слишних символов.

Функция main() в модуле controller.py управляет потоком приложения.

А именно:

- view.display_notes_menu() для отображения главного меню;

- view.user_choice_menu_item() для получения выбора пользователя;

- selecting_note_menu_item принимает запрос пользователя и дальше идет обработка запроса пользователя.

В консоли это выглядит следующим образом:

**- Основное меню приложения:**

<img src="images\notes_menu(1).jpg" height="241" width="917"/>

**- Выход:**

<img src="images\notes_menu(2).jpg" height="242" width="943"/>

**- Ошибки при вводе числа:**

<img src="images\notes_menu(3).jpg" height="416" width="954"/>

Обработка каждого пункта меню описано ниже

---

:point_right: [Вначало](#return "Вернуться вначало")
