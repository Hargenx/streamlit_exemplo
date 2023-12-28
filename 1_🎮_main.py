import streamlit as st


def desativa_input():
    st.session_state.disabled = True


def main():
    st.set_page_config(
        page_title="Exemplo Multipáginas",
        page_icon="🔥",
    )

    st.title("Página Principal")
    st.sidebar.success("Weeeee.🔥")

    st.subheader("Página 1")
    st.write("Página 1")

    if "disabled" not in st.session_state:
        st.session_state.disabled = False

    if "input_nome" not in st.session_state:
        st.session_state.input_nome = ""

    with st.form("my_form"):
        input_nome = st.text_input("Digite o seu nome:", disabled=st.session_state.disabled, key="nome")
        botao_submit = st.form_submit_button("Enviar Nome", on_click=desativa_input, disabled=st.session_state.disabled)

        if botao_submit:
            st.session_state.input_nome = input_nome
            st.info("Você entrou com: " + st.session_state.input_nome)

    if "my_input" not in st.session_state:
        st.session_state["my_input"] = ""

    entrada_persistente = st.text_input("Exemplo do seu texto que ficará em todas as páginas", st.session_state["my_input"])
    send_button = st.button("Enviar")

    if send_button:
        st.session_state["my_input"] = entrada_persistente


    st.write("Você entrou com: ", st.session_state.input_nome)
    st.write("Você digitou: ", st.session_state["my_input"])


if __name__ == "__main__":
    main()
