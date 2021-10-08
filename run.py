#!/usr/bin/env python
# coding=gbk
import pytest
import os

root_dir = os.path.dirname(os.path.abspath('.'))  # ��ȡ��Ŀ��Ŀ¼�����·��
file_path = root_dir + '\\auto_4.0\\Report'
print('root_dir:::',root_dir)

if __name__ == "__main__":
    #pytest.main(['-s'])
    # ִ��pytest��Ԫ���ԣ����� Allure ������Ҫ�����ݴ��� /temp Ŀ¼
    #pytest.main(['--alluredir', file_path])
    pytest.main(['-s', '-q', '--alluredir', file_path, root_dir+'\\auto_4.0\\Testcase\\Tenant\\1Super_agent'])
    # ִ������ allure generate ./temp -o ./report --clean �����ɲ��Ա���
    #os.popen('allure generate --clean ./Report')
    os.popen('allure generate ./Report  -o ./allure-report   --clean')



