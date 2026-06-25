"""
chat_page.py
"""

import streamlit as st

from frontend.components.chat_message import (
    render_chat_message
)
from backend.main import BackendFacade

def render_chat_page(
    backend : BackendFacade
):

    st.header(
        "Repository Chat"
    )

    history = (
        backend.get_chat_history()
    )

    for message in history:

        render_chat_message(
            message["role"],
            message["content"]
        )

    prompt = st.chat_input(
        "Ask a question..."
    )

    if prompt:

        render_chat_message(
            "user",
            prompt
        )

        with st.spinner(
            "Thinking..."
        ):

            response = (
                backend.chat(
                    prompt
                )
            )

        render_chat_message(
            "assistant",
            response
        )

        st.rerun()