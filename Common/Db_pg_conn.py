#coding=gbk
import psycopg2
import logging
import sys
from Config.public_config import  Get_Config
import json
# ������־
# ��ȡloggerʵ��
logger = logging.getLogger("baseSpider")
# ָ�������ʽ
formatter = logging.Formatter('%(asctime)s\
              %(levelname)-8s:%(message)s')
# �ļ���־
file_handler = logging.FileHandler("operation_database.log")
file_handler.setFormatter(formatter)
# ����̨��־
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

# Ϊlogge��Ӿ������־������
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.setLevel(logging.INFO)

get_config=Get_Config()

class DB_pg():
    # ������ѯ������
    def select(self,db,sql):

        host=json.loads(get_config.get_pg_conn())['host']
        user=json.loads(get_config.get_pg_conn())['user']
        password=json.loads(get_config.get_pg_conn())['password']
        port=json.loads(get_config.get_pg_conn())['port']
        # print(get_config.get_pg_conn()['user'])
        # print(get_config.get_pg_conn()['password'])
        conn = psycopg2.connect(host=host, user=user,
                                password=password, database=db, port=port)
        cur=conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        print('��ѯ��䷵�ؽ��:',result)
        cur.close()
        conn.close()
        return result
