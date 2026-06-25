def load_css():

    return """
    <style>

    .hero-title {

        font-size: 3rem;

        font-weight: 800;

        background:
        linear-gradient(
            90deg,
            #00E5FF,
            #8A2BE2
        );

        -webkit-background-clip:text;

        color: transparent;

        margin-bottom: 0;
    }

    .hero-subtitle {

        color:#AAAAAA;

        margin-bottom:25px;
    }

    .glass-card {

        background:
        rgba(
            255,
            255,
            255,
            0.05
        );

        backdrop-filter:
        blur(10px);

        border:
        1px solid rgba(
            255,
            255,
            255,
            0.1
        );

        border-radius:15px;

        padding:20px;

        margin-bottom:15px;
    }

    .repo-card {

        background:
        rgba(
            0,
            229,
            255,
            0.08
        );

        border:
        1px solid rgba(
            0,
            229,
            255,
            0.3
        );

        border-radius:15px;

        padding:20px;

        margin-bottom:20px;
    }

    /* Main App Background */

    .stApp {

        background:
        radial-gradient(
            circle at top left,
            rgba(0,229,255,0.10),
            transparent 35%
        ),

        radial-gradient(
            circle at top right,
            rgba(138,43,226,0.10),
            transparent 35%
        ),

        linear-gradient(
            135deg,
            #0B0F19,
            #111827,
            #0E1117
        );
    }

    /* Sidebar */

    [data-testid="stSidebar"] {

        background:
        linear-gradient(
            180deg,
            #111827,
            #0B1220
        );
    }

    /* Hide Streamlit default header */

    [data-testid="stHeader"] {

        background: transparent;
    }
    </style> 
    """
