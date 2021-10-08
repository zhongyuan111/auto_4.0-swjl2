#coding=gbk
import json
import allure
import pytest
from Common.common_param import  Common_param
import Common.public_tenant_api
from Common.get_token import Login_Token

token=Login_Token()
pre_camp=Common_param()
header1 = token.json_header('tenant')  # ʵ��json��ʽ��ͷ
pre_res=pre_camp.pre_campinon()
#print(pre_res)
pre_res1=pre_camp.pre_campinon1()
# ��������
test_datas =  [({"id":pre_res[2]},["\u6210\u529F!",10],"�˻��ͨ����¼��ѯ����������")]
@allure.epic("�����")    #��Ŀ¼
@allure.feature("�˻��")   #����ģ��
@allure.story("�˻�ͨ����¼��ѯ")   #����ģ���µķ�֧
@allure.link("https://redmine.lingban.cn/")  #����
@allure.title("{title}")
@pytest.mark.parametrize("test_input,expected,title",
                         test_datas
                         )
@pytest.mark.skipif(pre_res=='false',reason='pre_wrong')
def test_robotrecordlist(test_input,expected,title):
    res=Common.public_tenant_api.camp_query_record(header1,test_input)
    msg=json.loads(res)['msg']
    total=json.loads(res)['data']['total']
    checklist=[]
    checklist.append(msg)
    checklist.append(total)
    assert checklist==expected,'�ӿڷ��ؿ�'



#��������
test_datas1 =  [({"id":pre_res1[2]},["\u6210\u529F!",10],"�˻�Эͬͨ����¼��ѯ����������")]
@allure.epic("�����")    #��Ŀ¼
@allure.feature("�˻��")   #����ģ��
@allure.story("�˻�Эͬͨ����¼��ѯ")   #����ģ���µķ�֧
@allure.link("https://redmine.lingban.cn/")  #����
@allure.title("{title}")
@pytest.mark.parametrize("test_input,expected,title",
                         test_datas1
                         )
@pytest.mark.skipif(pre_res1=='false',reason='pre_wrong')
def test_mixcrecordlist(test_input,expected,title):
    res=Common.public_tenant_api.camp_query_record(header1,test_input)
    msg=json.loads(res)['msg']
    total=json.loads(res)['data']['total']
    checklist=[]
    checklist.append(msg)
    checklist.append(total)
    assert checklist==expected,'�ӿڷ��ؿ�'
