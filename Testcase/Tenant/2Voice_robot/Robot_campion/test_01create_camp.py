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
test_file = config.get_robot_testfile()   #����ļ���Դ�ļ�����
real_file = Common.public_tenant_api.upload_file(header2, test_file)#upload�ӿڷ����ļ�����
#camp_name = '�Զ����˻��' + str(int(time.time()))
instid=config.get_robot_instid() #robotid
flowid=config.get_robot_flowid() #�汾id
callno=config.get_robot_callno()  #���
ws_url = token.get_ws_url()  # ����websocket����
socketid = token.get_socketid(ws_url)

# ��������test
#��Դ���ӱ�ע
test_datas =  [({"name": '�Զ����˻��' + str(int(time.time())),"speaker":"YAY","instId":instid,"flowId":flowid,"callingNo":callno,"callingTimeout":30,
                 "file":real_file,"socketId":socketid,"fileName":test_file},["\u6210\u529F!",0,1,10],"�����˻������������1"),
               ({"name": '�Զ����˻��' + str(int(time.time())+1),"speaker": "wlu","instId": instid,"flowId": flowid,"callingNo": callno,"callingTimeout": 30,
                 "file": real_file, "socketId": socketid, "fileName": test_file}, ["\u6210\u529F!", 0, 1,10],"�����˻������������2"),
               ({"name": '�Զ����˻��' + str(int(time.time())+1),"speaker": "wlu","instId": instid,"flowId": flowid,"callingNo": callno,"callingTimeout": 30,
                 "file": real_file, "socketId": socketid, "fileName": test_file}, ["��������������", 999, 999,999], "������ظ�")
               ]
@allure.epic("�����")    #��Ŀ¼
@allure.feature("�˻��")   #����ģ��
@allure.story("�����˻��")   #����ģ���µķ�֧
@allure.link("https://redmine.lingban.cn/")  #����
@allure.title("{title}")
@pytest.mark.parametrize("test_input,expected,title",
                         test_datas
                         )
# @pytest.mark.skip()
def test_01(test_input,expected,title):
    '''�����˻��'''

    res = Common.public_tenant_api.robot_camp_save(header1,test_input)
    print('test_input',test_input)
    print('res::::::::::',res)

    msg = json.loads(res)['msg']
    time.sleep(10)

    if msg == "\u6210\u529F!":       #�ӿڷ���msg�ɹ����״̬�������Ƿ���ȷ
        print('campaignuuid:', json.loads(res)['data']['campaignUuid'])
        camp_uuid = json.loads(res)['data']['campaignUuid']
        sql='select state,type,total_numbers from campaign where  campaign_uuid=\''+camp_uuid+'\';'
        print('�˲����sql:::',sql)
        result = db_conn.select("outbound",sql)
        if result is not None:
            for rec in result:
                camp_state=rec[0]
                type=rec[1]
                total=rec[2]
    else:                          #�ӿڷ���ʧ�ܣ��˲������Ƿ���������������������
        sql = 'select count(*) from campaign where  name=\'' + test_input['name'] + '\';'
        print('�˲����sql:::', sql)
        result = db_conn.select("outbound", sql)
        for rec in result:
             cont=rec[0]
        if cont==1:
            camp_state = 999
            type = 999
            total=999
        else:
            camp_state=888
            type=888
            total=888
    list_res = []
    list_res.append(msg)    #�ӿڷ���
    list_res.append(camp_state)   #У��״̬'״̬:0-�滮��;2-������;3-ֹͣ��;4-��ֹͣ;5-�����;7-��ȡ��
    list_res.append(type)      #У������   ����� 1-��������� 2-�˻�Эͬ���3-�˹�Ԥ�����
    list_res.append(total)     #У���ϴ���������������ֶΣ�Ĭ��10��
    print('�״̬state�ͻ���͡��ϴ�����:', camp_state,type,total)

    assert   list_res==expected ,'��˲�ӿ�'
#jlwang 