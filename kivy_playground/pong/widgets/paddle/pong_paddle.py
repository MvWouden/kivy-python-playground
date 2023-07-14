import kivy
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector

from kivy_playground.pong.widgets.ball.pong_ball import PongBall

kivy.require("2.2.1")


class PongPaddle(Widget):
    """A pong paddle controlled by a player."""

    score: int = NumericProperty(0)
    speedup: float = 1.1

    def bounce_ball(self: "PongPaddle", ball: PongBall) -> None:
        """Bounce a ball with the paddle.

        Parameters
        ----------
        ball : PongBall
            The pong ball to bounce.
        """
        if not self.collide_widget(ball):
            return

        offset = 0.02 * Vector(0, ball.center_y - self.center_y)
        ball.velocity = (offset - ball.velocity) * self.speedup
