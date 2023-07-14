import kivy
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

from kivy_playground.pong.widgets.ball.pong_ball import PongBall

kivy.require("2.2.1")


class PongGame(Widget):
    """A game of pong."""

    ball: PongBall = ObjectProperty(None)

    def update(self: "PongGame", _: int) -> None:
        """Perform game update tick.

        Parameters
        ----------
        _ : int
            Passed along clock update call.
        """
        self.ball.move()

        # bounce off left and right
        if self.ball.x < 0 or self.ball.right > self.width:
            self.ball.velocity_x *= -1

        # bounce off top and bottom
        if self.ball.y < 0 or self.ball.top > self.height:
            self.ball.velocity_y *= -1
