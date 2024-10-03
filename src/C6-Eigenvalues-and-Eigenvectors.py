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

        text_A_matrix = MathTex(r"\text{Let }", r"A", r"\text{ be an }", r"n \times n",
                                r"\text{ matrix.}", color=colors.offwhite)
        text_A_matrix.move_to(window)

        self.play(Write(text_A_matrix))

        matrix_A_title = MathTex(r"A", color=colors.offwhite)
        matrix_A_assignment = MathTex(r"=", color=colors.offwhite)
        matrix_A = Matrix(
            [[r"\cdot", r"\cdot", r"\cdot"],
             [r"\cdot", r"\cdot", r"\cdot"],
             [r"\cdot", r"\cdot", r"\cdot"]],
            color=colors.offwhite
        )
        matrix_A.move_to(window).shift(2*DOWN)
        matrix_A_assignment.next_to(matrix_A, LEFT, buff=0.2)
        matrix_A_title.next_to(matrix_A_assignment, LEFT, buff=0.2)

        matrix_A_group = VGroup(matrix_A, matrix_A_title, matrix_A_assignment)

        text_matrix_group = VGroup(text_A_matrix, matrix_A_group)

        text_matrix_group.generate_target()
        text_matrix_group.target.shift(2*UP)

        self.play(AnimationGroup(
            FadeIn(matrix_A_group),
            MoveToTarget(text_matrix_group)
        ))

        self.wait(3)

        self.play(AnimationGroup(
            FadeOut(matrix_A_assignment),
            FadeOut(matrix_A)
        ))

        vector_v = MathTex(r"\mathbf{v}", color=colors.offwhite)
        equals_sign = MathTex(r"=", color=colors.offwhite)
        vector_v_copy = MathTex(r"\mathbf{v}", color=colors.offwhite)
        lambda_sign = MathTex(r"\lambda", color=colors.offwhite)

        equals_sign.move_to(window)
        vector_v.next_to(equals_sign, LEFT, buff=0.2)
        lambda_sign.next_to(equals_sign, RIGHT, buff=0.2)
        vector_v_copy.next_to(lambda_sign, RIGHT, buff=0.07)

        matrix_A_title.generate_target()
        matrix_A_title.target.next_to(vector_v, LEFT, buff=0.07).shift(0.05*UP)
        lambda_sign.shift(0.05*UP)

        self.play(AnimationGroup(
            MoveToTarget(matrix_A_title),
            FadeIn(vector_v, shift=LEFT),
            FadeIn(equals_sign, shift=LEFT),
            FadeIn(lambda_sign, shift=LEFT),
            FadeIn(vector_v_copy, shift=LEFT),
            lag_ratio=0.05
        ))

        self.wait(9)

        text_eigenvalue_vector = MathTex(
            r"\text{Vector }", r"\mathbf{v}", r"\text{ is an eigenvector of matrix }", r"A",
            r"\text{ for the eigenvalue }", r"\lambda", color=colors.offwhite)
        text_eigenvalue_vector.move_to(window).shift(2*DOWN)

        self.play(Write(text_eigenvalue_vector))

        self.wait(5)

        self.play(AnimationGroup(
            Unwrite(text_A_matrix),
            Unwrite(matrix_A_title),
            Unwrite(vector_v),
            Unwrite(equals_sign),
            Unwrite(lambda_sign),
            Unwrite(vector_v_copy),
            Unwrite(text_eigenvalue_vector)
        ))

        self.wait(1)
