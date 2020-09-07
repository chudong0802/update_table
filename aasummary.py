import  pandas as pd
import pymysql
import datetime,time

file = './analysis_module/aasummary.xlsx'

conn = pymysql.connect(host='10.16.31.77', user='root', password='AutoTest', port=3306, database='chart_demo')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# def common(sheetname):
#     data = pd.read_excel(file, sheet_name=sheetname)
#     df = pd.DataFrame(data)
#     for k in range(len(data['TIME'])):
#         df['user_nice'] = df['%user'] + df['%nice']
#         user_nice = df['user_nice'][k]
#         print(user_nice)
#         cpu = df['%cpu'][k]
#         sys = df['%sys'][k]
#         idle = df['%idle'][k]
#         iow = df['%iow'][k]
#         total_raw = df['Total_RAM'][k]
#         available_raw = df['Available_RAM'][k]
#         used_raw = df['Used_RAM'][k]
#         free = df['free'][k]
#         tstr = '2020-' + str(data['Folder'][k] + ' ' + data['TIME'][k])
#         print(tstr)
#         try:
#             time.strptime(tstr, "%Y-%m-%d %H:%M:%S")
#             create_time = datetime.datetime.fromtimestamp(time.mktime(time.strptime(tstr, "%Y-%m-%d %H:%M:%S")))
#         except Exception:
#             # traceback.print_exc()
#             continue
#         print(create_time)
#
#         return cpu,sys,idle,iow,total_raw,available_raw,used_raw,free,create_time

def todb_capture_first(sheetname):
    data = pd.read_excel(file, sheet_name=sheetname)
    df = pd.DataFrame(data)
    for k in range(len(data['TIME'])):
        df['user_nice'] = df['%user']+df['%nice']
        user_nice = df['user_nice'][k]
        print(user_nice)
        cpu = df['%cpu'][k]
        sys = df['%sys'][k]
        idle = df['%idle'][k]
        iow = df['%iow'][k]
        total_raw = df['Total_RAM'][k]
        available_raw = df['Available_RAM'][k]
        used_raw = df['Used_RAM'][k]
        free = df['free'][k]
        tstr = '2020-'+ str(data['Folder'][k]+' '+data['TIME'][k])
        print(tstr)
        try:
            time.strptime(tstr, "%Y-%m-%d %H:%M:%S")
            create_time = datetime.datetime.fromtimestamp(time.mktime(time.strptime(tstr, "%Y-%m-%d %H:%M:%S")))
        except Exception:
            # traceback.print_exc()
            continue
        print(create_time)

        sql = "insert into `capture_first` " \
              "(time,cpu,user_nice,sys,idle,iow,total_raw,available_raw,free,used_raw) " \
              "values('%s','%d','%d','%d','%d','%d','%d','%d','%d','%d')" \
              % (create_time, cpu, user_nice, sys, idle, iow, total_raw, available_raw, free,used_raw)
        # print(sql)
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


def todb_capture_last(sheetname):
    data = pd.read_excel(file, sheet_name=sheetname)
    df = pd.DataFrame(data)
    for k in range(len(data['TIME'])):
        df['user_nice'] = df['%user']+df['%nice']
        user_nice = df['user_nice'][k]
        print(user_nice)
        cpu = df['%cpu'][k]
        sys = df['%sys'][k]
        idle = df['%idle'][k]
        iow = df['%iow'][k]
        total_raw = df['Total_RAM'][k]
        available_raw = df['Available_RAM'][k]
        used_raw = df['Used_RAM'][k]
        free = df['free'][k]
        tstr = '2020-'+ str(data['Folder'][k]+' '+data['TIME'][k])
        print(tstr)
        try:
            time.strptime(tstr, "%Y-%m-%d %H:%M:%S")
            create_time = datetime.datetime.fromtimestamp(time.mktime(time.strptime(tstr, "%Y-%m-%d %H:%M:%S")))
        except Exception:
            # traceback.print_exc()
            continue
        print(create_time)

        sql = "insert into `capture_last` " \
              "(time,cpu,user_nice,sys,idle,iow,total_raw,available_raw,free,used_raw) " \
              "values('%s','%d','%d','%d','%d','%d','%d','%d','%d','%d')" \
              % (create_time, cpu, user_nice, sys, idle, iow, total_raw, available_raw, free,used_raw)
        # print(sql)
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


def todb_capture_cpu_user_top(sheetname):
    data = pd.read_excel(file, sheet_name=sheetname)
    df = pd.DataFrame(data)
    for k in range(len(data['TIME'])):
        df['user_nice'] = df['%user']+df['%nice']
        user_nice = df['user_nice'][k]
        print(user_nice)
        cpu = df['%cpu'][k]
        sys = df['%sys'][k]
        idle = df['%idle'][k]
        iow = df['%iow'][k]
        total_raw = df['Total_RAM'][k]
        available_raw = df['Available_RAM'][k]
        used_raw = df['Used_RAM'][k]
        free = df['free'][k]
        tstr = '2020-'+ str(data['Folder'][k]+' '+data['TIME'][k])
        print(tstr)
        try:
            time.strptime(tstr, "%Y-%m-%d %H:%M:%S")
            create_time = datetime.datetime.fromtimestamp(time.mktime(time.strptime(tstr, "%Y-%m-%d %H:%M:%S")))
        except Exception:
            # traceback.print_exc()
            continue
        print(create_time)

        sql = "insert into `capture_cpu_user_top` " \
              "(time,cpu,user_nice,sys,idle,iow,total_raw,available_raw,free,used_raw) " \
              "values('%s','%d','%d','%d','%d','%d','%d','%d','%d','%d')" \
              % (create_time, cpu, user_nice, sys, idle, iow, total_raw, available_raw, free,used_raw)
        # print(sql)
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


def todb_capture_cpu_usernice_top(sheetname):
    data = pd.read_excel(file, sheet_name=sheetname)
    df = pd.DataFrame(data)
    for k in range(len(data['TIME'])):
        df['user_nice'] = df['%user'] + df['%nice']
        user_nice = df['user_nice'][k]
        print(user_nice)
        cpu = df['%cpu'][k]
        sys = df['%sys'][k]
        idle = df['%idle'][k]
        iow = df['%iow'][k]
        total_raw = df['Total_RAM'][k]
        available_raw = df['Available_RAM'][k]
        used_raw = df['Used_RAM'][k]
        free = df['free'][k]
        tstr = '2020-' + str(data['Folder'][k] + ' ' + data['TIME'][k])
        print(tstr)
        try:
            time.strptime(tstr, "%Y-%m-%d %H:%M:%S")
            create_time = datetime.datetime.fromtimestamp(time.mktime(time.strptime(tstr, "%Y-%m-%d %H:%M:%S")))
        except Exception:
            # traceback.print_exc()
            continue
        print(create_time)

        sql = "insert into `capture_cpu_usernice_top` " \
              "(time,cpu,user_nice,sys,idle,iow,total_raw,available_raw,free,used_raw) " \
              "values('%s','%d','%d','%d','%d','%d','%d','%d','%d','%d')" \
              % (create_time, cpu, user_nice, sys, idle, iow, total_raw, available_raw, free,used_raw)
        # print(sql)
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


def todb_capture_cpu_sys_top(sheetname):
    data = pd.read_excel(file, sheet_name=sheetname)
    df = pd.DataFrame(data)
    for k in range(len(data['TIME'])):
        df['user_nice'] = df['%user'] + df['%nice']
        user_nice = df['user_nice'][k]
        print(user_nice)
        cpu = df['%cpu'][k]
        sys = df['%sys'][k]
        idle = df['%idle'][k]
        iow = df['%iow'][k]
        total_raw = df['Total_RAM'][k]
        available_raw = df['Available_RAM'][k]
        used_raw = df['Used_RAM'][k]
        free = df['free'][k]
        tstr = '2020-' + str(data['Folder'][k] + ' ' + data['TIME'][k])
        print(tstr)
        try:
            time.strptime(tstr, "%Y-%m-%d %H:%M:%S")
            create_time = datetime.datetime.fromtimestamp(time.mktime(time.strptime(tstr, "%Y-%m-%d %H:%M:%S")))
        except Exception:
            # traceback.print_exc()
            continue
        print(create_time)

        sql = "insert into `capture_cpu_sys_top` " \
              "(time,cpu,user_nice,sys,idle,iow,total_raw,available_raw,free,used_raw) " \
              "values('%s','%d','%d','%d','%d','%d','%d','%d','%d','%d')" \
              % (create_time, cpu, user_nice, sys, idle, iow, total_raw, available_raw, free,used_raw)
        # print(sql)
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


def todb_capture_cpu_idle_low(sheetname):
    data = pd.read_excel(file, sheet_name=sheetname)
    df = pd.DataFrame(data)
    for k in range(len(data['TIME'])):
        df['user_nice'] = df['%user'] + df['%nice']
        user_nice = df['user_nice'][k]
        print(user_nice)
        cpu = df['%cpu'][k]
        sys = df['%sys'][k]
        idle = df['%idle'][k]
        iow = df['%iow'][k]
        total_raw = df['Total_RAM'][k]
        available_raw = df['Available_RAM'][k]
        used_raw = df['Used_RAM'][k]
        free = df['free'][k]
        tstr = '2020-' + str(data['Folder'][k] + ' ' + data['TIME'][k])
        print(tstr)
        try:
            time.strptime(tstr, "%Y-%m-%d %H:%M:%S")
            create_time = datetime.datetime.fromtimestamp(time.mktime(time.strptime(tstr, "%Y-%m-%d %H:%M:%S")))
        except Exception:
            # traceback.print_exc()
            continue
        print(create_time)

        sql = "insert into `capture_cpu_idle_low` " \
              "(time,cpu,user_nice,sys,idle,iow,total_raw,available_raw,free,used_raw) " \
              "values('%s','%d','%d','%d','%d','%d','%d','%d','%d','%d')" \
              % (create_time, cpu, user_nice, sys, idle, iow, total_raw, available_raw, free,used_raw)
        # print(sql)
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


def todb_capture_cpu_iow_top(sheetname):
    data = pd.read_excel(file, sheet_name=sheetname)
    df = pd.DataFrame(data)
    for k in range(len(data['TIME'])):
        df['user_nice'] = df['%user'] + df['%nice']
        user_nice = df['user_nice'][k]
        print(user_nice)
        cpu = df['%cpu'][k]
        sys = df['%sys'][k]
        idle = df['%idle'][k]
        iow = df['%iow'][k]
        total_raw = df['Total_RAM'][k]
        available_raw = df['Available_RAM'][k]
        used_raw = df['Used_RAM'][k]
        free = df['free'][k]
        tstr = '2020-' + str(data['Folder'][k] + ' ' + data['TIME'][k])
        print(tstr)
        try:
            time.strptime(tstr, "%Y-%m-%d %H:%M:%S")
            create_time = datetime.datetime.fromtimestamp(time.mktime(time.strptime(tstr, "%Y-%m-%d %H:%M:%S")))
        except Exception:
            # traceback.print_exc()
            continue
        print(create_time)

        sql = "insert into `capture_cpu_iow_top` " \
              "(time,cpu,user_nice,sys,idle,iow,total_raw,available_raw,free,used_raw) " \
              "values('%s','%d','%d','%d','%d','%d','%d','%d','%d','%d')" \
              % (create_time, cpu, user_nice, sys, idle, iow, total_raw, available_raw, free,used_raw)
        # print(sql)
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


def todb_capture_mem_available_low(sheetname):
    data = pd.read_excel(file, sheet_name=sheetname)
    df = pd.DataFrame(data)
    for k in range(len(data['TIME'])):
        df['user_nice'] = df['%user'] + df['%nice']
        user_nice = df['user_nice'][k]
        print(user_nice)
        cpu = df['%cpu'][k]
        sys = df['%sys'][k]
        idle = df['%idle'][k]
        iow = df['%iow'][k]
        total_raw = df['Total_RAM'][k]
        available_raw = df['Available_RAM'][k]
        used_raw = df['Used_RAM'][k]
        free = df['free'][k]
        tstr = '2020-' + str(data['Folder'][k] + ' ' + data['TIME'][k])
        print(tstr)
        try:
            time.strptime(tstr, "%Y-%m-%d %H:%M:%S")
            create_time = datetime.datetime.fromtimestamp(time.mktime(time.strptime(tstr, "%Y-%m-%d %H:%M:%S")))
        except Exception:
            # traceback.print_exc()
            continue
        print(create_time)

        sql = "insert into `capture_mem_available_low` " \
              "(time,cpu,user_nice,sys,idle,iow,total_raw,available_raw,free,used_raw) " \
              "values('%s','%d','%d','%d','%d','%d','%d','%d','%d','%d')" \
              % (create_time, cpu, user_nice, sys, idle, iow, total_raw, available_raw, free,used_raw)
        # print(sql)
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


def todb_capture_mem_free_low(sheetname):
    data = pd.read_excel(file, sheet_name=sheetname)
    df = pd.DataFrame(data)
    for k in range(len(data['TIME'])):
        df['user_nice'] = df['%user'] + df['%nice']
        user_nice = df['user_nice'][k]
        print(user_nice)
        cpu = df['%cpu'][k]
        sys = df['%sys'][k]
        idle = df['%idle'][k]
        iow = df['%iow'][k]
        total_raw = df['Total_RAM'][k]
        available_raw = df['Available_RAM'][k]
        used_raw = df['Used_RAM'][k]
        free = df['free'][k]
        tstr = '2020-' + str(data['Folder'][k] + ' ' + data['TIME'][k])
        print(tstr)
        try:
            time.strptime(tstr, "%Y-%m-%d %H:%M:%S")
            create_time = datetime.datetime.fromtimestamp(time.mktime(time.strptime(tstr, "%Y-%m-%d %H:%M:%S")))
        except Exception:
            # traceback.print_exc()
            continue
        print(create_time)

        sql = "insert into `capture_mem_free_low` " \
              "(time,cpu,user_nice,sys,idle,iow,total_raw,available_raw,free,used_raw) " \
              "values('%s','%d','%d','%d','%d','%d','%d','%d','%d','%d')" \
              % (create_time, cpu, user_nice, sys, idle, iow, total_raw, available_raw, free,used_raw)
        # print(sql)
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


def todb_capture_mem_used_top(sheetname):
    data = pd.read_excel(file, sheet_name=sheetname)
    df = pd.DataFrame(data)
    for k in range(len(data['TIME'])):
        df['user_nice'] = df['%user'] + df['%nice']
        user_nice = df['user_nice'][k]
        print(user_nice)
        cpu = df['%cpu'][k]
        sys = df['%sys'][k]
        idle = df['%idle'][k]
        iow = df['%iow'][k]
        total_raw = df['Total_RAM'][k]
        available_raw = df['Available_RAM'][k]
        used_raw = df['Used_RAM'][k]
        free = df['free'][k]
        tstr = '2020-' + str(data['Folder'][k] + ' ' + data['TIME'][k])
        print(tstr)
        try:
            time.strptime(tstr, "%Y-%m-%d %H:%M:%S")
            create_time = datetime.datetime.fromtimestamp(time.mktime(time.strptime(tstr, "%Y-%m-%d %H:%M:%S")))
        except Exception:
            # traceback.print_exc()
            continue
        print(create_time)

        sql = "insert into `capture_mem_used_top` " \
              "(time,cpu,user_nice,sys,idle,iow,total_raw,available_raw,free,used_raw) " \
              "values('%s','%d','%d','%d','%d','%d','%d','%d','%d','%d')" \
              % (create_time, cpu, user_nice, sys, idle, iow, total_raw, available_raw, free,used_raw)
        # print(sql)
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


#将sheetname传入函数
# todb_capture_first('capture_first')
# todb_capture_last('capture_last')
# todb_capture_cpu_user_top('capture_cpu_user_top')
# todb_capture_cpu_usernice_top('capture_cpu_usernice_top')
# todb_capture_cpu_sys_top('capture_cpu_sys_top')
# todb_capture_cpu_idle_low('capture_cpu_idle_low')
# todb_capture_cpu_iow_top('capture_cpu_iow_top')
# todb_capture_mem_available_low('capture_mem_available_low')
# todb_capture_mem_free_low('capture_mem_free_low')
todb_capture_mem_used_top('capture_mem_used_top')