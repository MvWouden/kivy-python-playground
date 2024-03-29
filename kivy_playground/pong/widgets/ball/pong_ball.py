import random

import kivy
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector

kivy.require("2.2.1")


class PongBall(Widget):
    """A pong ball moving at a certain velocity."""

    pos: list[float]

    # velocity of the ball on the x- and y-axis
    velocity_x: float = NumericProperty(0)
    velocity_y: float = NumericProperty(0)

    # referencelist property so we can use ball.velocity as a shorthand
    velocity: tuple[float, float] = ReferenceListProperty(
        velocity_x, velocity_y
    )

    def init_velocity(self: "PongBall", _: int | None = None) -> None:
        """Initialize the velocity with randomized values."""
        self.velocity = Vector(4, 0).rotate(random.randint(-30, 30))

    def move(self: "PongBall") -> None:
        """Move the ball one step using its velocity."""
        self.pos = Vector(*self.velocity) + self.pos
