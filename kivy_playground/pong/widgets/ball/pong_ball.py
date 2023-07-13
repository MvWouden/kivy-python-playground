import kivy
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector

kivy.require("2.2.1")


class PongBall(Widget):
    """A pong ball moving at a certain velocity."""

    # velocity of the ball on the x- and y-axis
    velocity_x: int = NumericProperty(0)
    velocity_y: int = NumericProperty(0)

    # referencelist property so we can use ball.velocity as a shorthand
    velocity: tuple[int, int] = ReferenceListProperty(velocity_x, velocity_y)

    def move(self: "PongBall") -> None:
        """Move the ball one step using its velocity."""
        self.pos += Vector(*self.velocity)
