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
        self.width: int = 750
        self.height: int = 650

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Fractal Art")

        self.startX: int = self.width//2
        self.startY: int = self.height//2

        self.rules: Dict[str, Rule] = {}

        self.lineLength = 40
        self.system: LSystem = self.set_system()

        self.fps: int = 200
        self.clock = pygame.time.Clock()
        self.run: bool = True
        self.i = 0
        self.simulation_run = False

    def set_system(self) -> LSystem:
        """
        Set system randomly

        return: LSystem
        """
        art_data = random.choice(Arts.arts)
        lSystem = LSystem(screen=self.screen,
                          artData=art_data,
                          length=self.lineLength,
                          n=8,
                          preline=False,
                          iter_per_time=50)
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
                if event.key == pygame.K_SPACE:
                    self.simulation_run = not self.simulation_run

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
        # self.screen.fill((0, 0, 0))  # fill with black
        if self.simulation_run:
            self.system.draw()  # draw system

        self.clock.tick(self.fps)
        pygame.display.flip()


Main().main()
