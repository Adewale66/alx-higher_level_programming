import unittest
from models.base import Base


class BaseTest(unittest.TestCase):

    def test_doc(self):
        """Test documentation"""
        self.assertIsNotNone(Base.__doc__)
        self.assertGreater(len(Base.__doc__), 1)
        self.assertIsNotNone(Base.__init__.__doc__)
        self.assertGreater(len(Base.__init__.__doc__), 1)

    def test_base(self):
        """Test base class"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)
