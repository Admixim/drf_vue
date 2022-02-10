# drf_vue

Sanchez Garcia, [10.02.2022 12:09]
Идея
Создать блог 

Функционал
1.Размещать книги
2.Загружать фотографии книг
3.Указывать автора книг
4.Регистрироваться с учетными данными пользователей
5.Поиск по категориям, авторам, дате публикации, названию книги
6.Пользователь может загрузить описание, обложки, автор, категории, издатель
7.Подписка  на категори
8.



Архитектура БД

Author
name - char
country -char
discribe - text

publisher 
name -char
adress -char
email - email field
discribe - text 

category
name  char

image  book
book - Book, FK
name char
img - image 

Book
title- char
discribe - text
author - M2M - Author 
publisher - FK- publisher
file - file (*.pdf)
published_date - date 
page -  positivinteger
category - category - FK




Tools

  Django / DRF
  vue.js
