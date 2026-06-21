"""
app.py

Main Streamlit Application.
"""

import streamlit as st

from frontend.utils.session_manager import (
    SessionManager
)

from frontend.components.sidebar import (
    render_sidebar
)

from frontend.components.repository_status import (
    render_repository_status
)

from frontend.pages.upload_repository import (
    render_upload_page
)

from frontend.pages.chat_page import (
    render_chat_page
)


st.set_page_config(
    page_title="GitHub Repo RAG Assistant",
    page_icon="🤖",
    layout="wide"
)


def main():

    st.title(
        "GitHub Repository RAG Assistant"
    )

    backend = (
        SessionManager
        .get_backend()
    )

    sidebar_actions = (
        render_sidebar()
    )

    if sidebar_actions[
        "clear_chat"
    ]:

        backend.clear_chat()

        st.rerun()

    if sidebar_actions[
        "clear_repo"
    ]:

        backend.clear_repository()

        st.rerun()

    repository_name = (
        backend.get_repository_name()
    )

    render_repository_status(
        repository_name
    )

    tab1, tab2 = st.tabs(
        [
            "Upload Repository",
            "Chat"
        ]
    )

    with tab1:

        render_upload_page(
            backend
        )

    with tab2:

        render_chat_page(
            backend
        )


if __name__ == "__main__":

    main()