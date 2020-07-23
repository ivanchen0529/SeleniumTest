import unittest
import time
import HTMLTestReport
import os

#生成报告的时间
current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
# 用例路径 默认获取当前目录
case_path = os.getcwd()
# 报告存放路径 默认获取当前目录
report_path = os.path.join(os.getcwd(), 'report_'+current_time+".html")

def all_case():
    # test*.py  用例的文件必须是test开头 并且只能包含字母或者下划线，否则有可能识别不了,无法全部执行
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)
    print(discover)
    return discover

if __name__ == "__main__":
    fp = open(report_path, "wb")
    # 用例标题，执行者可以自己更改
    runner = HTMLTestReport.HTMLTestRunner(stream=fp, title="自动化测试报告", \
                                           description='自动化测试报告', tester='liyushu')
    runner.run(all_case())
    fp.close()

