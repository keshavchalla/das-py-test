import unittest
import requests
import logging
import time
import pickle
import sys
import configs.config

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
        uri = configs.config.CISEndpoint + "6105555551"
        response = requests.get(uri)
        data = response.json()
        self.response = response
        f = open('workfile', 'w')
        pickle.dump(data, f)
        f.close()
        self.assertEqual(data[1]['tnType'], 'UNKNOWN')
        self.assertEqual((len(data[0])), 2)
        self.assertEqual((len(data)), 6)
        
    def testValidTN_MultipleCustomers_Failure(self):
        """TestCase:getValidTN_MultipleCustomers_Failure"""
        self.testId = "cis_test_007_Failure"
        uri = configs.config.CISEndpoint + "6105555551"
        response = requests.get(uri)
        data = response.json()
        self.response = response
        f = open('workfile', 'w')
        pickle.dump(data, f)
        f.close()
        self.assertNotEquals((len(data)), 4)
    
    def testValidTN_SingleCustomerCSG_Success(self):
        """TestCase:getValidTN_MultipleCustomers_Success"""
        self.testId = "cis_test_006_Success"
        uri = configs.config.CISEndpoint + "3860137486"
        response = requests.get(uri)
        data = response.json()
        self.response = response
        f = open('workfile', 'w')
        pickle.dump(data, f)
        f.close()
        self.assertTrue(data[0]['tnType'], 'UNKNOWN')
        self.assertEqual(len(data[0]['accountNumber']), 16)
        
    def testValidTN_SingleCustomerCSG_Failure(self):
        """TestCase:getValidTN_MultipleCustomers_Failure"""
        self.testId = "cis_test_006_Failure"
        uri = configs.config.CISEndpoint + "3860137486"
        response = requests.get(uri)
        data = response.json()
        self.response = response
        f = open('workfile', 'w')
        pickle.dump(data, f)
        f.close()
        self.assertNotEqual((len(data)), 2)
    
    def testValidTN_SingleCustomerDDP_Success(self):
        """TestCase:getValidTN_MultipleCustomers_Success"""
        self.testId = "cis_test_009_Success"
        uri = configs.config.CISEndpoint
        response = requests.get(uri)
        data = response.json()
        self.response = response
        f = open('workfile', 'w')
        pickle.dump(data, f)
        f.close()
        self.assertEqual(response.status_code, 404)

        
    def testValidTN_SingleCustomerDDP_Failure(self):
        """TestCase:getValidTN_MultipleCustomers_Failure"""
        self.testId = "cis_test_009_Failure"
        uri = configs.config.CISEndpoint
        response = requests.get(uri)
        data = response.json()
        self.response = response
        f = open('workfile', 'w')
        pickle.dump(data, f)
        f.close()
        self.assertNotEquals(response.status_code, 500)
        
    def testInvalidTN_Length_Success(self):
        """TestCase:getValidTN_MultipleCustomers_Success"""
        self.testId = "cis_test_017_Success"
        uri = configs.config.CISEndpoint + "233"
        response = requests.get(uri)
        data = response.json()
        self.response = response
        f = open('workfile', 'w')
        pickle.dump(data, f)
        f.close()
        print response.status_code
        self.assertEqual(response.status_code, 500)
        #self.assertEqual(len(data[0][0]), 16)   
        
    def testInvalidTN_Length_Failure(self):
        """TestCase:getValidTN_MultipleCustomers_Failure"""
        self.testId = "cis_test_017_Failure"
        uri = configs.config.CISEndpoint + "233"
        response = requests.get(uri)
        data = response.json()
        self.response = response
        f = open('workfile', 'w')
        pickle.dump(data, f)
        f.close()
        self.assertNotEquals(response.status_code, 200)
           
if __name__ == '__main__':
    #del sys.argv[1:]
    #print sys.argv[1]
    unittest.main()
