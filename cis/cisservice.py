import unittest
import requests
import logging
import pickle
import sys
import configs.config


class CISService(unittest.TestCase):
    def __init__(self, testName, *args):
        super(CISService, self).__init__(testName)
        self.cisEndpoint = configs.config.Cust
        logging.basicConfig(filename="cis.log", level=logging.DEBUG)
        sys.stdout = open('finaltestresult', 'w')

    def setUp(self):
        logging.debug("Validating: %s" % self._testMethodName)
        logging.debug("Validating: %s" % self.cisEndpoint)

    def tearDown(self):
        logging.debug(" Request:%s" % self.cisEndpoint)
        logging.debug(" Response:%s" % self.response)

    def writeResponseToFile(self, output):
        self.response = output
        f = open('workfile', 'w')
        pickle.dump(output, f)
        f.close()

    def printOutput(self, testId, testName, output):
        print '------------------------------------------------------------------------------------------------------------------------------------------------------'
        print 'Test Case Id : ' + testId
        print 'Test Name : ' + testName
        print 'Input : ' + self.cisEndpoint
        print 'Output :'
        print  output
        print '------------------------------------------------------------------------------------------------------------------------------------------------------'

    def testValidTN_CISService_NotDeployed_Success(self):
        """TestCase:getValidTN_CISService_NotDeployed_Success"""
        self.testId = "cis_test_001_Success"
        uri = configs.config.CISEndpoint + "4756412378"
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_CISService_NotDeployed_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_001_Success", "testValidTN_CISService_NotDeployed_Success", output)
#         self.assertEqual(response.status_code, 404)
# 
#     def testValidTN_CISService_NotDeployed_Failure(self):
#         """TestCase:getValidTN_CISService_NotDeployed_Failure"""
#         self.testId = "cis_test_001_Failure"
#         uri = configs.config.CISEndpoint + "1875641237"
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_CISService_NotDeployed_Failure")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_001_Failure", "testValidTN_CISService_NotDeployed_Failure", output)
#         self.assertNotEquals(response.status_code, 200)
#         
#     def testValidTN_CISService_NotAvailable_Success(self):
#         """TestCase:getValidTN_CISService_NotAvailable_Success"""
#         self.testId = "cis_test_002_Success"
#         uri = configs.config.CISEndpoint + "4756412378"
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_CISService_NotAvailable_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_002_Success", "testValidTN_CISService_NotAvailable_Success", output)
#         self.assertEqual(response.status_code, 404)
# 
#     def testValidTN_CISService_NotAvailable_Failure(self):
#         """TestCase:getValidTN_CISService_NotAvailable_Failure"""
#         self.testId = "cis_test_002_Failure"
#         uri = configs.config.CISEndpoint + "1875641237"
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_CISService_NotAvailable_Failure")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_002_Failure", "testValidTN_CISService_NotAvailable_Failure", output)
#         self.assertNotEquals(response.status_code, 200)
# 
#     def testValidTN_CISService_InvalidPathParameter_Success(self):
#         """TestCase:getValidTN_CISService_InvalidPathParameter_Success"""
#         self.testId = "cis_test_003_Success"
#         uri = configs.config.CISEndpoint + "47562.2378"
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_CISService_InvalidPathParameter_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_003_Success", "testValidTN_CISService_InvalidPathParameter_Success", output)
#         self.assertEqual(response.status_code, 404)
# 
#     def testValidTN_CISService_InvalidPathParameter_Failure(self):
#         """TestCase:getValidTN_CISService_InvalidPathParameter_Failure"""
#         self.testId = "cis_test_003_Failure"
#         uri = configs.config.CISEndpoint + "18756.41237"
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_CISService_InvalidPathParameter_Failure")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_003_Failure", "testValidTN_CISService_InvalidPathParameter_Failure", output)
#         self.assertNotEquals(response.status_code, 200)
#         
#     def testAuthentication_Success(self):
#         """TestCase:getAuthentication_Success"""
#         self.testId = "cis_test_004_Success"
#         uri = configs.config.CISEndpoint + "4756412378"
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testAuthentication_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_004_Success", "testAuthentication_Success", output)
#         self.assertEqual(response.status_code, 404)
# 
#     def testAuthentication_Failure(self):
#         """TestCase:getAuthentication_Failure"""
#         self.testId = "cis_test_005_Failure"
#         uri = configs.config.CISEndpoint + "1875641237"
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testAuthentication_Failure")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_005_Failure", "testAuthentication_Failure", output)
#         self.assertNotEquals(response.status_code, 200)
# 
# 
#     def testValidTN_SingleCustomerCSG_Success(self):
#         """TestCase:getValidTN_SingleCustomerCSG_Success"""
#         self.testId = "cis_test_006_Success"
#         uri = configs.config.Cust  # + "3860137486"
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertEqual((len(output[0])), 2)
#         self.assertEqual(len(output[0]['accountNumber']), 16)
#         self.assertTrue(output[0]['tnType'], 'UNKNOWN')
# 
#     def testValidTN_SingleCustomerCSG_Failure(self):
#         """TestCase:getValidTN_SingleCustomerCSG_Failure"""
#         self.testId = "cis_test_006_Failure"
#         uri = configs.config.CISEndpoint + "3860137486"
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Failure")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Failure", "testValidTN_SingleCustomerCSG_Failure", output)
#         self.assertNotEqual((len(output)), 2)
# 
#     def testValidTN_MultipleCustomers_Success(self):
#         """TestCase:getValidTN_MultipleCustomers_Success"""
#         self.testId = "cis_test_007_Success"
#         uri = configs.config.CISEndpoint + "6105555551"
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_MultipleCustomers_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_007_Success", "testValidTN_MultipleCustomers_Success", output)
#         self.assertEqual(output[1]['tnType'], 'UNKNOWN')
#         self.assertEqual((len(output[0])), 2)
#         self.assertEqual((len(output)), 6)
# 
#     def testValidTN_MultipleCustomers_Failure(self):
#         """TestCase:getValidTN_MultipleCustomers_Failure"""
#         self.testId = "cis_test_007_Failure"
#         uri = configs.config.CISEndpoint + "6105555551"
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_MultipleCustomers_Failure")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_007_Failure", "testValidTN_MultipleCustomers_Failure", output)
#         self.assertNotEquals((len(output)), 4)
# 
#     def testValidTN_MultipleCustomers_CSG_Success(self):
#         """TestCase:getValidTN_MultipleCustomers_CSG_Success"""
#         self.testId = "cis_test_008_Success"
#         uri = configs.config.CISEndpoint + "6105555551"
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_MultipleCustomers_CSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_008_Success", "testValidTN_MultipleCustomers_CSG_Success", output)
#         self.assertEqual(output[1]['tnType'], 'UNKNOWN')
#         self.assertEqual((len(output[0])), 2)
#         self.assertEqual((len(output)), 6)
# 
#     def testValidTN_MultipleCustomers_CSG_Failure(self):
#         """TestCase:getValidTN_MultipleCustomers_CSG_Failure"""
#         self.testId = "cis_test_008_Failure"
#         uri = configs.config.CISEndpoint + "6105555551"
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_MultipleCustomers_CSG_Failure")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_008_Failure", "testValidTN_MultipleCustomers_CSG_Failure", output)
#         self.assertNotEquals((len(output)), 4)
# 
#     def testValidTN_SingleCustomerDDP_Success(self):
#         """TestCase:getValidTN_SingleCustomerDDP_Success"""
#         self.testId = "cis_test_009_Success"
#         uri = configs.config.CISEndpoint + ""  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerDDP_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_009_Success", "testValidTN_SingleCustomerDDP_Success", output)
#         self.assertEqual(response.status_code, 404)
# 
#     def testValidTN_SingleCustomerDDP_Failure(self):
#         """TestCase:getValidTN_SingleCustomerDDP_Failure"""
#         self.testId = "cis_test_009_Failure"
#         uri = configs.config.CISEndpoint + ""  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerDDP_Failure")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_009_Failure", "testValidTN_SingleCustomerDDP_Failure", output)
#         self.assertNotEquals(response.status_code, 500)
# 
#     def testValidTN_MultipleCustomers_DDP_Success(self):
#         """TestCase:getValidTN_MultipleCustomers_DDP_Success"""
#         self.testId = "cis_test_010_Success"
#         uri = configs.config.CISEndpoint + "8985434231"
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_MultipleCustomers_DDP_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_010_Success", "testValidTN_MultipleCustomers_DDP_Success", output)
#         self.assertEqual(output[1]['tnType'], 'UNKNOWN')
#         self.assertEqual((len(output[0]['account'])), 13)
#         self.assertEqual((len(output)), 6)
#         #
# 
#     def testValidTN_MultipleCustomers_DDP_Failure(self):
#         """TestCase:getValidTN_MultipleCustomers_DDP_Failure"""
#         self.testId = "cis_test_010_Failure"
#         uri = configs.config.CISEndpoint + "8985434231"
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_MultipleCustomers_DDP_Failure")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_010_Failure", "testValidTN_MultipleCustomers_DDP_Failure", output)
#         self.assertNotEquals((len(output)), 4)
# 
#     def testValidTN_MultipleCustomers_Combination_Success(self):
#         """TestCase:getValidTN_MultipleCustomers_Combination_Success"""
#         self.testId = "cis_test_011_Success"
#         uri = configs.config.CISEndpoint + ""  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_MultipleCustomers_Combination_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_011_Success", "testValidTN_MultipleCustomers_Combination_Success", output)
#         self.assertEqual(output[1]['tnType'], 'UNKNOWN')
#         self.assertEqual((len(output[0])), 2)
#         self.assertEqual((len(output)), 6)
# 
#     def testValidTN_MultipleCustomers_Combination_Failure(self):
#         """TestCase:getValidTN_MultipleCustomers_Combination_Failure"""
#         self.testId = "cis_test_011_Failure"
#         uri = configs.config.CISEndpoint + ""  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_MultipleCustomers_Combination_Failure")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_011_Failure", "testValidTN_MultipleCustomers_Combination_Failure", output)
#         self.assertNotEquals((len(output)), 4)
# 
#     def testValidTN_NoDataInGSA_Success(self):
#         """TestCase:getValidTN_NoDataInGSA_Success"""
#         self.testId = "cis_test_012_Success"
#         uri = configs.config.CISEndpoint + ""  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_NoDataInGSA_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_012_Success", "testValidTN_NoDataInGSA_Success", output)
#         self.assertEqual(output[1]['tnType'], 'UNKNOWN')
#         self.assertEqual((len(output[0])), 2)
#         self.assertEqual((len(output)), 6)
# 
#     def testValidTN_NoDataInGSA_Failure(self):
#         """TestCase:getValidTN_NoDataInGSA_Failure"""
#         self.testId = "cis_test_012_Failure"
#         uri = configs.config.CISEndpoint + ""  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_NoDataInGSA_Failure")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_012_Failure", "testValidTN_NoDataInGSA_Failure", output)
#         self.assertNotEquals((len(output)), 4)
#         
#     def testValidTN_CIS_Timeout_Success(self):
#         """TestCase:getValidTN_CIS_Timeout_Success"""
#         self.testId = "cis_test_013_Success"
#         uri = configs.config.CISEndpoint + ""  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_CIS_Timeout_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_013_Success", "testValidTN_CIS_Timeout_Success", output)
#         self.assertEqual(output[1]['tnType'], 'UNKNOWN')
#         self.assertEqual((len(output[0])), 2)
#         self.assertEqual((len(output)), 6)
# 
#     def testValidTN_CIS_Timeout_Failure(self):
#         """TestCase:getValidTN_CIS_Timeout_Failure"""
#         self.testId = "cis_test_013_Failure"
#         uri = configs.config.CISEndpoint + ""  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertNotEquals((len(output)), 4)
# 
#     def testValidTN_CIS_Exception_Success(self):
#         """TestCase:getValidTN_CIS_Exception_Success"""
#         self.testId = "cis_test_014_Success"
#         uri = configs.config.CISEndpoint + ""  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertEqual(output[1]['tnType'], 'UNKNOWN')
#         self.assertEqual((len(output[0])), 2)
#         self.assertEqual((len(output)), 6)
# 
#     def testValidTN_CIS_Exception_Failure(self):
#         """TestCase:getValidTN_CIS_Exception_Failure"""
#         self.testId = "cis_test_014_Failure"
#         uri = configs.config.CISEndpoint + ""  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertNotEquals((len(output)), 4)
# 
#     def testValidTN_GSA_Timeout_Success(self):
#         """TestCase:getValidTN_GSA_Timeout_Success"""
#         self.testId = "cis_test_015_Success"
#         uri = configs.config.CISEndpoint + ""  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_GSA_Timeout_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_015_Failure", "testValidTN_GSA_Timeout_Success", output)
#         self.assertEqual(output[1]['tnType'], 'UNKNOWN')
#         self.assertEqual((len(output[0])), 2)
#         self.assertEqual((len(output)), 6)
# 
#     def testValidTN_GSA_Timeout_Failure(self):
#         """TestCase:getValidTN_GSA_Timeout_Failure"""
#         self.testId = "cis_test_015_Failure"
#         uri = configs.config.CISEndpoint + ""  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_GSA_Timeout_Failure")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_015_Failure", "testValidTN_GSA_Timeout_Failure", output)
#         self.assertNotEquals((len(output)), 4)
# 
#     def testValidTN_GSA_Exception_Success(self):
#         """TestCase:getValidTN_GSA_Exception_Success"""
#         self.testId = "cis_test_016_Success"
#         uri = configs.config.CISEndpoint + ""  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_GSA_Exception_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_016_Success", "testValidTN_GSA_Exception_Success", output)
#         self.assertEqual(output[1]['tnType'], 'UNKNOWN')
#         self.assertEqual((len(output[0])), 2)
#         self.assertEqual((len(output)), 6)
# 
#     def testValidTN_GSA_Exception_Failure(self):
#         """TestCase:getValidTN_GSA_Exception_Failure"""
#         self.testId = "cis_test_016_Failure"
#         uri = configs.config.CISEndpoint + ""  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_GSA_Exception_Failure")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_016_Failure", "testValidTN_GSA_Exception_Failure", output)
#         self.assertNotEquals((len(output)), 4)
# 
#     def testInvalidTN_Length_Success(self):
#         """TestCase:getValidTN_MultipleCustomers_Success"""
#         self.testId = "cis_test_017_Success"
#         uri = configs.config.CISEndpoint + "233"
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         print response.status_code
#         self.assertEqual(response.status_code, 500)
#         # self.assertEqual(len(output[0][0]), 16)
# 
#     def testInvalidTN_Length_Failure(self):
#         """TestCase:getValidTN_MultipleCustomers_Failure"""
#         self.testId = "cis_test_017_Failure"
#         uri = configs.config.CISEndpoint + "233"
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertNotEquals(response.status_code, 200)
# 
#     def testInValidTN_AlphaNumeric_Success(self):
#         """TestCase:getInValidTN_AlphaNumeric_Success"""
#         self.testId = "cis_test_0018_Success"
#         uri = configs.config.CISEndpoint + "47562a2378"
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         print response.status_code
#         self.assertEqual(response.status_code, 404)
# 
#     def testInValidTN_AlphaNumeric_Failure(self):
#         """TestCase:getInValidTN_AlphaNumeric_Failure"""
#         self.testId = "cis_test_0018_Failure"
#         uri = configs.config.CISEndpoint + "18756a41237"
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertNotEquals(response.status_code, 200)
# 
#     def testInvalidTN_NPA_Success(self):
#         """TestCase:getValidTN_MultipleCustomers_Success"""
#         self.testId = "cis_test_019_Success"
#         uri = configs.config.CISEndpoint + "1875641237"
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         print response.status_code
#         self.assertEqual(response.status_code, 404)
# 
#     def testInvalidTN_NPA_Failure(self):
#         """TestCase:getValidTN_MultipleCustomers_Failure"""
#         self.testId = "cis_test_019_Failure"
#         uri = configs.config.CISEndpoint + "1875641237"
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertNotEquals(response.status_code, 200)
# 
#     def testInvalidTN_NXX_Success(self):
#         """TestCase:InvalidTN_NXX_Success"""
#         self.testId = "cis_test_020_Success"
#         uri = configs.config.CISEndpoint + "8870641237"
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         print response.status_code
#         self.assertEqual(response.status_code, 500)
#         # self.assertEqual(len(output[0][0]), 16)
# 
#     def testInvalidTN_NXX_Failure(self):
#         """TestCase:InvalidTN_NXX_Failure"""
#         self.testId = "cis_test_020_Failure"
#         uri = configs.config.CISEndpoint + "8870641237"
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertNotEquals(response.status_code, 200)
# 
#     def testInvalidTN_NXX_N11_Success(self):
#         """TestCase:InvalidTN_NXX_N11_Success"""
#         self.testId = "cis_test_021_Success"
#         uri = configs.config.CISEndpoint + "233"
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         print response.status_code
#         self.assertEqual(response.status_code, 500)
#         # self.assertEqual(len(output[0][0]), 16)
# 
#     def testInvalidTN_NXX_N11s_Failure(self):
#         """TestCase:InvalidTN_NXX_N11_Failure"""
#         self.testId = "cis_test_021_Failure"
#         uri = configs.config.CISEndpoint + "233"
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertNotEquals(response.status_code, 200)
# 
#     def testInvalidTN_NXX_555_Success(self):
#         """TestCase:InvalidTN_NXX_555_Success"""
#         self.testId = "cis_test_022_Success"
#         uri = configs.config.CISEndpoint + "233"
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         print response.status_code
#         self.assertEqual(response.status_code, 500)
#         # self.assertEqual(len(output[0][0]), 16)
# 
#     def testInvalidTN_NXX_555_Failure(self):
#         """TestCase:InvalidTN_NXX_555_Failure"""
#         self.testId = "cis_test_022_Failure"
#         uri = configs.config.CISEndpoint + "233"
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertNotEquals(response.status_code, 200)
# 
#     def testInValidTN_Identical_Success(self):
#         """TestCase:InValidTN_Identical_Success"""
#         self.testId = "cis_test_023_Success"
#         uri = configs.config.CISEndpoint + "233"
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         print response.status_code
#         self.assertEqual(response.status_code, 500)
#         # self.assertEqual(len(output[0][0]), 16)
# 
#     def testInValidTN_Identical_Failure(self):
#         """TestCase:InValidTN_Identical_Failure"""
#         self.testId = "cis_test_023_Failure"
#         uri = configs.config.CISEndpoint + "233"
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertNotEquals(response.status_code, 200)
#     def testValidTN_NoDataIn_Attroute_Success(self):
#         """TestCase:getValidTN_NoDataIn_Attroute_Success"""
#         self.testId = "cis_test_024_Success"
#         uri = configs.config.CISEndpoint + ""  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertTrue(output[0]['tnType'], 'ALTERNATE')
#         self.assertEqual(len(output[0]['accountNumber']), 16)
#     
#     def testValidTN_NoDataIn_Attroute_Failure(self):
#         """TestCase:getValidTN_NoDataIn_Attroute_Failure"""
#         self.testId = "cis_test_024_Failure"
#         uri = configs.config.CISEndpoint + " "  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertNotEqual((len(output)), 2)
#     
#     def testValidTN_SingleCustomer_CSG_Attroute_CDV_Primary_Success(self):
#         """TestCase:getValidTN_SingleCustomer_CSG_Attroute_CDV_Primary_Success"""
#         self.testId = "cis_test_025_Success"
#         uri = configs.config.CISEndpoint + ""  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertTrue(output[0]['tnType'], 'ALTERNATE')
#         self.assertEqual(len(output[0]['accountNumber']), 16)
#     
#     def testValidTN_SingleCustomer_CSG_Attroute_CDV_Primary_Failure(self):
#         """TestCase:getValidTN_SingleCustomer_CSG_Attroute_CDV_Primary_Failure"""
#         self.testId = "cis_test_025_Failure"
#         uri = configs.config.CISEndpoint + " "  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertNotEqual((len(output)), 2)
#     
#     def testValidTN_MultipleCustomers_Attroute_CDV_Primary_Success(self):
#         """TestCase:getValidTN_MultipleCustomers_Attroute_CDV_Primary_Success"""
#         self.testId = "cis_test_026_Success"
#         uri = configs.config.CISEndpoint + ""  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertTrue(output[0]['tnType'], 'ALTERNATE')
#         self.assertEqual(len(output[0]['accountNumber']), 16)
#     
#     
#     def testValidTN_MultipleCustomers_Attroute_CDV_Primary_Failure(self):
#         """TestCase:getValidTN_MultipleCustomers_Attroute_CDV_Primary_Failure"""
#         self.testId = "cis_test_026_Failure"
#         uri = configs.config.CISEndpoint + " "  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertNotEqual((len(output)), 2)
#     
#     def testValidTN_MultipleCustomers_CSG_Attroute_CDV_Primary_Success(self):
#         """TestCase:getValidTN_MultipleCustomers_CSG_Attroute_CDV_Primary_Success"""
#         self.testId = "cis_test_027_Success"
#         uri = configs.config.CISEndpoint + ""  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertTrue(output[0]['tnType'], 'ALTERNATE')
#         self.assertEqual(len(output[0]['accountNumber']), 16)
#     
#     
#     def testValidTN_MultipleCustomers_CSG_Attroute_CDV_Primary_Failure(self):
#         """TestCase:getValidTN_MultipleCustomers_CSG_Attroute_CDV_Primary_Failure"""
#         self.testId = "cis_test_027_Failure"
#         uri = configs.config.CISEndpoint + " "  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertNotEqual((len(output)), 2)
#     
#     def testValidTN_SingleCustomer_DDP_Attroute_CDV_Primary_Success(self):
#         """TestCase:getValidTN_SingleCustomer_DDP_Attroute_CDV_Primary_Success"""
#         self.testId = "cis_test_028_Success"
#         uri = configs.config.CISEndpoint + ""  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertTrue(output[0]['tnType'], 'ALTERNATE')
#         self.assertEqual(len(output[0]['accountNumber']), 16)
#     
#     
#     def testValidTN_SingleCustomer_DDP_Attroute_CDV_Primary_Failure(self):
#         """TestCase:getValidTN_SingleCustomer_DDP_Attroute_CDV_Primary_Failure"""
#         self.testId = "cis_test_028_Failure"
#         uri = configs.config.CISEndpoint + " "  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertNotEqual((len(output)), 2)
#     
#     def testValidTN_MultipleCustomers_DDP_Attroute_CDV_Primary_Success(self):
#         """TestCase:getValidTN_MultipleCustomers_DDP_Attroute_CDV_Primary_Success"""
#         self.testId = "cis_test_029_Success"
#         uri = configs.config.CISEndpoint + ""  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertTrue(output[0]['tnType'], 'ALTERNATE')
#         self.assertEqual(len(output[0]['accountNumber']), 16)
#     
#     
#     def testValidTN_MultipleCustomers_DDP_Attroute_CDV_Primary_Failure(self):
#         """TestCase:getValidTN_MultipleCustomers_DDP_Attroute_CDV_Primary_Failure"""
#         self.testId = "cis_test_029_Failure"
#         uri = configs.config.CISEndpoint + " "  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertNotEqual((len(output)), 2)
#     
#     def testValidTN_MultipleCustomers_Combination_Attroute_CDV_Primary_Success(self):
#         """TestCase:getValidTN_MultipleCustomers_Combination_Attroute_CDV_Primary_Success"""
#         self.testId = "cis_test_030_Success"
#         uri = configs.config.CISEndpoint + ""  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertTrue(output[0]['tnType'], 'ALTERNATE')
#         self.assertEqual(len(output[0]['accountNumber']), 16)
#     
#     def testValidTN_MultipleCustomers_Combination_Attroute_CDV_Primary_Failure(self):
#         """TestCase:getValidTN_MultipleCustomers_Combination_Attroute_CDV_Primary_Failure"""
#         self.testId = "cis_test_030_Failure"
#         uri = configs.config.CISEndpoint + " "  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertNotEqual((len(output)), 2)
#     
#     def testValidTN_SingleCustomer_CSG_Attroute_CDV_Other_Success(self):
#         """TestCase:getValidTN_SingleCustomer_CSG_Attroute_CDV_Other_Success"""
#         self.testId = "cis_test_031_Success"
#         uri = configs.config.CISEndpoint + ""  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertTrue(output[0]['tnType'], 'ALTERNATE')
#         self.assertEqual(len(output[0]['accountNumber']), 16)
#     
#     
#     def testValidTN_SingleCustomer_CSG_Attroute_CDV_Other_Failure(self):
#         """TestCase:getValidTN_SingleCustomer_CSG_Attroute_CDV_Other_Failure"""
#         self.testId = "cis_test_031_Failure"
#         uri = configs.config.CISEndpoint + " "  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertNotEqual((len(output)), 2)
#     
#     
#     def testValidTN_MultipleCustomers_Attroute_CDV_Other_Success(self):
#         """TestCase:getValidTN_MultipleCustomers_Attroute_CDV_Other_Success"""
#         self.testId = "cis_test_032_Success"
#         uri = configs.config.CISEndpoint + ""  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertTrue(output[0]['tnType'], 'ALTERNATE')
#         self.assertEqual(len(output[0]['accountNumber']), 16)
#     
#     def testValidTN_MultipleCustomers_Attroute_CDV_Other_Failure(self):
#         """TestCase:getValidTN_MultipleCustomers_Attroute_CDV_Other_Failure"""
#         self.testId = "cis_test_032_Failure"
#         uri = configs.config.CISEndpoint + " "  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertNotEqual((len(output)), 2)
#         
#     def testValidTN_MultipleCustomers_CSG_Attroute_CDV_Other_Success(self):
#         """TestCase:getValidTN_MultipleCustomers_CSG_Attroute_CDV_Other_Success"""
#         self.testId = "cis_test_033_Success"
#         uri = configs.config.CISEndpoint + ""  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertTrue(output[0]['tnType'], 'ALTERNATE')
#         self.assertEqual(len(output[0]['accountNumber']), 16)
#     
#     def testValidTN_MultipleCustomers_CSG_Attroute_CDV_Other_Failure(self):
#         """TestCase:getValidTN_MultipleCustomers_CSG_Attroute_CDV_Other_Failure"""
#         self.testId = "cis_test_033_Failure"
#         uri = configs.config.CISEndpoint + " "  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertNotEqual((len(output)), 2)
#     
#     def testValidTN_SingleCustomer_DDP_Attroute_CDV_Other_Success(self):
#         """TestCase:getValidTN_SingleCustomer_DDP_Attroute_CDV_Other_Success"""
#         self.testId = "cis_test_034_Success"
#         uri = configs.config.CISEndpoint + ""  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertTrue(output[0]['tnType'], 'ALTERNATE')
#         self.assertEqual(len(output[0]['accountNumber']), 16)
#     
#     def testValidTN_SingleCustomer_DDP_Attroute_CDV_Other_Failure(self):
#         """TestCase:getValidTN_SingleCustomer_DDP_Attroute_CDV_Other_Failure"""
#         self.testId = "cis_test_034_Failure"
#         uri = configs.config.CISEndpoint + " "  # Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertNotEqual((len(output)), 2)
# 
# 
#     def testValidTN_MultipleCustomers_DDP_AttRoute_CDV_Other_Success(self):
#         """TestCase:getValidTN_MultipleCustomers_DDP_AttRoute_CDV_Other_Success"""
#         self.testId = "cis_test_035_Success"
#         uri = configs.config.CISEndpoint + " " #Test Data required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_MultipleCustomers_DDP_AttRoute_CDV_Other_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_035_Success", "testValidTN_MultipleCustomers_DDP_AttRoute_CDV_Other_Success", output)
#         self.assertEqual(output[1]['tnType'], 'CDV_Other')
#         self.assertEqual((len(output[0]['accountNumber'])), 13)
#         self.assertEqual((len(output)), 6)
#          
#     def testValidTN_MultipleCustomers_DDP_AttRoute_CDV_Other_Failure(self):
#         """TestCase:getValidTN_MultipleCustomers_DDP_AttRoute_CDV_Other_Failure"""
#         self.testId = "cis_test_035_Failure"
#         uri = configs.config.CISEndpoint + " " #Test Data required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_MultipleCustomers_DDP_AttRoute_CDV_Other_Failure")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_035_Failure", "testValidTN_MultipleCustomers_DDP_AttRoute_CDV_Other_Failure", output)
#         self.assertNotEquals((len(output)), 4)
# 
# 
#     #AttRoute
#     def testValidTN_MultipleCustomers_Combination_AttRoute_CDV_Other_Success(self):
#         """TestCase:getValidTN_MultipleCustomers_Combination_AttRoute_CDV_Other_Success"""
#         self.testId = "cis_test_036_Success"
#         uri = configs.config.CISEndpoint + "" #Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_MultipleCustomers_Combination_AttRoute_CDV_Other_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_036_Success", "testValidTN_MultipleCustomers_Combination_AttRoute_CDV_Other_Success", output)
#         self.assertEqual(output[1]['tnType'], 'CDV_Other')
#         self.assertEqual((len(output[0])), 2)
#         self.assertEqual((len(output)), 6)
#          
#     def testValidTN_MultipleCustomers_Combination_AttRoute_CDV_Other_Failure(self):
#         """TestCase:getValidTN_MultipleCustomers_Combination_AttRoute_CDV_Other_Failure"""
#         self.testId = "cis_test_036_Failure"
#         uri = configs.config.CISEndpoint + "" #Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_MultipleCustomers_Combination_AttRoute_CDV_Other_Failure")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_036_Failure", "testValidTN_MultipleCustomers_Combination_AttRoute_CDV_Other_Failure", output)
#         self.assertNotEquals((len(output)), 4)
# 
#     #AttRoute
#     def testValidTN_SingleCustomerCSG_AttRoute_Primary_Success(self):
#         """TestCase:getValidTN_MultipleCustomers_AttRoute_Primary_Success"""
#         self.testId = "cis_test_037_Success"
#         uri = configs.config.CISEndpoint + " " #Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_AttRoute_Primary_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_037_Success", "testValidTN_SingleCustomerCSG_AttRoute_Primary_Success", output)
#         self.assertTrue(output[0]['tnType'], 'PRIMARY')
#         self.assertEqual(len(output[0]['accountNumber']), 16)
#          
#     def testValidTN_SingleCustomerCSG_AttRoute_Primary_Failure(self):
#         """TestCase:getValidTN_MultipleCustomers_AttRoute_Primary_Failure"""
#         self.testId = "cis_test_037_Failure"
#         uri = configs.config.CISEndpoint + "" #Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_AttRoute_Primary_Failure")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_037_Failure", "testValidTN_SingleCustomerCSG_AttRoute_Primary_Failure", output)
#         self.assertNotEqual((len(output)), 2)
#          
# 
#     #AttRoute
#     def testValidTN_MultipleCustomers_AttRoute_Primary_Success(self):
#         """TestCase:getValidTN_MultipleCustomers_AttRoute_Primary_Success"""
#         self.testId = "cis_test_038_Success"
#         uri = configs.config.CISEndpoint + "" #Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_MultipleCustomers_AttRoute_Primary_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_038_Success", "testValidTN_MultipleCustomers_AttRoute_Primary_Success", output)
#         self.assertEqual(output[1]['tnType'], 'PRIMARY')
#         self.assertEqual((len(output[0])), 2)
#         self.assertEqual((len(output)), 6)
#            
#     def testValidTN_MultipleCustomers_AttRoute_Primary_Failure(self):
#         """TestCase:getValidTN_MultipleCustomers_AttRoute_Primary_Failure"""
#         self.testId = "cis_test_038_Failure"
#         uri = configs.config.CISEndpoint + " " #Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_MultipleCustomers_AttRoute_Primary_Failure")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_037_Failure", "testValidTN_MultipleCustomers_AttRoute_Primary_Failure", output)
#         self.assertNotEquals((len(output)), 4)
#  
#     #AttRoute
#     def testValidTN_MultipleCustomers_CSG_AttRoute_Primary_Success(self):
#         """TestCase:getValidTN_MultipleCustomers_CSG_AttRoute_Primary_Success"""
#         self.testId = "cis_test_039_Success"
#         uri = configs.config.CISEndpoint + " " #Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_MultipleCustomers_CSG_AttRoute_Primary_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_039_Success", "testValidTN_MultipleCustomers_CSG_AttRoute_Primary_Success", output)
#         self.assertEqual(output[1]['tnType'], 'PRIMARY')
#         self.assertEqual((len(output[0])), 2)
#         self.assertEqual((len(output)), 6)
#           
#     def testValidTN_MultipleCustomers_CSG_AttRoute_Primary_Failure(self):
#         """TestCase:getValidTN_MultipleCustomers_CSG_AttRoute_Primary_Failure"""
#         self.testId = "cis_test_039_Failure"
#         uri = configs.config.CISEndpoint + " " #Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_MultipleCustomers_CSG_AttRoute_Primary_Failure")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_039_Failure", "testValidTN_MultipleCustomers_CSG_AttRoute_Primary_Failure", output)
#         self.assertNotEquals((len(output)), 4)
# 
# 
#     #AttRoute    
#     def testValidTN_SingleCustomerDDP_AttRoute_Primary_Success(self):
#         """TestCase:getValidTN_SingleCustomerDDP_AttRoute_Primary_Success"""
#         self.testId = "cis_test_040_Success"
#         uri = configs.config.CISEndpoint + "" #Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerDDP_AttRoute_Primary_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_040_Success", "testValidTN_SingleCustomerDDP_AttRoute_Primary_Success", output)
#         self.assertEqual(response.status_code, 404)
#  
#     def testValidTN_SingleCustomerDDP_AttRoute_Primary_Failure(self):
#         """TestCase:getValidTN_SingleCustomerDDP_AttRoute_Primary_Failure"""
#         self.testId = "cis_test_040_Failure"
#         uri = configs.config.CISEndpoint + "" #Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerDDP_AttRoute_Primary_Failure")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_040_Failure", "testValidTN_SingleCustomerDDP_AttRoute_Primary_Failure", output)
#         self.assertNotEquals(response.status_code, 500)
# 
#     #AttRoute
#     def testValidTN_MultipleCustomers_DDP_AttRoute_Primary_Success(self):
#         """TestCase:getValidTN_MultipleCustomers_DDP_AttRoute_Primary_Success"""
#         self.testId = "cis_test_041_Success"
#         uri = configs.config.CISEndpoint + " " #Test Data required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_MultipleCustomers_DDP_AttRoute_Primary_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_041_Success", "testValidTN_MultipleCustomers_DDP_AttRoute_Primary_Success", output)
#         self.assertEqual(output[1]['tnType'], 'PRIMARY')
#         self.assertEqual((len(output[0]['account'])), 13)
#         self.assertEqual((len(output)), 6)
#          
#     def testValidTN_MultipleCustomers_DDP_AttRoute_Primary_Failure(self):
#         """TestCase:getValidTN_MultipleCustomers_DDP_AttRoute_Primary_Failure"""
#         self.testId = "cis_test_041_Failure"
#         uri = configs.config.CISEndpoint + " " #Test Data required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_MultipleCustomers_DDP_AttRoute_Primary_Failure")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_041_Failure", "testValidTN_MultipleCustomers_DDP_AttRoute_Primary_Failure", output)
#         self.assertNotEquals((len(output)), 4)
# 
#     #AttRoute
#     def testValidTN_MultipleCustomers_Combination_AttRoute_Primary_Success(self):
#         """TestCase:getValidTN_MultipleCustomers_Combination_AttRoute_Primary_Success"""
#         self.testId = "cis_test_042_Success"
#         uri = configs.config.CISEndpoint + "" #Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_MultipleCustomers_Combination_AttRoute_Primary_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_042_Success", "testValidTN_MultipleCustomers_Combination_AttRoute_Primary_Success", output)
#         self.assertEqual(output[1]['tnType'], 'PRIMARY')
#         self.assertEqual((len(output[0])), 2)
#         self.assertEqual((len(output)), 6)
#          
#     def testValidTN_MultipleCustomers_Combination_AttRoute_Primary_Failure(self):
#         """TestCase:getValidTN_MultipleCustomers_Combination_AttRoute_Primary_Failure"""
#         self.testId = "cis_test_042_Failure"
#         uri = configs.config.CISEndpoint + "" #Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_MultipleCustomers_Combination_AttRoute_Primary_Failure")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_042_Failure", "testValidTN_MultipleCustomers_Combination_AttRoute_Primary_Failure", output)
#         self.assertNotEquals((len(output)), 4)
#    
#     #AttRoute
#     def testValidTN_MultipleCustomers_Combination_AttRoute_Alternate_Success(self):
#         """TestCase:getValidTN_MultipleCustomers_Combination_AttRoute_Alternate_Success"""
#         self.testId = "cis_test_043_Success"
#         uri = configs.config.CISEndpoint + "" #Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_MultipleCustomers_Combination_AttRoute_Alternate_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_043_Success", "testValidTN_MultipleCustomers_Combination_AttRoute_Alternate_Success", output)
#         self.assertEqual(output[1]['tnType'], 'ALTERNATE')
#         self.assertEqual((len(output[0])), 2)
#         self.assertEqual((len(output)), 6)
#          
#     def testValidTN_MultipleCustomers_Combination_AttRoute_Alternate_Failure(self):
#         """TestCase:getValidTN_MultipleCustomers_Combination_AttRoute_Alternate_Failure"""
#         self.testId = "cis_test_043_Failure"
#         uri = configs.config.CISEndpoint + "" #Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_MultipleCustomers_Combination_AttRoute_Alternate_Failure")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_043_Failure", "testValidTN_MultipleCustomers_Combination_AttRoute_Alternate_Failure", output)
#         self.assertNotEquals((len(output)), 4)
#    
# 
#     #AttRoute
#     def testValidTN_SingleCustomerCSG_AttRoute_Alternate_Success(self):
#         """TestCase:getValidTN_MultipleCustomers_AttRoute_Alternate_Success"""
#         self.testId = "cis_test_044_Success"
#         uri = configs.config.CISEndpoint + "" # Test Data required 
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_AttRoute_Alternate_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_044_Success", "testValidTN_SingleCustomerCSG_AttRoute_Alternate_Success", output)
#         self.assertTrue(output[0]['tnType'], 'ALTERNATE')
#         self.assertEqual(len(output[0]['accountNumber']), 16)
#          
#     def testValidTN_SingleCustomerCSG_AttRoute_Alternate_Failure(self):
#         """TestCase:getValidTN_MultipleCustomers_AttRoute_Alternate_Failure"""
#         self.testId = "cis_test_044_Failure"
#         uri = configs.config.CISEndpoint + " " # Test Data required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_AttRoute_Alternate_Failure")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_044_Failure", "testValidTN_SingleCustomerCSG_AttRoute_Alternate_Failure", output)
#         self.assertNotEqual((len(output)), 2)
# 
#     #AttRoute
#     def testValidTN_MultipleCustomers_AttRoute_Alternate_Success(self):
#         """TestCase:getValidTN_MultipleCustomers_AttRoute_Alternate_Success"""
#         self.testId = "cis_test_045_Success"
#         uri = configs.config.CISEndpoint + "" #Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_MultipleCustomers_AttRoute_Alternate_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_045_Success", "testValidTN_MultipleCustomers_AttRoute_Alternate_Success", output)
#         self.assertEqual(output[1]['tnType'], 'ALTERNATE')
#         self.assertEqual((len(output[0])), 2)
#         self.assertEqual((len(output)), 6)
#            
#     def testValidTN_MultipleCustomers_AttRoute_Alternate_Failure(self):
#         """TestCase:getValidTN_MultipleCustomers_AttRoute_Alternate_Failure"""
#         self.testId = "cis_test_045_Failure"
#         uri = configs.config.CISEndpoint + " " #Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_MultipleCustomers_AttRoute_Alternate_Failure")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_045_Failure", "testValidTN_MultipleCustomers_AttRoute_Alternate_Failure", output)
#         self.assertNotEquals((len(output)), 4)
# 
#     #AttRoute
#     def testValidTN_MultipleCustomers_CSG_AttRoute_Alternate_Success(self):
#         """TestCase:getValidTN_MultipleCustomers_CSG_AttRout_eAlternate_Success"""
#         self.testId = "cis_test_046_Success"
#         uri = configs.config.CISEndpoint + " " #Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_MultipleCustomers_CSG_AttRoute_Alternate_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_046_Success", "testValidTN_MultipleCustomers_CSG_AttRoute_Alternate_Success", output)
#         self.assertEqual(output[1]['tnType'], 'ALTERNATE')
#         self.assertEqual((len(output[0])), 2)
#         self.assertEqual((len(output)), 6)
#           
#     def testValidTN_MultipleCustomers_CSG_AttRoute_Alternate_Failure(self):
#         """TestCase:getValidTN_MultipleCustomers_CSG_AttRoute_Alternate_Failure"""
#         self.testId = "cis_test_046_Failure"
#         uri = configs.config.CISEndpoint + " " #Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_MultipleCustomers_CSG_AttRoute_Alternate_Failure")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_046_Failure", "testValidTN_MultipleCustomers_CSG_AttRoute_Alternate_Failure", output)
#         self.assertNotEquals((len(output)), 4)
# 
#     #AttRoute
#     def testValidTN_SingleCustomerDDP_AttRoute_Alternate_Success(self):
#         """TestCase:getValidTN_SingleCustomerDDP_AttRoute_Alternate_Success"""
#         self.testId = "cis_test_047_Success"
#         uri = configs.config.CISEndpoint + "" #Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerDDP_AttRoute_Alternate_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_047_Success", "testValidTN_SingleCustomerDDP_AttRoute_Alternate_Success", output)
#         self.assertEqual(response.status_code, 404)
#  
#     def testValidTN_SingleCustomerDDP_AttRoute_Alternate_Failure(self):
#         """TestCase:getValidTN_SingleCustomerDDP_AttRoute_Alternate_Failure"""
#         self.testId = "cis_test_047_Failure"
#         uri = configs.config.CISEndpoint + "" #Test output required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerDDP_AttRoute_Alternate_Failure")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_047_Failure", "testValidTN_SingleCustomerDDP_AttRoute_Alternate_Failure", output)
#         self.assertNotEquals(response.status_code, 500)
# 
#     def testValidTN_MultipleCustomers_DDP_AttRoute_Alternate_Success(self):
#         """TestCase:getValidTN_MultipleCustomers_DDP_AttRoute_Alternate_Success"""
#         self.testId = "cis_test_048_Success"
#         uri = configs.config.CISEndpoint + " " #Test Data required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerDDP_AttRoute_Alternate_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_048_Success", "testValidTN_MultipleCustomers_DDP_AttRoute_Alternate_Success", output)
#         self.assertEqual(output[1]['tnType'], 'ALTERNATE')
#         self.assertEqual((len(output[0]['account'])), 13)
#         self.assertEqual((len(output)), 6)
#          
#     def testValidTN_MultipleCustomers_DDP_AttRoute_Alternate_Failure(self):
#         """TestCase:getValidTN_MultipleCustomers_DDP_AttRoute_Alternate_Failure"""
#         self.testId = "cis_test_048_Failure"
#         uri = configs.config.CISEndpoint + " " #Test Data required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_MultipleCustomers_DDP_AttRoute_Alternate_Failure")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_048_Failure", "testValidTN_MultipleCustomers_DDP_AttRoute_Alternate_Failure", output)
#         self.assertNotEquals((len(output)), 4)
# 
#         
#     def testValidTN_Attroute_Timeout_Success(self):
#         """TestCase:getValidTN_Attroute_Timeout_Success"""
#         self.testId = "cis_test_049_Success"
#         uri = configs.config.CISEndpoint + " " #Test Data required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertEqual(output[1]['tnType'], 'ALTERNATE')
#         self.assertEqual((len(output[0]['account'])), 13)
#         self.assertEqual((len(output)), 6)
#          
#     def testValidTN_Attroute_Timeout_Failure(self):
#         """TestCase:getValidTN_Attroute_Timeout_Failure"""
#         self.testId = "cis_test_049_Failure"
#         uri = configs.config.CISEndpoint + " " #Test Data required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertNotEquals((len(output)), 4)
# 
#     def testValidTN_Attroute_Exception_Success(self):
#         """TestCase:getValidTN_Attroute_Exception_Success"""
#         self.testId = "cis_test_050_Success"
#         uri = configs.config.CISEndpoint + " " #Test Data required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertEqual(output[1]['tnType'], 'ALTERNATE')
#         self.assertEqual((len(output[0]['account'])), 13)
#         self.assertEqual((len(output)), 6)
#          
#     def testValidTN_Attroute_Exception_Failure(self):
#         """TestCase:getValidTN_Attroute_Exception_Failure"""
#         self.testId = "cis_test_050_Failure"
#         uri = configs.config.CISEndpoint + " " #Test Data required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertNotEquals((len(output)), 4)
# 
#     def testValidTN_Attroute_NotAvailable_Success(self):
#         """TestCase:getValidTN_Attroute_NotAvailable_Success"""
#         self.testId = "cis_test_051_Success"
#         uri = configs.config.CISEndpoint + " " #Test Data required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertEqual(output[1]['tnType'], 'ALTERNATE')
#         self.assertEqual((len(output[0]['account'])), 13)
#         self.assertEqual((len(output)), 6)
#          
#     def testValidTN_Attroute_NotAvailable_Failure(self):
#         """TestCase:getValidTN_Attroute_NotAvailable_Failure"""
#         self.testId = "cis_test_051_Failure"
#         uri = configs.config.CISEndpoint + " " #Test Data required
#         response = requests.get(uri)
#         output = response.json()
#         cisService = CISService("testValidTN_SingleCustomerCSG_Success")
#         cisService.writeResponseToFile(output)
#         cisService.printOutput("cis_test_006_Success", "testValidTN_SingleCustomerCSG_Success", output)
#         self.assertNotEquals((len(output)), 4)

if __name__ == '__main__':
    del sys.argv[1:]
    print sys.argv[1]
unittest.main()
