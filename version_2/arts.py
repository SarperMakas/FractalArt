"""
Data of the fractal art.
Include information of the FractalData.txt of the version_1
"""

from typing import Dict, List
import math


class _ArtData:
    def __init__(self, axiom: str, rules: Dict[str, str], angle: float, ratio: float):
        """
        Class that is includes only the data for the fractal pattern.
        This class is going to use at Arts class which is the class that is
        include every fractal arts data using this class (_ArtData)

        :param axiom: axiom of the text
        :param rules: rules of the pattern
        :param angle: angle of the rotation
        """

        self.axiom = axiom
        self.rules = rules
        self.angle = angle
        self.ratio = ratio


class Arts:
    """
    It is a class that replaces the FractalData file in version 1
    The aim of this class is not using the .TXT file for scraping data
    instead of using variables of this class
    """
    Tree: _ArtData = _ArtData("F", {"F": "FF+[+F-F-F]-[-F+F+F]"}, math.radians(30), 0.65)
    Triangle: _ArtData = _ArtData("F+F+F", {"F": "F-F+F"}, math.radians(120), 0.8)
    Sierpinski: _ArtData = _ArtData("F-G-G", {"F": "F-G+F+G-F", "G": "GG"}, math.radians(120), 0.8)
    Plant: _ArtData = _ArtData("X", {"X": "F+[[X]-X]-F[-FX]+X", "F": "FF"}, math.radians(25), 0.65)
    Dragon: _ArtData = _ArtData("FX", {"X": "X+YF+", "Y": "-FX-Y"}, math.radians(90), 0.8)
    Turtle: _ArtData = _ArtData("F-F-F-F", {"F": "F-F+F+FF-F-F+F"}, math.radians(90), 0.4)

    arts: List[_ArtData] = [Tree, Triangle, Sierpinski, Plant, Dragon, Turtle]
    arts_dict: Dict[str, _ArtData] = {"tree": Tree,
                                      "triangle": Triangle,
                                      "sierpinski": Sierpinski,
                                      "plant": Plant,
                                      "dragon": Dragon,
                                      "turtle": Turtle}
