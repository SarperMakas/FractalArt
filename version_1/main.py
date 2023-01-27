import pygame, math

from LSystem import LSystem
from Rule import Rule
from Fractal import Fractal
from typing import *
import asyncio


class Main:
    """Main class"""
    def __init__(self):
        """Initialize
        :rtype: Main Class of the simulation
        """
        self.width: int = 0
        self.height: int = 0

        self.startX: int = 0
        self.startY: int = 0

        self.rules: Dict[str, Rule] = {}

        self.ratio = 0.5
        self.systemNo: str = self.getSystem()
        self.system: LSystem = None
        self.lineLength = 40

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Fractal Art")

        self.fps: int = 10
        self.clock = pygame.time.Clock()
        self.run: bool = True
        self.i = 0


    def getSystem(self) -> str:
        """
        Get chosen system of the simulation
        :return: system
        """
        print("0. Triangle\n1. Plant\n2. Dragon\n3. Tree\n4. Sierpinski")
        fractalDict = {0: Fractal.Triangle, 1: Fractal.Plant,
                            2: Fractal.Dragon, 3: Fractal.Tree, 4: Fractal.Sierpinski}
        num = 0
        while True:
            try:
                num = int(input("Enter fractal number: "))
                if 0 <= num <= 4:
                    break
            except:
                pass
        while True:
            try:
                nums = list(map(float, input("Enter width, height, x, y and ratio:").split(" ")))
                self.width = int(nums[0])
                self.height = int(nums[1])
                self.startX = int(nums[2])
                self.startY = int(nums[3])
                self.ratio = nums[4]
                break
            except:
                pass

        return fractalDict[num]

    def readRules(self) -> None:
        """
        Read rules from FractalData/FractalData.txt
        add to the dict()
        """
        with open("FractalData.txt", "r") as data:
            for line in data.readlines()[1:]:  # first line is comment line
                lineData = line.split(",")
                rules: Dict[str, str] = {}
                # get rules
                for i in lineData[3:-1]:
                    mapping = i.split(" ")
                    rules[mapping[0]] = mapping[1]

                # add to rules")
                self.rules[lineData[0]] = Rule(axiom=lineData[1],
                                               angle=math.radians(int(lineData[-1])),
                                               rules=rules)

        # set system
        self.system = LSystem(screen=self.screen,
                              rule=self.rules[self.systemNo],
                              startX=self.startX,
                              startY=self.startY,
                              length=self.lineLength,
                              ratio=self.ratio)


    def event(self) -> None:
        """
        Main event method
        Includes main event loop
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

    def main(self) -> None:
        """
        Main method
        """
        self.readRules()

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
        self.system.generate()  # generate

        if self.i <= 15:
            pygame.image.save(self.screen, rf"C:\Users\Sarper\Desktop\F\Sierpinski\sierpinski{self.i}.jpeg")
            self.i += 1
        else:
            self.run = False
        pygame.display.flip()


Main().main()

