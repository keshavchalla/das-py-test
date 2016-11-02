import unittest
import urllib2
import logging
import random
import requests

import time
import urllib2
from datetime import datetime, timedelta
import xml.dom.minidom
'''
Created on Oct 31, 2016

@author: keshav
'''



class Test(unittest.TestCase):

   logging.basicConfig(filename="c:\users\keshav\example.log",level=logging.DEBUG)
   
   def setUp(self):
       pass


   def tearDown(self):
       pass

  
   def testRestService(self):
       logging.debug('I told you so so  what')
       logging.warning('Watch out!')
       
       url = 'http://localhost:8080/'
       response = requests.get(url)
       print response.text
       self.assertEqual(response.text,'Greetings from Spring Boot!')

   def testWeatherService(self):
       logging.debug('Testing Weather Service')
       url = 'http://localhost:8080/weatherDetails'
       response = requests.get(url)
       data = response.json()
       self.assertEqual(data['countryCode'],'USA')
       
   def testCity(self):
       logging.debug('Testing City in Weather Service')
       url = 'http://localhost:8080/weatherDetails'
       response = requests.get(url)
       data = response.json()
       self.assertEqual(data['city']['name'],'West Chester')
       
if __name__ == "__main__":
   #import sys;sys.argv = ['', 'Test.testRestService']
   unittest.main()