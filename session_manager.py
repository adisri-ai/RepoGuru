"""
session_manager.py

Maintains BackendFacade
inside Streamlit session state.
"""

import streamlit as st

from backend.main import BackendFacade


class SessionManager:

    BACKEND_KEY = "backend_facade"

    @staticmethod
    def get_backend():

        if (
            SessionManager.BACKEND_KEY
            not in st.session_state
        ):

            st.session_state[
                SessionManager.BACKEND_KEY
            ] = BackendFacade()

        return st.session_state[
            SessionManager.BACKEND_KEY
        ]