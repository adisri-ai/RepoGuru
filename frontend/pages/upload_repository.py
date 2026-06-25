"""
upload_repository.py
"""

import streamlit as st
from backend.main import BackendFacade
def render_upload_page(
    backend : BackendFacade
):

    st.header(
        "Repository Ingestion"
    )

    github_url = st.text_input(
        "GitHub Repository URL"
    )

    if st.button(
        "Load Repository"
    ):

        if not github_url:

            st.warning(
                "Enter a GitHub URL."
            )

            return

        with st.spinner(
            "Processing repository..."
        ):

            try:

                result = (
                    backend.ingest_repository(
                        github_url
                    )
                )

                st.success(result)

            except Exception as ex:

                st.error(
                    str(ex)
                )