"""
Main Python Script for the simulation
"""
import random

import pygame, math

from LSystem import LSystem
from arts import Arts
from typing import Dict
import asyncio
import sys


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

        self.fps: int = 200
        self.clock = pygame.time.Clock()
        self.run: bool = True
        self.i = 0
        self.simulation_run = False
        self.n = 4
        self.iter_per_time = 15
        self.random_system = True
        self.choosen_system = ""


    def set_system(self) -> LSystem:
        """
        Set system randomly

        return: LSystem
        """
        if self.random_system:
            art_data = random.choice(Arts.arts)
        else:
            art_data = Arts.arts_dict[self.choosen_system.lower()]

        lSystem = LSystem(screen=self.screen,
                          artData=art_data,
                          length=self.lineLength,
                          n=self.n,
                          preline=False,
                          iter_per_time=self.iter_per_time)
        return lSystem

    def user_input(self) -> bool:
        """
        Gets user input
        :return: user input is get without error or with error
        """
        if len(sys.argv) > 1:
            try:
                try:
                    self.n = int(sys.argv[1])
                except:
                    print("Error with number_of_iter")
                    raise Exception("error n")

                try:
                    self.iter_per_time = int(sys.argv[2])
                except:
                    print("Error with iter_per_time")
                    raise Exception("iter_per_time")

                try:
                    self.random_system = True if sys.argv[3].lower() == "true" else False

                    if not self.random_system:
                        self.choosen_system = sys.argv[4]
                    self.system: LSystem = self.set_system()
                except:
                    print("Error with system choosing")
                    raise Exception("system choosing")

            except Exception as e:
                print(e)
                print("\nError in command line arguments make sure:")
                print("You write command line as number_of_iter iter_per_time random_system")
                print("If random system is False you must give 4. argument as system_name")
                print("number_of_iter, iter_per_time must be integer")
                print("system_name must be one of the Tree, Triangle, Sierpinski, Plant, Dragon, Turtle\n")
                return True
        else:
            self.system: LSystem = self.set_system()
        return False

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
        if self.user_input():
            return

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
