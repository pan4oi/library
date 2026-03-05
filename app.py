import streamlit as st

st.title("📚 Библиотека (Евро зона)")

# Инициализация на базата данни
if "books" not in st.session_state:
    st.session_state.books = []

# --- СЕКЦИЯ: ВЪВЕЖДАНЕ ---
st.header("➕ Добави нова книга")
col1, col2, col3 = st.columns([2, 2, 1])
with col1:
    new_title = st.text_input("Заглавие")
with col2:
    new_author = st.text_input("Автор")
with col3:
    new_price = st.number_input("Цена (€)", min_value=0.0, step=0.01, format="%.2f")

if st.button("Добави в базата"):
    if new_title and new_author:
        st.session_state.books.append({
            "title": new_title,
            "author": new_author,
            "price": new_price
        })
        st.success(f"Книгата е добавена успешно!")
    else:
        st.error("Попълни заглавие и автор!")

st.divider()

# --- СЕКЦИЯ: ТЪРСЕНЕ ---
st.header("🔍 Филтриране")

c1, c2, c3 = st.columns(3)
with c1:
    search_t = st.text_input("Търси заглавие", key="s_t")
with c2:
    search_a = st.text_input("Търси автор", key="s_a")
with c3:
    max_p = st.number_input("Макс. цена (€)", min_value=0.0, value=500.0)

sort_order = st.radio("Сортирай по цена:", ["Без сортиране", "Най-евтини първо", "Най-скъпи първо"], horizontal=True)

if st.button("Приложи филтрите"):
    # Филтриране по трите критерия
    results = [
        b for b in st.session_state.books 
        if search_t.lower() in b["title"].lower() 
        and search_a.lower() in b["author"].lower()
        and b["price"] <= max_p
    ]
    
    # Сортиране
    if sort_order == "Най-евтини първо":
        results = sorted(results, key=lambda x: x["price"])
    elif sort_order == "Най-скъпи първо":
        results = sorted(results, key=lambda x: x["price"], reverse=True)

    if results:
        st.subheader(f"Намерени: {len(results)}")
        for b in results:
            st.info(f"📖 **{b['title']}** | ✍️ {b['author']} | 💶 **{b['price']:.2f} €**")
    else:
        st.warning("Няма намерени книги по тези критерии.")

# Показване на всичко
if st.checkbox("Покажи инвентар (Таблица)"):
    st.dataframe(st.session_state.books, use_container_width=True)
