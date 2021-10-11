
import numpy as np
from numpy import ndarray

class LUT:
    """
    Following the documentation from
    https://wwwimages2.adobe.com/content/dam/acom/en/products/speedgrade/cc/pdfs/cube-lut-specification-1.0.pdf
    """

    def __init__(self, filepath: str) -> None:
        """
        LUT / Cube file parser

        Args:
            filepath (str): Path to LUT / Cube file
        """
        self._filepath = filepath

        self._title = None  # or undefined as said in the docu
        self._domain_min = np.array([0, 0, 0])  # according to docu
        self._domain_max = np.array([1, 1, 1])  # according to docu

        self._parse_LUT()

    def _parse_LUT(self):
        """
        Parses a LUT file
        """
        with open(self._filepath, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith('TITLE'):
                    self._title = line[len('TITLE'):].strip()
                    if self._title.startswith('"'):
                        self._title = self._title[1:]
                    if self._title.endswith('"'):
                        self._title = self._title[:-1]
                elif line.startswith('DOMAIN_MIN'):
                    self._domain_min = self._parse_numbers(line[len('DOMAIN_MIN'):].strip())
                elif line.startswith('DOMAIN_MAX'):
                    self._domain_max = self._parse_numbers(line[len('DOMAIN_MAX'):].strip())
                elif line.startswith('LUT_1D_SIZE') or line.startswith('LUT_3D_SIZE'):
                    self.table_size = self._parse_numbers(line[len('LUT_XD_SIZE'):].strip())[0]
                elif line.startswith('#') or len(line) == 0:
                    # comment --> continue
                    continue
                else:
                    # must be data ; should be stored
                    pass

    def _parse_numbers(self, numberstr: str):
        """
        Parses a number according to CUBE documentation

        Args:
            numberstr (str): Line string which shall be parsed

        Returns:
            nd.narray: Array with the values found in the numberstr
        """
        numbers = []
        currentnumber = ""

        for c in numberstr:
            if c.isdigit() or c == '-' or c == '.':
                currentnumber += c
            elif len(currentnumber) > 0:
                numbers.append(float(currentnumber))
                currentnumber = ""
        if len(currentnumber) > 0:
            numbers.append(float(currentnumber))

        return np.array(numbers)

    @property
    def title(self):
        return self._title

    @property
    def domain_min(self):
        return self._domain_min

    @property
    def domain_max(self):
        return self._domain_max


class Pyluter:

    @staticmethod
    def apply_LUT(image, lut: LUT):

        # Load image as ndarray
        if not isinstance(image, ndarray):
            # Load image first
            try:
                import cv2
            except:
                raise Exception('cv2 not installed --> Cannot read in image. Install cv2 first!')
            _image_array = cv2.imread(image)
        else:
            _image_array = image

        # Apply ndarray
        raise NotImplementedError()
