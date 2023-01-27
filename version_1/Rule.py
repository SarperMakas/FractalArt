from typing import *


class Rule:
    """Rule of the fractal art"""
    def __init__(self, axiom: str, angle: float, rules: Dict[str, str]):
        """
        :param axiom: String of the fractal
        :param angle: Angle of the movement
        :param rules: Rules
        """

        self.angle = angle
        self.axiom = axiom
        self.rules = rules


