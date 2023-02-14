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

### **Главное меню приложения для ведения заметок:**

Функция open_main_menu() в модуле view.py выводит главное меню, в котором два варианта выбора для пользователя.

Функция get_user_choice() в модуле view.py обрабатывает введенные пользователем данные и возвращает результат выбора пользователя. Также проверяется правильность ввода данных пользователем. Должно быть число, которое не должно быть больше или меньше количества пунктов меню и это должно быть именно число без слишних символов.

Функция handle_main_menu_choice() в модуле model.py принимает данные, которые выбрал пользователь и выполняет одно из двух действий - выход из приложения или продолжение работы и переход в основное меню.

Функция main() в модуле controller.py управляет потоком приложения.

А именно:

- view.open_main_menu() для отображения главного меню;

- view.get_user_choice() для получения выбора пользователя;

- model.handle_main_menu_choice() для обработки выбора.

В консоли это выглядит следующим образом:

#### **Главное меню приложения:**

<img src="images\main_menu(1).jpg" height="181" width="907"/>

#### **Выход:**

<img src="images\main_menu(2).jpg" height="208" width="911"/>

#### **Ошибки при вводе числа:**

<img src="images\main_menu(3).jpg" height="312" width="903"/>

При выборе пункта меню 1 идет следующий шаг - **Открытие основного меню**

---

:point_right: [Вначало](#return "Вернуться вначало")

---

### **Основное меню приложения для ведения заметок:**

Функция display_notes_menu в модуле view.py выводит список основного меню приложения, в котором несколько вариантов выбора для пользователя (посмотреть все заметки, добавить заметк, редактировать заметку, удалить заметку, сделать выборку заметок по дате добавления, выход).

Функция user_choice_menu_item в модуле view.py предлагает пользователю выбрать пункт меню и возвращает результат выбора пользователя. Также проверяется правильность ввода данных пользователем. Должно быть число, которое не должно быть больше или меньше количества пунктов меню и это должно быть именно число без слишних символов.

Функция main() в модуле controller.py управляет потоком приложения.

А именно:

- view.display_notes_menu() для отображения главного меню;

- view.user_choice_menu_item() для получения выбора пользователя;

- selecting_note_menu_item принимает запрос пользователя и дальше идет обработка запроса пользователя.

В консоли это выглядит следующим образом:

#### **Основное меню приложения:**

<img src="images\notes_menu(1).jpg" height="241" width="917"/>

#### **Выход:**

<img src="images\notes_menu(2).jpg" height="242" width="943"/>

#### **Ошибки при вводе числа:**

<img src="images\notes_menu(3).jpg" height="416" width="954"/>

Обработка каждого пункта меню описано ниже

---

:point_right: [Вначало](#return "Вернуться вначало")

---

### **Посмотр всех заметок:**

Функция notes_list в модуле view.py - выводит просто сообщение, что перед нами список всех заметок.

Функция open_all_notes в model.py - считывает CSV-файл "notes.csv", анализирует, что находится в этом файле и создает список заметок. Извлекаются заголовок(title), описание заметки(body), дата/время создания(creation_time), дата/время изменения(change_time), также проверяются любые исключения IndexError, которые могут возникнуть при извлечении данных из строки CSV-файла, например, когда в строке меньше столбцов, чем ожидалось. Если обнаруживается ошибка, то добавляется пустой список, который содержит пять пустых строк, к списку заметок. В итоге список заметок всегда будет содержать одинаковое количество столбцов, независимо от того, есть ли какие-либо пропущенные значения в какой-либо из строк.

tabulate используется для печати содержимого файла notes.csv в виде форматированной таблицы с заголовками столбцов. headers - список строк, который используется для указания заголовков столбцов. tablefmt - задает стиль таблицы. stralign - указывает как необходимо выровнять текст внутри ячеек.

Функция selecting_note_menu_item принимает входной параметр choice. Далее начинается цикл, который будет продолжаться пока пользователь не нажмет на выход.

Первая проверка choice == 1. Если пользователь выбрал первый пункт в основном меню, то вызывается функция notes_list из модуля view.py (view.notes_list()), которая печатает сообщение "Список всех заметок:". Далее вызывается функция open_all_notes из модуля model (model.open_all_notes()) для чтения файла notes.csv, извлечения информации из файла и отображения информации в виде таблицы.

#### **Результат вывода всех заметок:**

<img src="images\open_all_notes.jpg" height="344" width="974"/>

---

:point_right: [Вначало](#return "Вернуться вначало")

---

### **Добавление заметок:**

Функция adding_notes в модуле view.py - просит пользователя заполнить необходимые поля (заголовок и описание заметки) и считывает введенные пользователем данные. Возвращает кортеж значений (return header, description).

Функция get_next_id в модуле model.py считывает CSV-файл notes.csv с помощью csv.reader, извлекает id каждой заметки из первого столбца CSV-файла. Возвращает максимальный id плюс один, если есть записи в файле, если записей нет, то возвращает 1.

Функция adding_notes в модуле model.py принимает два аргумента (title, body), вызывает функцию get_next_id для получения следующего доступного id. Также, используя функцию time.strftime, получаем текущую дату и время. Затем открывается файл notes.csv для добавления записи с помощью функции open, записывается новая строка с помощью csv.writer. Строка будет содержать id, заголовок, описание заметки, дату/время создания заметки. В данном случае последний столбец таблицы останется пустым, т.к. реализуется только добавление.

Функция selecting_note_menu_item принимает входной параметр choice. Описание смотри в пункте "Посмотр всех заметок:".

Вторая проверка choice == 2. Вызывается функция adding_notes из модуля view.py (title, body = view.adding_notes()) для получения от пользователя введеных значений. Далее полученные значения от пользователя передаются в качестве аргумента функции adding_notes модуля model.py ( model.adding_notes(title, body)) для добавления заметки в файл notes.csv.
Для наглядного отображения, что запись добавилась, используется функция open_all_notes модуля model.py (model.open_all_notes())

#### **Результат добавления заметки:**

<img src="images\adding_notes.jpg" height="619" width="915"/>

---

:point_right: [Вначало](#return "Вернуться вначало")

---

### **Редактирование заметки:**

Функция edit_note в модуле view.py - просит пользователя ввести id заметки для редактирования, далее просит изменить заголовок заметки и описание заметки. Возвращает кортеж (return id, title, body). Изначально выводится сообщение "Редактировать заметку". Просит пользователя ввести id заметки, проверяет на правильность ввода, если ввод не правильный, а именно, id отсутствует в списке заметок, т.е. идет проверка списка всех заметок, то выводится сообщение "Неверный ID. Такая заметка отсутствует в списке!!!". Также проверяется пользователь ввел число или нет, если пользователь ввел не число, то выводится сообщение "Неверный ввод. Пожалуйста, введите число!!!". Если id найден, то пользователя просят ввести данные в поля "Заголовок" и "Описание Заметки".

Функция editing_notes в модуле model.py открывает файл notes.csv в режиме чтения, считывает данные и обновляет заметку с указаным id, изменяя поля title и body. Если какое-то из полей не изменялось, то значение, которое было в этом поле до редактирования остается не изменным. Также обновляется поле "Дата/время изменения заметки" текущим временем с помощью функции time.ctime(). Далее открывает файл notes.csv в режиме записи, записывает отредактированную заметку.

Функция selecting_note_menu_item принимает входной параметр choice. Описание смотри в пункте "Посмотр всех заметок:".

Вторая проверка choice == 2. Открывается файл notes.csv и передает его функции edit_note() модуля view.py (result = view.edit_note(file)) в качестве аргумента. Если возвращаемый результат edit_note() модуля view.py не равен None, то значения id, title и body распаковываются в отдельные переменные (id, title, body = result). Далее вызывается функция editing_notes() модуля model.py (model.editing_notes(id, title, body)), передаваются переменные id, title и body. И в конце для наглядного отображения, что запись изменилась, используется функция open_all_notes модуля model.py (model.open_all_notes())

#### **Результат изменения заметки:**

<img src="images\edit_note(2).jpg" height="711" width="945"/>

#### **Ошибки при вводе числа при выборе id:**

<img src="images\edit_note(1).jpg" height="781" width="907"/>

---

:point_right: [Вначало](#return "Вернуться вначало")

---

:point_right: [Вначало](#return "Вернуться вначало")
