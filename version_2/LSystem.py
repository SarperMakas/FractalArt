"""
Defining LSystem
"""

import pygame, math
from typing import Dict, List, Tuple
from arts import _ArtData
from tqdm import tqdm


class LSystem:
    """LSystem class for generation string and drawing to the screen"""

    def __init__(self, screen, artData: _ArtData,
                 length: int, n: int, preline: bool,
                 iter_per_time: int):
        """
        :param name: name of the project
        :param screen: Screen of the simulation
        :param axiom: start text
        :param rules: rules of the fractal
        :param length: Length of the lines
        :param angle: Angle of the movement
        :param ratio: Length ratio (length *= ratio for each Iteration)
        :param preline: Drawing line path
        :param iter_per_time: iteration of drawing per time
        """
        self.screen: pygame.Surface = screen
        self.axiom: str = artData.axiom
        self.rules: Dict[str, str] = artData.rules
        self.length: int = length
        self.dtheta: float = artData.angle
        self.ratio: float = artData.ratio
        self.theta: float = math.pi / 2 + math.radians(150)
        self.positions: List[Dict[str, float]] = []
        self.preline = preline
        self.iter_per_time = iter_per_time

        self.width, self.height = self.screen.get_size()  # size of the screen
        self.fractal_surface = pygame.Surface((self.width*3, self.height*3))
        self.x, self.y = self.width // 2, self.height // 2
        self.start: Tuple[int, int] = (self.x, self.y)

        self.max_X = 0
        self.max_Y = 0
        self.min_X = self.width * 10000
        self.min_Y = self.height * 1000

        for i in tqdm(range(n)):
            self.generate()  # generate

        self.track_positions()
        self.w, self.h = self.max_X-self.min_X, self.max_Y-self.min_Y

        print(f"X: {self.max_X}, {self.min_X}")
        print(f"Y: {self.max_Y}, {self.min_Y}")
        print(f"Width: {self.w}")
        print(f"height: {self.h}"),

        if self.w > self.width or self.h > self.height:
            print("Size is not optimal")


        self.reset()
        self.fractal = self.draw_fractal_object()

        self.i = 0
        self.r = 0

    def reset(self):
        """Reset values"""
        self.x, self.y = self.start
        self.theta = math.pi / 2 + math.radians(150)

    def generate(self) -> None:
        """Generate"""
        self.reset()
        self.length *= self.ratio
        newAxiom = ""
        for char in self.axiom:
            mapped = char
            try:
                mapped = self.rules[char]
            except:
                pass
            newAxiom += mapped
        self.axiom = newAxiom

    def track_positions(self):
        """
        Get position
        """
        for char in tqdm(self.axiom):

            if char == 'F' or char == 'G' or char == 'A' or char == 'B':
                # set x2 and y2
                x2 = self.x - self.length * math.cos(self.theta)
                y2 = self.y - self.length * math.sin(self.theta)

                if self.preline:
                    pygame.draw.line(self.fractal_surface, (255, 255, 255),
                                     (self.x, self.y), (x2, y2))


                self.x, self.y = x2, y2

            elif char == "f" or char == "g" or char == "a" or char == "b":
                # set x2 and y2
                x2 = self.x - self.length * math.cos(self.theta)
                y2 = self.y - self.length * math.sin(self.theta)
            elif char == "+":
                self.theta += self.dtheta  # right
            elif char == "-":
                self.theta -= self.dtheta  # left
            elif char == '[':
                self.positions.append({'x': self.x, 'y': self.y, 'theta': self.theta})
            elif char == ']':
                _dict = self.positions.pop()
                self.x = _dict['x']
                self.y = _dict['y']
                self.theta = _dict['theta']

            # get values
            self.min_X = min(self.x, self.min_X)
            self.min_Y = min(self.y, self.min_Y)
            self.max_X = max(self.x, self.max_X)
            self.max_Y = max(self.y, self.max_Y)

    def draw_fractal_object(self):
        """
        Draws fractal object to `self.fractal`
        """
        # set color and fractal Surface
        color = 0
        colorChange = 255 / (len(self.axiom) + 10)

        for char in self.axiom:

            if char == 'F' or char == 'G' or char == 'A' or char == 'B':
                # set x2 and y2
                x2 = self.x - self.length * math.cos(self.theta)
                y2 = self.y - self.length * math.sin(self.theta)

                pygame.draw.line(self.fractal_surface, (color, 255 - color, 100 + color / 255),
                                 (self.x, self.y), (x2, y2))
                self.x, self.y = x2, y2

            elif char == "f" or char == "g" or char == "a" or char == "b":
                # set x2 and y2
                x2 = self.x - self.length * math.cos(self.theta)
                y2 = self.y - self.length * math.sin(self.theta)
            elif char == "+":
                self.theta += self.dtheta  # right
            elif char == "-":
                self.theta -= self.dtheta  # left
            elif char == '[':
                self.positions.append({'x': self.x, 'y': self.y, 'theta': self.theta})
            elif char == ']':
                _dict = self.positions.pop()
                self.x = _dict['x']
                self.y = _dict['y']
                self.theta = _dict['theta']
            # change color value
            color += colorChange
            yield

    def draw(self) -> None:
        """
        Draw fractal
        """
        if self.i < len(self.axiom):
            try:
                for _ in range(self.iter_per_time):
                    next(self.fractal)
            except:
                pass
            self.i += 1

        cropped = pygame.Surface((self.w, self.h))

        cropped.blit(self.fractal_surface, (0, 0), (self.min_X, self.min_Y, self.w, self.h))
        self.screen.blit(cropped, ((self.width-cropped.get_width())/2, (self.height-cropped.get_height())/2))
