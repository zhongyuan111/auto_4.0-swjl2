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
camp_name=pre_camp.pre_campinon()
camp_name1=pre_camp.pre_campinon1()
# ��������
test_datas =  [({"name":camp_name[0]},["\u6210\u529F!",1],"�˻����ѯ����������")]
@allure.epic("�����")    #��Ŀ¼
@allure.feature("�˻��")   #����ģ��
@allure.story("�˻����ѯ")   #����ģ���µķ�֧
@allure.link("https://redmine.lingban.cn/")  #����
@allure.title("{title}")
@pytest.mark.parametrize("test_input,expected,title",
                         test_datas
                         )
@pytest.mark.skipif(camp_name='false')
def test_robotcamplist(test_input,expected,title):
    res=Common.public_tenant_api.camp_manage_list(header1,test_input)
    msg=json.loads(res)['msg']
    total=json.loads(res)['data']['total']
    checklist=[]
    checklist.append(msg)
    checklist.append(total)
    assert checklist==expected,'�ӿڷ��ؿ�'



# ��������
test_datas1 =  [({"name":camp_name1[0]},["\u6210\u529F!",1],"�˻�Эͬ���ѯ����������")]
@allure.epic("�����")    #��Ŀ¼
@allure.feature("�˻��")   #����ģ��
@allure.story("�˻�Эͬ���ѯ")   #����ģ���µķ�֧
@allure.link("https://redmine.lingban.cn/")  #����
@allure.title("{title}")
@pytest.mark.parametrize("test_input,expected,title",
                         test_datas1
                         )
@pytest.mark.skipif(camp_name1='false')
def test_mixcamplist(test_input,expected,title):
    res=Common.public_tenant_api.camp_manage_list(header1,test_input)
    msg=json.loads(res)['msg']
    total=json.loads(res)['data']['total']
    checklist=[]
    checklist.append(msg)
    checklist.append(total)
    assert checklist==expected,'�ӿڷ��ؿ�'
