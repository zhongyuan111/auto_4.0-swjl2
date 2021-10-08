import pymysql
import logging
import sys
from Common.public_config import  Get_Config

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


class DB_mysql():
    # ���캯��,��ʼ�����ݿ�����
    def __init__(self,db,sql,params=None):
        self.database=db
        self.sql = sql
        self.params = params
        self.conn = None
        self.cur = None

    def connectiondatabase(self):
        print(Get_Config.get_mysql_conn()['host'],Get_Config.get_mysql_conn()['username'],Get_Config.get_mysql_conn()['password'],Get_Config.get_mysql_conn()['database'],Get_Config.get_mysql_conn()['charset'])
        try:
            self.conn = pymysql.connect(Get_Config.get_mysql_conn()['host'],Get_Config.get_mysql_conn()['username'],
                                    Get_Config.get_mysql_conn()['password'],self.database,charset=Get_Config.get_mysql_conn()['charset'])
        except:
            logger.error("connectDatabase failed")
            return False
        self.cur = self.conn.cursor()
        return True



    # �ر����ݿ�
    def closedatabase(self):
        # ������ݴ򿪣���رգ�����û�в���
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()
        return True



    # ������ѯ������
    def select(self):
        self.connectiondatabase()
        self.cur.execute(self.sql,self.params)
        result = self.cur.fetchall()
        print(result)
        return result
