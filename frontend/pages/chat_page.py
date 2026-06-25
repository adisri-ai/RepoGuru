import streamlit as st

from frontend.components.chat_message import (
    render_chat_message
)


def render_chat_page(
    backend
):

    st.markdown(
        """
        <h1 class="hero-title">
        RepoGuru
        </h1>

        <p class="hero-subtitle">
        AI-Powered GitHub Repository Assistant
        </p>
        """,
        unsafe_allow_html=True
    )

    repo_name = (
        backend.get_repository_name()
    )

    if repo_name:

        st.markdown(
            f"""
            <div class="repo-card">

            <h3>
            Repository Loaded
            </h3>

            <b>
            {repo_name}
            </b>

            <br><br>

            Ready for questions.

            </div>
            """,
            unsafe_allow_html=True
        )

    history = (
        backend.get_chat_history()
    )

    if not history:

        st.markdown(
            """
            <div class="glass-card">

            <h4>
            Suggested Questions
            </h4>

            • Explain the architecture

            • How does authentication work?

            • Which files contain business logic?

            • Explain the processing pipeline

            • Show repository dependencies

            </div>
            """,
            unsafe_allow_html=True
        )

    for message in history:

        render_chat_message(
            message["role"],
            message["content"]
        )

    prompt = st.chat_input(
        "Ask about the repository..."
    )

    if prompt:

        render_chat_message(
            "user",
            prompt
        )

        with st.status(
            "Analyzing repository..."
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