#!/usr/bin/python3
""""This is a script in the base model"""

import uuid
from datetime import datetime 

class BaseModel:
    """"This is a class from which other classes will inherit from"""
    
    def __init__(self):
        """initializing instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


    def __str__(self):
        """defines a format for the string representation of the class"""
        return "[{}] ({}) {}".\format(type(self).__name__, self.id, self.__dict__)


    def save(self):
       """updates the public instance attribute with the current datetime"""
       self.updated_at = datetime.now()

    def to_dict(self):
       """returns a dictionary containing all keys/values of the instance"""
       my_dict = self.__dict__.copy()
       my_dict["__class__"] = type(self).__name__

       return my_dict 
