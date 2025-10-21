main_page_style = """
    <style>
        /* Hide sidebar and its toggle completely */
        [data-testid="stSidebar"] { display: none; }
        [data-testid="collapsedControl"] { display: none; }
    </style>
"""

detection_page_style = """
    <style>
        [data-testid="stSidebar"] { display: block; }
        [data-testid="collapsedControl"] { display: block; }
        [data-testid="stSidebarNav"] { display: none; }
        [data-testid="stSidebarHeader"] { display: none; }
    </style>
"""