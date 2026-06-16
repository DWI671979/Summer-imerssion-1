"""
Inkverse — main Streamlit application.

A colorful, open-source collaborative storytelling platform where writers can
publish fiction, collaborate on universes, showcase short films, and run an
offline text-recognition originality check before publishing.
"""

from __future__ import annotations

import streamlit as st

from lib import seed, ui
from views import (
    page_account,
    page_copyright,
    page_explore,
    page_films,
    page_home,
    page_legal,
    page_universes,
    page_write,
)

st.set_page_config(
    page_title="Inkverse — stories, universes & short films",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

ui.inject_css()
seed.ensure_seeded()

PAGES = {
    "Home": page_home.render,
    "Explore stories": page_explore.render,
    "Write & publish": page_write.render,
    "Shared universes": page_universes.render,
    "Short films": page_films.render,
    "Copyright check": page_copyright.render,
    "Legal & IP": page_legal.render,
    "Account": page_account.render,
}


def go_to(page_name: str) -> None:
    """Navigate to a page from buttons/cards.

    Keep navigation state separate from Streamlit widget keys.
    Streamlit does not allow assigning to a session_state key after a widget
    with the same key has been instantiated in the current run.
    """
    st.session_state["page"] = page_name


def sidebar() -> str:
    with st.sidebar:
        ui.brand_header()
        st.divider()

        user = st.session_state.get("user")
        if user:
            ui.avatar(user.get("avatar"), size=64)
            st.success(f"Signed in as **{user['display_name']}**")
        else:
            st.info("Browsing as a guest. Sign in to publish.")

        page_names = list(PAGES.keys())
        if "page" not in st.session_state or st.session_state["page"] not in PAGES:
            st.session_state["page"] = "Home"

        choice = st.radio(
            "Navigate",
            page_names,
            index=page_names.index(st.session_state["page"]),
            label_visibility="collapsed",
        )
        st.session_state["page"] = choice

        st.divider()
        from lib import storage
        from lib.copyright_checker import engine_name

        st.caption("System status")
        st.write("Storage:", "GitHub" if storage.github_enabled() else "Local demo")
        st.write("Originality:", "Offline text recognition")
        st.caption(engine_name())
    return st.session_state["page"]


def main() -> None:
    choice = sidebar()
    PAGES[choice]()


if __name__ == "__main__":
    main()
