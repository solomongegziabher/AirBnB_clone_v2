#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """amenity test class"""

    def __init__(self, *args, **kwargs):
        """Initializes the test class"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Tests the type of name """
        new = self.value()
        self.assertEqual(
                type(new.name), 
                str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
                )
