import  pandas as pd
import json
import pymysql
import datetime,time
import os
import xlrd

def to_summary(path):
    workbook = xlrd.open_workbook(path)
    # 文件所包含的所有sheetname
    sheetname = workbook.sheet_names()

    conn = pymysql.connect(host='10.16.31.77', user='root', password='AutoTest', port=3306,database='chart_demo')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    for i in range(-4,0):
        data = pd.read_excel(path,sheet_name=sheetname[i])
        df = pd.DataFrame(data)
        for k in range(len(data['TIME'])):
            df['user_nice'] = df['%user']+df['%nice']
            user_nice = df['user_nice'][k]
            print(user_nice)
            cpu = df['%cpu'][k]
            print(cpu)
            sys = df['%sys'][k]
            idle = df['%idle'][k]
            iow = df['%iow'][k]
            total_raw = df['Total_RAM'][k]
            available_raw = df['Available_RAM'][k]
            used_raw = df['Used_RAM'][k]
            free = df['free'][k]
            tstr = '2020-'+sheetname[i]+' ' + str(data['TIME'][k])
            try:
                time.strptime(tstr, "%Y-%m-%d %H:%M:%S")
                create_time = datetime.datetime.fromtimestamp(time.mktime(time.strptime(tstr, "%Y-%m-%d %H:%M:%S")))
            except Exception:
                # traceback.print_exc()
                continue
            print(create_time)

            sql = "insert into `summary` " \
                  "(time,cpu,user_nice,sys,idle,iow,total_raw,available_raw,free,used_raw) " \
                  "values('%s','%d','%d','%d','%d','%d','%d','%d','%d','%d')" \
                  % (create_time, cpu, user_nice, sys, idle, iow, total_raw, available_raw, free,used_raw)
            print(sql)
            try:
                # values = (dalvik_max,dalvik_min,dalvik_avg,native_max,native_min,native_avg,cpu_max,cpu_min,cpu_avg,crash)
                cursor.execute(sql)
                conn.commit()
                print('....................')
            except:
                conn.rollback()
                print('=====================')

    cursor.close()
    conn.close()
if __name__ == '__main__':
    to_summary('./analysis_module/aasummary.xlsx')



# conn = pymysql.connect(host='10.16.31.77', user='root', password='AutoTest',
#                        port=3306,database = 'chart_demo')
# cursor = conn.cursor()
#
#
#
# # for j in range(1,len(sheetname)):
# data = pd.read_excel(new_path, sheet_name=sheetname[-1])
# for k in range(len(data['TIME'])):
#     timstr = '2020-' + str(sheetname[-1]) + ' ' + str(data['TIME'][k])
#     try:
#         time.strptime(timstr, "%Y-%m-%d %H:%M:%S")
#         create_time = datetime.datetime.fromtimestamp(
#             time.mktime(time.strptime(timstr, "%Y-%m-%d %H:%M:%S")))
#     except Exception:
#         continue
#     print(create_time)
#     dalvik = data['DALVIK'][k]
#     print(dalvik)
#     native = data['NATIVE'][k]
#     print(native)
#     cpu = data['CPU'][k]
#     print(cpu)
#
#     sql = "insert into daily_data " \
#           "(package_name,dalvik,native,cpu,time) " \
#           "values('%s','%d','%d','%d','%s')" \
#           % (new_name, dalvik, native, cpu, create_time)
#     try:
#         # values = (dalvik_max,dalvik_min,dalvik_avg,native_max,native_min,native_avg,cpu_max,cpu_min,cpu_avg,crash)
#         cursor.execute(sql)
#         conn.commit()
#         print(sql)
#         print('....................')
#
#     except:
#         conn.rollback()
#         print('=====================')
#
# cursor.close()
# conn.close()