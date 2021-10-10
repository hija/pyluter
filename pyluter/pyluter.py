class LUT:
    pass


from numpy import ndarray

class Pyluter:

    @staticmethod
    def apply_LUT(image, lut: LUT):

        ## Load image as ndarray
        if not isinstance(image, ndarray):
            # Load image first
            try:
                import cv2
            except:
                raise Exception('cv2 not installed --> Cannot read in image. Install cv2 first!')
            _image_array = cv2.imread(image)
        else:
            _image_array = image
        
        ## Apply ndarray
        raise NotImplementedError()

