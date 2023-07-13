import importlib
from pathlib import Path

import kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget

from kivy_playground.pong.widgets.ball.pong_ball import PongBall  # noqa: F401
from kivy_playground.pong.widgets.game.pong_game import PongGame

kivy.require("2.2.1")

DIR_PATH: Path = Path(__file__).resolve().parent
WIDGETS: tuple[tuple[str, str], ...] = (
    (
        "kivy_playground.pong.widgets.game",
        str(DIR_PATH / "widgets" / "game" / "pong_game.kv"),
    ),
    (
        "kivy_playground.pong.widgets.ball",
        str(DIR_PATH / "widgets" / "ball" / "pong_ball.kv"),
    ),
)


class PongApp(App):
    """A pong application."""

    def build(self: "PongApp") -> Widget:
        """Build the pong application and register files.

        Returns
        -------
        Widget
            The pong application.
        """
        # Load Widgets dependencies
        for widget, widget_kv in WIDGETS:
            importlib.import_module(widget)
            Builder.load_file(widget_kv)

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
