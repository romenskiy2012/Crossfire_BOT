Бот использует mariadb, в теории может роботать с MySQL, НО я не тестировал это!

Для запуска требуется создать 1 базу данных и 1 пользователя который будет иметь полный доступ к ней.

# mysql -p -u root
# CREATE USER 'Crossfire_bot'@'localhost' IDENTIFIED BY '';
# CREATE DATABASE Crossfire_P CHARACTER SET utf8 COLLATE utf8_general_ci;
# GRANT ALL PRIVILEGES ON Crossfire_P.* TO 'Crossfire_bot'@'localhost';
# FLUSH PRIVILEGES;
# exit

Бот опирается на таблицу "role", после первого запуска он создаст её сам, вам требуется создать новую строку для вашего сервера, и указать соотвецтвуюшие ID.
Если вам не требуется роль которая выдаётся новым пользователям "hi" просто оставьте это поле пустым (None) или впишите ноль (0).
Естественно скобки вписывать не нужно))))



Admin Discord bot.

RU:
    Функцианал:
        - Выдавать роль Warning от 1 - 3.
        - Выдавать роль Mut на определенное время (Время указывается в часах, если вам нужно выдать роль на 30мин можете прописать 0.5 и тд.).
        - Выдавать указанную роль при заходе пользователя.
        - ВОССТАНАВЛИВАЕТ РОЛИ ПРИ ПЕРЕЗАХОДЕ.
    Перпед запускам;
        - Читайте "README.md"
    Коментарий:
        - Требует MARIADB!
        - Пытался написать читаемый и красивый код, что бы его мог отредактировать под себя каждый.
        Некоторые методы подсчёта времени и проверки очень спорные, так что не бойтесь экспериментировать.

US:
    translate.google.com))))
