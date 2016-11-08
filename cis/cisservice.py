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
        
    def testValidTN_CISService_NotDeployed_Success(self):
        """TestCase:getValidTN_CISService_NotDeployed_Success"""
        self.testId = "cis_test_001_Success"
        uri = configs.config.CISEndpoint + "4756412378"
        response = requests.get(uri)
        data = response.json()
        self.response = response
        f = open('workfile', 'w')
        pickle.dump(data, f)
        f.close()
        print response.status_code
        self.assertEqual(response.status_code, 404)
        
    def testValidTN_CISService_NotDeployed_Failure(self):
        """TestCase:getValidTN_CISService_NotDeployed_Failure"""
        self.testId = "cis_test_001_Failure"
        uri = configs.config.CISEndpoint + "1875641237"
        response = requests.get(uri)
        data = response.json()
        self.response = response
        f = open('workfile', 'w')
        pickle.dump(data, f)
        f.close()
        self.assertNotEquals(response.status_code, 200)
    
    def testValidTN_CISService_InvalidPathParameter_Success(self):
        """TestCase:getValidTN_CISService_InvalidPathParameter_Success"""
        self.testId = "cis_test_003_Success"
        uri = configs.config.CISEndpoint + "47562.2378"
        response = requests.get(uri)
        data = response.json()
        self.response = response
        f = open('workfile', 'w')
        pickle.dump(data, f)
        f.close()
        print response.status_code
        self.assertEqual(response.status_code, 404)
        
    def testValidTN_CISService_InvalidPathParameter_Failure(self):
        """TestCase:getValidTN_CISService_InvalidPathParameter_Failure"""
        self.testId = "cis_test_003_Failure"
        uri = configs.config.CISEndpoint + "18756.41237"
        response = requests.get(uri)
        data = response.json()
        self.response = response
        f = open('workfile', 'w')
        pickle.dump(data, f)
        f.close()
        self.assertNotEquals(response.status_code, 200)
        
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
        
    def testValidTN_MultipleCustomers_CSG_Success(self):
        """TestCase:getValidTN_MultipleCustomers_CSG_Success"""
        self.testId = "cis_test_008_Success"
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
        
    def testValidTN_MultipleCustomers_CSG_Failure(self):
        """TestCase:getValidTN_MultipleCustomers_CSG_Failure"""
        self.testId = "cis_test_008_Failure"
        uri = configs.config.CISEndpoint + "6105555551"
        response = requests.get(uri)
        data = response.json()
        self.response = response
        f = open('workfile', 'w')
        pickle.dump(data, f)
        f.close()
        self.assertNotEquals((len(data)), 4)
    
    def testValidTN_SingleCustomerDDP_Success(self):
        """TestCase:getValidTN_SingleCustomerDDP_Success"""
        self.testId = "cis_test_009_Success"
        uri = configs.config.CISEndpoint + "" #Test data required
        response = requests.get(uri)
        data = response.json()
        self.response = response
        f = open('workfile', 'w')
        pickle.dump(data, f)
        f.close()
        self.assertEqual(response.status_code, 404)

    def testValidTN_SingleCustomerDDP_Failure(self):
        """TestCase:getValidTN_SingleCustomerDDP_Failure"""
        self.testId = "cis_test_009_Failure"
        uri = configs.config.CISEndpoint + "" #Test data required
        response = requests.get(uri)
        data = response.json()
        self.response = response
        f = open('workfile', 'w')
        pickle.dump(data, f)
        f.close()
        self.assertNotEquals(response.status_code, 500)
        
    def testValidTN_MultipleCustomers_DDP_Success(self):
        """TestCase:getValidTN_MultipleCustomers_DDP_Success"""
        self.testId = "cis_test_010_Success"
        uri = configs.config.CISEndpoint + "8985434231"
        response = requests.get(uri)
        data = response.json()
        self.response = response
        f = open('workfile', 'w')
        pickle.dump(data, f)
        f.close()
        self.assertEqual(data[1]['tnType'], 'UNKNOWN')
        self.assertEqual((len(data[0]['account'])), 13)
        self.assertEqual((len(data)), 6)
        
    def testValidTN_MultipleCustomers_DDP_Failure(self):
        """TestCase:getValidTN_MultipleCustomers_DDP_Failure"""
        self.testId = "cis_test_010_Failure"
        uri = configs.config.CISEndpoint + "8985434231"
        response = requests.get(uri)
        data = response.json()
        self.response = response
        f = open('workfile', 'w')
        pickle.dump(data, f)
        f.close()
        self.assertNotEquals((len(data)), 4)
        
    def testValidTN_MultipleCustomers_Combination_Success(self):
        """TestCase:getValidTN_MultipleCustomers_Combination_Success"""
        self.testId = "cis_test_011_Success"
        uri = configs.config.CISEndpoint + "" #Test data required
        response = requests.get(uri)
        data = response.json()
        self.response = response
        f = open('workfile', 'w')
        pickle.dump(data, f)
        f.close()
        self.assertEqual(data[1]['tnType'], 'UNKNOWN')
        self.assertEqual((len(data[0])), 2)
        self.assertEqual((len(data)), 6)
        
    def testValidTN_MultipleCustomers_Combination_Failure(self):
        """TestCase:getValidTN_MultipleCustomers_Combination_Failure"""
        self.testId = "cis_test_011_Failure"
        uri = configs.config.CISEndpoint + "" #Test data required
        response = requests.get(uri)
        data = response.json()
        self.response = response
        f = open('workfile', 'w')
        pickle.dump(data, f)
        f.close()
        self.assertNotEquals((len(data)), 4)
        
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
    
    def testInValidTN_AlphaNumeric_Success(self):
        """TestCase:getInValidTN_AlphaNumeric_Success"""
        self.testId = "cis_test_0018_Success"
        uri = configs.config.CISEndpoint + "47562a2378"
        response = requests.get(uri)
        data = response.json()
        self.response = response
        f = open('workfile', 'w')
        pickle.dump(data, f)
        f.close()
        print response.status_code
        self.assertEqual(response.status_code, 404)
        
    def testInValidTN_AlphaNumeric_Failure(self):
        """TestCase:getInValidTN_AlphaNumeric_Failure"""
        self.testId = "cis_test_0018_Failure"
        uri = configs.config.CISEndpoint + "18756a41237"
        response = requests.get(uri)
        data = response.json()
        self.response = response
        f = open('workfile', 'w')
        pickle.dump(data, f)
        f.close()
        self.assertNotEquals(response.status_code, 200)
        
    def testInvalidTN_NPA_Success(self):
        """TestCase:getValidTN_MultipleCustomers_Success"""
        self.testId = "cis_test_019_Success"
        uri = configs.config.CISEndpoint + "1875641237"
        response = requests.get(uri)
        data = response.json()
        self.response = response
        f = open('workfile', 'w')
        pickle.dump(data, f)
        f.close()
        print response.status_code
        self.assertEqual(response.status_code, 404)
        
    def testInvalidTN_NPA_Failure(self):
        """TestCase:getValidTN_MultipleCustomers_Failure"""
        self.testId = "cis_test_019_Failure"
        uri = configs.config.CISEndpoint + "1875641237"
        response = requests.get(uri)
        data = response.json()
        self.response = response
        f = open('workfile', 'w')
        pickle.dump(data, f)
        f.close()
        self.assertNotEquals(response.status_code, 200)    
    def testInvalidTN_NXX_Success(self):
        """TestCase:InvalidTN_NXX_Success"""
        self.testId = "cis_test_020_Success"
        uri = configs.config.CISEndpoint + "8870641237"
        response = requests.get(uri)
        data = response.json()
        self.response = response
        f = open('workfile', 'w')
        pickle.dump(data, f)
        f.close()
        print response.status_code
        self.assertEqual(response.status_code, 500)
        #self.assertEqual(len(data[0][0]), 16)   
        
    def testInvalidTN_NXX_Failure(self):
        """TestCase:InvalidTN_NXX_Failure"""
        self.testId = "cis_test_020_Failure"
        uri = configs.config.CISEndpoint + "8870641237"
        response = requests.get(uri)
        data = response.json()
        self.response = response
        f = open('workfile', 'w')
        pickle.dump(data, f)
        f.close()
        self.assertNotEquals(response.status_code, 200)
        
    def testInvalidTN_NXX_N11_Success(self):
        """TestCase:InvalidTN_NXX_N11_Success"""
        self.testId = "cis_test_021_Success"
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
        
    def testInvalidTN_NXX_N11s_Failure(self):
        """TestCase:InvalidTN_NXX_N11_Failure"""
        self.testId = "cis_test_021_Failure"
        uri = configs.config.CISEndpoint + "233"
        response = requests.get(uri)
        data = response.json()
        self.response = response
        f = open('workfile', 'w')
        pickle.dump(data, f)
        f.close()
        self.assertNotEquals(response.status_code, 200)
        
    def testInvalidTN_NXX_555_Success(self):
        """TestCase:InvalidTN_NXX_555_Success"""
        self.testId = "cis_test_022_Success"
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
        
    def testInvalidTN_NXX_555_Failure(self):
        """TestCase:InvalidTN_NXX_555_Failure"""
        self.testId = "cis_test_022_Failure"
        uri = configs.config.CISEndpoint + "233"
        response = requests.get(uri)
        data = response.json()
        self.response = response
        f = open('workfile', 'w')
        pickle.dump(data, f)
        f.close()
        self.assertNotEquals(response.status_code, 200)
        
    def testInValidTN_Identical_Success(self):
        """TestCase:InValidTN_Identical_Success"""
        self.testId = "cis_test_023_Success"
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
        
    def testInValidTN_Identical_Failure(self):
        """TestCase:InValidTN_Identical_Failure"""
        self.testId = "cis_test_023_Failure"
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
