import streamlit as st

st.title("📚 Библиотека")

# Инициализация на списъка с книги
if "books" not in st.session_state:
    st.session_state.books = []

# --- СЕКЦИЯ: ДОБАВЯНЕ ---
st.header("➕ Добави книга")
title = st.text_input("Заглавие")
author = st.text_input("Автор")
# Поправка: тук беше записано в променлива author, а трябва да е price
price = st.number_input("Цена", min_value=0.0)

if st.button("Добави книгата"):
    if title and author:  # Проверка дали не са празни
        book = {
            "title": title,
            "author": author,
            "price": price
        }
        st.session_state.books.append(book)
        st.success(f"Книгата '{title}' е добавена!")
    else:
        st.error("Моля, попълни заглавие и автор.")

st.divider()

# --- СЕКЦИЯ: ПОКАЗВАНЕ ---
if st.button("Покажи всички книги"):
    if not st.session_state.books:
        st.write("Няма добавени книги.")
    else:
        for book in st.session_state.books:
            st.write(f"**Заглавие:** {book['title']}")
            st.write(f"**Автор:** {book['author']}")
            st.write(f"**Цена:** {book['price']:.2f} лв.")
            st.write("---")

# --- СЕКЦИЯ: ТЪРСЕНЕ ---
st.header("🔍 Търсене по автор")
search_author = st.text_input("Въведи име на автор")

if st.button("Търси по автор"):
    if search_author:
        found_books = [b for b in st.session_state.books if search_author.lower() in b["author"].lower()]
        
        if found_books:
            for b in found_books:
                st.json(b) # По-прегледно показване на обекта
        else:
            st.warning("Няма намерени книги от този автор.")
    else:
        st.info("Въведи име за търсене.")
