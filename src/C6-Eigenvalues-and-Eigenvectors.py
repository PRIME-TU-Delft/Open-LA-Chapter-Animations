from manim import *
from primescene import PrimeScene
from define import *
import colors


class EigenvaluesAndEigenvectors(PrimeScene):

    def construct(self):
        # Setup the PRIME custom tex template
        PrimeScene.construct(self)

        # Create window rectangle (which is not displayed)
        window = Rectangle(width=WIDTH, height=HEIGHT)
        window.to_corner(UP + LEFT, buff=0)

        test = MathTex(r"\sum_0^{10} why", color=colors.pink)
        test.move_to(window)

        self.play(Write(test))

        self.wait(1)
