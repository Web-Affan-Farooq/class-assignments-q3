import streamlit as st

books = [
{
    "Title" :"example title_1",
    "Author":"Example author_1",
    "Publication":"example publication_1",
    "Genre":"Example genre_1",
    "Read status":True
},{
    "Title" :"example title_2",
    "Author":"Example author_2",
    "Publication":"example publication_2",
    "Genre":"Example genre_2",
    "Read status":True
},{
    "Title" :"example title_3",
    "Author":"Example author_3",
    "Publication":"example publication_3",
    "Genre":"Example genre_3",
    "Read status":False
}
]
newBook = {
    "Title" :"example title_4",
    "Author":"Example author_4",
    "Publication":"example publication_4",
    "Genre":"Example genre_4",
    "Read status":True
}

st.markdown("""<style>
            
            </style>""", unsafe_allow_html=True)
st.title("Personal library management system")
# books.append(newBook)

# books.remove({
#     "Title" :"example title_3",
#     "Author":"Example author_3",
#     "Publication":"example publication_3",
#     "Genre":"Example genre_3",
#     "Read status":True
# })

# requiredBook = {}
# for book in books: 
#     if(book["Title"] == "example title_5"):
#         requiredBook = book
name = st.text_input("Search book")
st.subheader("All :")

def deleteBook(book_name):
    newBooks = [book for book in books if book["Title"] != book_name]
    for book in newBooks :
        print(book)


for book in books:
    read_status= ""
    if(book["Read status"]): 
        read_status = "Readed"
    else : read_status = "Remaining"
    col_1, col_2, col_3 = st.columns([3,1,1])
    col_1 = st.markdown(f"""<div style="display:flex; flex-direction:row;">
                        <span>{book["Title"]}</span>
                        <span style="color:{"red" if read_status=="Readed" else "green"};">{read_status}</span>
                        </div>""",unsafe_allow_html=True)
    col_2 = st.write(book["Genre"])
    col_3 = st.button("Delete", key=book["Genre"], on_click=lambda: deleteBook(book["Title"]))


    # st.markdown(f"""<div style="display:flex; flex-dir+ection:row; flex-wrap:nowrap; justify-content:space-between; align-items:center">
    #             <span>{book["Title"]}</span>
                # <span style="color:{"red" if read_status=="Readed" else "green"};">{read_status}</span>
    #             <button onClick={deleteBook(book["Title"])}>Click</button>
    #             </div> """, unsafe_allow_html=True)
# print(books)