import os
import sys
import logging

logger = logging.getLogger(__name__)
logging.basicConfig()
logger.setLevel(logging.ERROR)

class TestLib(object):
    def __init__(self):
        logger.debug("Testparser init()")

    def print_result(self, id, params, output, status):
        print ''.join(['=' for i in range(1, 100)])
        print "\nTest ID: %s" % id
        print "Test type: %s" % params['type']
        print "Test name: %s" % params['name']
        print "Test status: %s" % ("passed" if status else "failed")
        print ''.join(['=' for i in range(1, 100)])
        sys.stdout.flush()
        logger.debug("Expected result: %s" % params['remote_expected_result'])
        logger.debug("Actual result: %s" % output)

    def exec_remote_cmd(self, host, dut, id, params):
        output, status = dut.send_command(params['remote_cmd'], params['remote_cmd_timeout'], params['remote_cmd_error_hint'])
        status = dut.check_output(params['remote_expected_result'])
        self.print_result(id, params, output, status)
        return output, status

    def lspci_test(self, host, dut, id, params):
        params['remote_cmd'] = 'lspci -k'
        return self.exec_remote_cmd(host, dut, id, params)
