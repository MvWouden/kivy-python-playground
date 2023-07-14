import kivy
from kivy.clock import Clock
from kivy.input import MotionEvent
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector

from kivy_playground.pong.widgets.ball.pong_ball import PongBall
from kivy_playground.pong.widgets.paddle.pong_paddle import PongPaddle

kivy.require("2.2.1")


class PongGame(Widget):
    """A game of pong."""

    ball: PongBall = ObjectProperty(None)
    player1: PongPaddle = ObjectProperty(None)
    player2: PongPaddle = ObjectProperty(None)

    def update(self: "PongGame", _: int) -> None:
        """Perform game update tick.

        Parameters
        ----------
        _ : int
            Elapsed time between scheduling and calling of method.
            Passed along with clock update call.
        """
        self.ball.move()

        # bounce off paddles
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # bounce off top and bottom
        if self.ball.y < self.y or self.ball.top > self.top:
            self.ball.velocity_y *= -1

        # point scored by player 1
        if self.ball.right > self.width:
            self.player1.score += 1
            self.reset()
            return

        # point scored by player 2
        if self.ball.x < self.x:
            self.player2.score += 1
            self.reset()
            return

    def reset(self: "PongGame") -> None:
        """Reset the pong ball."""
        self.ball.velocity = Vector(0, 0)
        self.ball.center = self.center
        Clock.schedule_once(self.ball.init_velocity, 1)

    def on_touch_move(self: "PongGame", touch: MotionEvent) -> None:
        """Move the paddles on touch movements.

        Parameters
        ----------
        touch : MotionEvent
            A touch movement.
        """
        # Move player 1 paddle
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y

        # Move player 2 paddle
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y
