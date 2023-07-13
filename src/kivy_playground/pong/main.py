import os
from pathlib import Path

import kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget

from src.kivy_playground.pong.widgets.ball.pong_ball import (  # noqa: F401
    PongBall,
)
from src.kivy_playground.pong.widgets.game.pong_game import PongGame

kivy.require("2.2.1")
DIR_PATH: str = os.path.dirname(os.path.realpath(__file__))


class PongApp(App):
    """A pong application."""

    def build(self) -> Widget:
        """Build the pong application and register files."""
        Builder.load_file(
            str(Path(DIR_PATH) / "widgets" / "game" / "pong_game.kv")
        )
        Builder.load_file(
            str(Path(DIR_PATH) / "widgets" / "ball" / "pong_ball.kv")
        )

        return PongGame()


def run_pong_app() -> None:
    """Run the pong application."""
    try:
        PongApp().run()
    except KeyboardInterrupt:
        print("Time to Buzz the Tower!")
        exit(0)


if __name__ == "__main__":
    run_pong_app()
