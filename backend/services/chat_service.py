"""
chat_service.py
"""
class ChatService:

    def __init__(self):

        self.sessions = {
            "Session 1": []
        }

        self.active_session = (
            "Session 1"
        )
    def create_session(
        self,
        session_name: str
    ):

        if session_name not in self.sessions:

            self.sessions[
                session_name
            ] = []
    def switch_session(
        self,
        session_name: str
    ):

        if session_name in self.sessions:

            self.active_session = (
                session_name
            )
    def get_sessions(
        self
    ):

        return list(
            self.sessions.keys()
        )
    def add_user_message(
        self,
        message: str
    ):

        self.sessions[
            self.active_session
        ].append(
            {
                "role": "user",
                "content": message
            }
        )

    def add_ai_message(
        self,
        message: str
    ):

       self.sessions[
            self.active_session
        ].append(
            {
                "role": "assistant",
                "content": message
            }
        )

    def get_history(
        self
    ):

        return (
            self.sessions[
                self.active_session
            ]
        )

    def clear(
        self
    ):

        self.sessions[
            self.active_session
        ].clear()
    def get_recent_history(
        self,
        limit: int
    ):

        history = []

        for msg in self.sessions[self.active_session][-limit:]:

            if msg["role"] == "user":

                history.append(
                    {
                        "role" : "user" , 
                        "content"  : msg["content"]
                    }
                )

            else:

                history.append(
                    {
                        "role" : "assistant",
                        "content" : msg["content"]
                    }
                )

        return history