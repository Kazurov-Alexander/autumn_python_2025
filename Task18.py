#todo: Заданы множества
#Даны читатели книг
#readers_books = {'id3', 'id5', 'id9', 'id8', 'id2', 'id1' }

#Даны читатели газет
#readers_magazines = { 'id8', 'id2', 'id1', 'id4', 'id6', 'id7', 'id10'}

#Найти пользователей кто читает и книги и газеты

# Читатели книг
readers_books = {'id3', 'id5', 'id9', 'id8', 'id2', 'id1'}

# Читатели газет
readers_newspapers = {'id8', 'id2', 'id1', 'id4', 'id6', 'id7', 'id10'}

# Пересечение множеств — те, кто читают и книги, и газеты
readers_both = readers_books & readers_newspapers  # можно также использовать .intersection()

# Вывод результата
print("Пользователи, читающие и книги, и газеты:", readers_both)

# Комментарий для фиксации в новом коммите