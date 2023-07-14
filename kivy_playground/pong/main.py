from pathlib import Path

import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget

from kivy_playground.pong.widgets.ball.pong_ball import PongBall  # noqa: F401
from kivy_playground.pong.widgets.game.pong_game import PongGame

kivy.require("2.2.1")

# Load Widgets dependencies
DIR_PATH: Path = Path(__file__).resolve().parent
WIDGETS: tuple[str, ...] = (
    str(DIR_PATH / "widgets" / "game" / "pong_game.kv"),
    str(DIR_PATH / "widgets" / "ball" / "pong_ball.kv"),
)
for widget_kv in WIDGETS:
    Builder.load_file(widget_kv)


class PongApp(App):
    """A pong application."""

    def build(self: "PongApp") -> Widget:
        """Build the pong application and register files.

        Returns
        -------
        Widget
            The pong application.
        """
        game = PongGame()

        # 60 ticks per second clock
        Clock.schedule_interval(game.update, 1.0 / 60.0)

        # Start movement of ball
        game.ball.init_velocity()

        return game


def run_pong_app() -> None:
    """Run the pong application."""
    try:
        PongApp().run()
    except KeyboardInterrupt:
        print("Time to Buzz the Tower!")
        exit(0)


if __name__ == "__main__":
    run_pong_app()
