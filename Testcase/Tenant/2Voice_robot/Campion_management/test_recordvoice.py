#coding=gbk
import json
import allure
import pytest
from Common.common_param import  Common_param
import Common.public_tenant_api
from Common.get_token import Login_Token
import math
token=Login_Token()
pre_camp=Common_param()
header1 = token.json_header('tenant')  # ʵ��json��ʽ��ͷ
pre_res=pre_camp.pre_campinon()

# ��������
test_datas=[({'camp_uuid':pre_res[1],'call_id':pre_res[3]},None,'ͨ������¼��')]
@allure.epic("�����")    #��Ŀ¼
@allure.feature("�˻��")   #����ģ��
@allure.story("ͨ������¼��")   #����ģ���µķ�֧
@allure.link("https://redmine.lingban.cn/")  #����
@allure.title("{title}")
@pytest.mark.skipif(pre_res=='false',reason='webhook_wrong')
@pytest.mark.parametrize("test_input,expected,title",
                         test_datas
                         )
def test_record_voice(test_input,expected,title):
   '''ͨ�������в�ѯ¼���ӿ�'''

   res=Common.public_tenant_api.query_record_voice(header1,test_input)
   assert res!=expected,'δ����¼��'

