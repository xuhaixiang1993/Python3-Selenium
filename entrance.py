import os
import unittest
import HTMLTestRunnerCN

import getcwd
from TestSuites.testHome import TestHome
from TestSuites.testLogin import TestLogin
from Common.log import log1


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestHome('test_select_selenium'))
    suite.addTest(TestHome('test_switch_login'))
    suite.addTest(TestLogin('test_login1'))
    suite.addTest(TestLogin('test_login2'))
    suite.addTest(TestLogin('test_login3'))
    suite.addTest(TestLogin('test_login4'))
    log1.info('加载测试用例')
    path = getcwd.get_cwd()
    file_path = os.path.join(path, 'Report/xxxUi自动化测试报告.html')
    try:
        fp = open(file_path, 'wb')
        runner = HTMLTestRunnerCN.HTMLTestReportCN(
            stream=fp,
            title='xxxUi自动化测试报告',
            description='报告描述',
            tester='测试者'
        )
        runner.run(suite)
        log1.info('test end')
        fp.close()
        log1.info('测试报告生成成功')
    except BaseException:
        log1.error("测试报告生成失败", exc_info=1)
    # sent_mail()
