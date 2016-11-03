import unittest
import requests
import logging
import json
import time
import pickle
import sys
from time import gmtime, strftime
#from requests.packages.urllib3 import response
#import configs.config

HEADER = {'content-type': 'text/xml'}

class CISService(unittest.TestCase):
    def __init__(self, testName, *args):
        super(CISService, self).__init__(testName)
        self.cisEndpoint = "http://weather-citystate-service.cfapps.io/getZipForCityState?state=CT&city=Windsor"
        logging.basicConfig(filename="cis.log",level=logging.DEBUG)
        sys.stdout = open('finaltestresult', 'w')
        sys.stdout.flush()
        
    def setUp(self):
        logging.debug("Validating: %s"%self._testMethodName)
        logging.debug("Validating: %s"%self.cisEndpoint)

    def tearDown(self):
        logging.debug(" Request:")#%s"%self.cisEndpoint)#, "/%s"%self.params)
        logging.debug(" Response:")#%s"%self.response)

    def testGetCustomerForValidTN(self):
        """TestCase:getCustomerForValidTN"""
        trackingId = "CIS_"+self._testMethodName[4:]+str(time.time()).replace(".","")[8:]
        self.testId = 1#self.params[0][0]
        uri = "http://weather-citystate-service.cfapps.io/getZipForCityState?state=CT&city=Windsor"
        response = requests.get(uri)
        self.response = response
        data = response.json()
        f = open('workfile', 'a')
        pickle.dump(response.content, f)
        f.close()
        self.assertEqual(data['country abbreviation'], 'US')
        
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)    
        
if __name__ == '__main__':
    unittest.main()
