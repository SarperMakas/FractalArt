"""
Data of the fractal art.
Include information of the FractalData.txt of the version_1
"""

from typing import Dict


class __ArtData:
    def __init__(self, axiom: str, rules: Dict[str, str], angle: int):
        """
        Class that is includes only the data for the fractal pattern.
        This class is going to use at Arts class which is the class that is
        include every fractal arts data using this class (__ArtData)

        :param axiom: axiom of the text
        :param rules: rules of the pattern
        :param angle: angle of the rotation
        """
        self.axiom = axiom
        self.angle = angle
        self.rules = rules


class Arts:
    """
    It is a class that replaces the FractalData file in version 1
    The aim of this class is not using the .TXT file for scraping data
    instead of using variables of this class
    """
    Tree = __ArtData("F", {"F": "FF+[+F-F-F]-[-F+F+F]"}, 30)
    Triangle = __ArtData("F+F+F", {"F": "F-F+F"}, 120)
    Sierpinski = __ArtData("F-G-G", {"F": "F-G+F+G-F", "G": "GG"}, 120)
    Plant = __ArtData("X", {"X": "F+[[X]-X]-F[-FX]+X", "F": "FF"}, 25)
    Dragon = __ArtData("FX", {"X": "X+YF+", "Y": "-FX-Y"}, 90)
