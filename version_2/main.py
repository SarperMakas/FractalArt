"""
Main Python Script for the simulation
"""
import random

import pygame, math

from LSystem import LSystem
from arts import Arts
from typing import Dict
import asyncio


class Main:
    """Main class"""

    def __init__(self):
        """Initialize
        :rtype: Main Class of the simulation
        """
        self.width: int = 500
        self.height: int = 500

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Fractal Art")

        self.startX: int = self.width//2
        self.startY: int = self.height//2

        self.rules: Dict[str, Rule] = {}

        self.lineLength = 40
        self.system: LSystem = self.set_system()

        self.fps: int = 100
        self.clock = pygame.time.Clock()
        self.run: bool = True
        self.i = 0

    def set_system(self) -> LSystem:
        """
        Set system randomly

        return: LSystem
        """
        # art_data = random.choice(Arts.arts)
        art_data = Arts.Dragon
        lSystem = LSystem(screen=self.screen,
                          artData=art_data,
                          length=self.lineLength,
                          n=3)
        return lSystem

    def event(self) -> None:
        """
        Main event method
        Includes main event loop
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.run = False

    def main(self) -> None:
        """
        Main method
        """

        while self.run:
            self.event()
            self.draw()
            self.clock.tick(self.fps)
        quit()

    def draw(self) -> None:
        """
        Everything will draw in this method
        """
        self.screen.fill((0, 0, 0))  # fill with black
        self.system.draw()  # draw system
        r"""# self.system.draw()  # draw system
        if self.i <= 5:
            self.system.draw()  # draw system
           

            # pygame.image.save(self.screen, rf"C:\Users\Sarper\Desktop\F\Sierpinski\sierpinski{self.i}.jpeg")
            self.i += 1
        else:
            # self.run = False
            self.system.reset()
            self.system.draw()  # draw system"""

        pygame.display.flip()


Main().main()
