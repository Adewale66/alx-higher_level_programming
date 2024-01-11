import unittest
from models.rectangle import Rectangle
from models.square import Square


class SquareTest(unittest.TestCase):

    def test_doc(self):
        """Test documentation"""
        self.assertIsNotNone(Square.__doc__)
        self.assertGreater(len(Square.__doc__), 1)
        self.assertIsNotNone(Square.__init__.__doc__)
        self.assertGreater(len(Square.__init__.__doc__), 1)

    def test_square_instance(self):
        """Test Square is a subclass of Rectangle class"""
        self.assertTrue(isinstance(Square(1), Rectangle))

    def test_square_instance_base(self):
        """Test Square is a subclass of Base class"""
        self.assertTrue(issubclass(Square, Rectangle))

    def test_square_attributes(self):
        """Test Square attributes"""
        s1 = Square(1)
        self.assertTrue(hasattr(s1, "id"))
        self.assertTrue(hasattr(s1, "size"))
        self.assertTrue(hasattr(s1, "x"))
        self.assertTrue(hasattr(s1, "y"))
