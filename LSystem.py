import pygame, math
from typing import *
from Rule import Rule


class LSystem:
    """LSystem class for generation string and drawing to the screen"""
    def __init__(self, screen, rule: Rule,
                 startX: int, startY: int,
                 length: int, ratio: float):
        """
        :param name: name of the project
        :param screen: Screen of the simulation
        :param axiom: start text
        :param rules: rules of the fractal
        :param startX: Start x position
        :param startY: Start y position
        :param length: Length of the lines
        :param angle: Angle of the movement
        :param ratio: Length ratio (length *= ratio for each Iteration)
        """
        self.screen = screen
        self.axiom = rule.axiom
        self.rules = rule.rules
        self.start = (startX, startY)
        self.x, self.y = startX, startY
        self.length: int = length
        self.dtheta: float = rule.angle
        self.ratio: float = ratio
        self.theta: float = math.pi / 2
        self.positions = []

    def generate(self) -> None:
        """Generate"""
        self.x, self.y = self.start
        self.length *= self.ratio
        self.theta = math.pi / 2
        newAxiom = ""
        for char in self.axiom:
            mapped = char
            try:
                mapped = self.rules[char]
            except:
                pass
            newAxiom += mapped
        self.axiom = newAxiom

    def draw(self) -> None:
        """
        Draw fractal
        """

        color = 0
        colorChange = 255 / len(self.axiom)
        for char in self.axiom:
            if char == 'F' or char == 'G' or char == 'A' or char == 'B':
                # set x2 and y2
                x2 = self.x - self.length * math.cos(self.theta)
                y2 = self.y - self.length * math.sin(self.theta)
                pygame.draw.line(self.screen, (color, 255 - color, 100 + color / 255),
                                 (self.x, self.y), (x2, y2))
                self.x, self.y = x2, y2
            elif char == "+":
                self.theta += self.dtheta  # right
            elif char == "-":
                self.theta -= self.dtheta  # left
            elif char == '[':
                self.positions.append({'x': self.x, 'y': self.y, 'theta': self.theta})
            elif char == ']':
                dict = self.positions.pop()
                self.x = dict['x']
                self.y = dict['y']
                self.theta = dict['theta']
            # change color value
            color += colorChange



