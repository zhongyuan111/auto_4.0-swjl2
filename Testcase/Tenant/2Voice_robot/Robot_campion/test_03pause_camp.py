#coding=gbk
from Common.get_token import Login_Token
import Common.public_tenant_api
from Config.public_config import Get_Config
import Common.public_tenant_api
import  pytest
import allure
import time
import json
from Common.Db_pg_conn import DB_pg

config =Get_Config()
token = Login_Token()
db_conn= DB_pg()
header1 = token.json_header('tenant')  # ʵ��json��ʽ��ͷ
header2 = token.upload_header('tenant')  # ʵ���ϴ��ļ��õ�ͷ
test_file = config.get_robot_testfile()
real_file = Common.public_tenant_api.upload_file(header2, test_file)
#camp_name = '�Զ����˻��' + str(int(time.time()))
instid=config.get_robot_instid()
flowid=config.get_robot_flowid()
callno=config.get_robot_callno()
ws_url = token.get_ws_url()  # ����websocket����
socketid = token.get_socketid(ws_url)
print('socketid:',socketid)
# ��������
test_datas =  [({"action":2,"socketId":socketid},["\u6210\u529F!",4],"��ͣ�˻������������")]
@allure.epic("�����")    #��Ŀ¼
@allure.feature("�˻��")   #����ģ��
@allure.story("�����˻��")   #����ģ���µķ�֧
@allure.link("https://redmine.lingban.cn/")  #����
@allure.title("{title}")
@pytest.mark.parametrize("test_input,expected,title",
                         test_datas
                         )
# @pytest.mark.skip()
def test_03(test_input,expected,title):
    '''�����˻��'''
    camp_name= '�Զ����˻��' + str(int(time.time()))
    input_json=[{"name":camp_name,"speaker":"YAY","instId":instid,"flowId":flowid,"callingNo":callno,"callingTimeout":30,
                 "file":real_file,"socketId":socketid,"fileName":test_file},{"action":1,"socketId":socketid}]
    res = Common.public_tenant_api.robot_camp_save(header1,input_json[0])
    print('����ƣ�',camp_name)
    print('������ӿڷ���::',res)
    print('campaignuuid:', json.loads(res)['data']['campaignUuid'])
    camp_uuid = json.loads(res)['data']['campaignUuid']
    test_input["camp_uuid"] = camp_uuid
    time.sleep(10)
    Common.public_tenant_api.camp_operation(header1,input_json[1],camp_uuid)
    time.sleep(20)
    operation_res=Common.public_tenant_api.camp_operation(header1,test_input,camp_uuid)
    print('��ͣ��ӿڷ��أ�',operation_res)
    msg=json.loads(operation_res)['msg']
    time.sleep(30)
    sql = 'select state from campaign where  campaign_uuid=\'' + camp_uuid + '\';'
    print('�˲����sql:::', sql)
    result = db_conn.select("outbound", sql)
    if result is not None:
        for rec in result:
             camp_state=rec[0]
    else:
             camp_state=888

    list_res = []
    list_res.append(msg)
    list_res.append(camp_state)  #У��״̬'״̬:0-�滮��;2-������;3-ֹͣ��;4-��ֹͣ;5-�����;7-��ȡ��

    print('�״̬state:', camp_state)

    assert   list_res==expected ,'��˲�ӿ�'