"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    """The app state."""

    pass


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("Hello Bro !",
                        background_image="linear-gradient(271.68deg, #ee0979,#ff6a00 )",
                        background_clip="text",
                        font_weight="bold",
                        font_size="2em",),
            pc.box(
                "Hello, visit my site and get answers to your questions",
                color = "#e0eafc",
                font_family = "Monospace"
            ),
            pc.link(
                "Go to my web site ...",
                href="https://javokhir0729.vercel.app/",    
                border="5px solid #e0eafc",
                padding="0.5em",
                border_radius="40px",
                transition = "0.5s",
                background_image="linear-gradient(271.68deg, #ee0979,#ff6a00 )",
                background_clip="text",
                _hover={
                    "color": "#fff",
                    "border" : "5px solid transparent"
                },
            ),
            spacing="1.5em",
            font_size="2em",
        ),
        height = "100vh",
        # padding_top="10%",
        # background = "#000000"
        # background_image = "linear-gradient(45deg, #00428, #004292)"
        # justify_content="center"
        background_image="linear-gradient(271.68deg, #141e30,#243b55 )"
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
