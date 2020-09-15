import  pandas as pd
import json
import pymysql
import datetime,time
import os
import xlrd
import shutil

def find_file(path):
    os.system('mkdir xlsxfile')
    all_file = os.listdir(path)
    need_file = './xlsxfile/'
    for name in all_file:
        if name.startswith('com.') or name.startswith('surface') or name.startswith('system'):
            #找到符合条件的文件名
            new_name = os.path.splitext(name)[0]
            #文件路径
            new_path = path+new_name+'.xlsx'
            # 打开相应的文件
            shutil.copy(new_path,need_file)


def to_daily_data(path):
    workbook_c = xlrd.open_workbook(path+'com.hryt.desktop.xlsx')
    sheetname_c = workbook_c.sheet_names()
    # print(sheetname_c)
    dealed_path = []#删选出来文件的所有路径
    packagename = []
    for needed_name in os.listdir(path):
        packagename.append(needed_name.split('.xlsx')[0])
        needed_file = os.path.join(path,needed_name)
        dealed_path.append(needed_file)
    for i in range(len(dealed_path)):
        workbook = xlrd.open_workbook(dealed_path[i])
        # 文件所包含的所有sheetname
        sheetname = workbook.sheet_names()
        for name in sheetname:
            if name == sheetname_c[-1]:
                conn = pymysql.connect(host='10.16.31.77', user='root', password='AutoTest',
                                       port=3306,database = 'chart_demo')
                cursor = conn.cursor()
                data = pd.read_excel(dealed_path[i],sheet_name=sheetname_c[-1])
                for k in range(len(data['TIME'])):
                    timstr = '2020-' + str(sheetname_c[-1]) + ' ' + str(data['TIME'][k])
                    try:
                        time.strptime(timstr, "%Y-%m-%d %H:%M:%S")
                        create_time = datetime.datetime.fromtimestamp(
                            time.mktime(time.strptime(timstr, "%Y-%m-%d %H:%M:%S")))
                    except Exception:
                        continue
                    print(create_time)
                    dalvik = data['DALVIK'][k]
                    print(dalvik)
                    native = data['NATIVE'][k]
                    print(native)
                    cpu = data['CPU'][k]
                    print(cpu)
                    sql = "insert into test(package_name,dalvik,native,cpu,time) values('%s','%d','%d','%d','%s')"% (packagename[i], dalvik, native, cpu, create_time)
                    print(sql)
                    try:
                        # values = (dalvik_max,dalvik_min,dalvik_avg,native_max,native_min,native_avg,cpu_max,cpu_min,cpu_avg,crash)
                        cursor.execute(sql)
                        conn.commit()
                        print(sql)
                        print('....................')

                    except:
                        conn.rollback()
                        print('=====================')

                cursor.close()
                conn.close()
            else:
                continue


if __name__ == '__main__':
    # find_file('./analysis_module/')
    to_daily_data('./test/')


# path = './analysis_module/'
# all_file = os.listdir(path)
#
# for name in all_file:
#     if name.startswith('com.') or name.startswith('surface') or name.startswith('system'):
#         #找到符合条件的文件名
#         new_name = os.path.splitext(name)[0]
#         #文件路径
#         new_path = path+new_name+'.xlsx'
#         #打开相应的文件
#         xl =pd.ExcelFile(new_path)
#         sheet_names = xl.sheet_names
#         # print(sheet_names)
#         if len(sheet_names) > 1:
#             try:
#
#                 if sheet_names[-1]=='index':
#                     continue
#                 else:
#                     conn = pymysql.connect(host='10.16.31.77', user='root', password='AutoTest',
#                                            port=3306,database = 'chart_demo')
#                     cursor = conn.cursor()
#                     data = pd.read_excel(new_path, sheet_name=sheet_names[-1])
#                     # print(data)
#                     for k in range(len(data['TIME'])):
#                         timstr = '2020-' + str(sheet_names[-1]) + ' ' + str(data['TIME'][k])
#                         try:
#                             time.strptime(timstr, "%Y-%m-%d %H:%M:%S")
#                             create_time = datetime.datetime.fromtimestamp(
#                                 time.mktime(time.strptime(timstr, "%Y-%m-%d %H:%M:%S")))
#                         except Exception:
#                             continue
#                         print(create_time)
#                         dalvik = data['DALVIK'][k]
#                         print(dalvik)
#                         native = data['NATIVE'][k]
#                         print(native)
#                         cpu = data['CPU'][k]
#                         print(cpu)
#
#                         sql = "insert into test(package_name,dalvik,native,cpu,time) values('%s','%d','%d','%d','%s')"% (new_name, dalvik, native, cpu, create_time)
#                         try:
#                             # values = (dalvik_max,dalvik_min,dalvik_avg,native_max,native_min,native_avg,cpu_max,cpu_min,cpu_avg,crash)
#                             cursor.execute(sql)
#                             conn.commit()
#                             print(sql)
#                             print('....................')
#
#                         except:
#                             conn.rollback()
#                             print('=====================')
#
#                     cursor.close()
#                     conn.close()
#             except Exception:
#                 continue
