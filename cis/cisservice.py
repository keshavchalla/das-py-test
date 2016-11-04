import unittest
import requests
import logging
import json
import time
import pickle
import sys
from time import gmtime, strftime
#from requests.packages.urllib3 import response
import configs.config

HEADER = {'content-type': 'text/xml'}

class CISService(unittest.TestCase):
    def __init__(self, testName, *args):
        super(CISService, self).__init__(testName)
        self.cisEndpoint = configs.config.CISEndpoint
        logging.basicConfig(filename="cis.log",level=logging.DEBUG)
        sys.stdout = open('finaltestresult', 'w')
        
    def setUp(self):
        logging.debug("Validating: %s"%self._testMethodName)
        logging.debug("Validating: %s"%self.cisEndpoint)

    def tearDown(self):
        logging.debug(" Request:%s"%self.cisEndpoint)
        logging.debug(" Response:%s"%self.response)

    def testValidTN_MultipleCustomers_Success(self):
        """TestCase:getValidTN_MultipleCustomers_Success"""
        self.testId = "cis_test_007_Success"
        uri = configs.config.CISEndpoint
        response = requests.get(uri)
        self.response = response
        f = open('workfile', 'w')
        pickle.dump(response.content, f)
        f.close()
        self.assertEqual(response[1]['tnType'], 'UNKNOWN')
        self.assertEqual(len(response[0]), 2)   
        
    def testValidTN_MultipleCustomers_Failure(self):
        """TestCase:getValidTN_MultipleCustomers_Failure"""
        self.testId = "cis_test_007_Failure"
        uri = configs.config.CISEndpoint
        response = requests.get(uri)
        self.response = response
        f = open('workfile', 'w')
        pickle.dump(response.content, f)
        f.close()
        self.assertFalse(len(response[0]), 1)  
        
if __name__ == '__main__':
    #del sys.argv[1:]
    #print sys.argv[1]
    unittest.main()
