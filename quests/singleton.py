'''
https://py.checkio.org/en/mission/capital-city/
You are an active traveler who have visited a lot of countries. The main city in the every country is its capital and each country can have only one capital city. So your task is to create the class Capital which has some special properties: the first created instance of this class will be unique and single, and all of the other instances should be the same as the very first one. 
Also you should add the name() method which returns the name of the capital. 
In this mission you should use the Singleton design pattern.
'''

class Capital(object):
    __instance = None
    
    def __new__(cls, city):
        if Capital.__instance is None:
            Capital.__instance = object.__new__(cls)
            Capital.__instance.city = city
        return Capital.__instance

    def name(self):
        return self.city

