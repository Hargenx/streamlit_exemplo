import streamlit as st

def page1():
    st.title('Página 1')
    st.write('Conteúdo da página 1')

def page2():
    st.title('Página 2')
    st.write('Conteúdo da página 2')

def main():
    st.set_page_config(
        page_title="Exemplo de Múltiplas Páginas",
        page_icon="🔥",
        layout="wide"
    )

    pages = {
        "Página 1": page1,
        "Página 2": page2
    }

    selection = st.sidebar.radio("Navegar", list(pages.keys()))

    page = pages[selection]
    page()

if __name__ == "__main__":
    main()
